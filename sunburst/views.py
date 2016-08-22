import requests
import json
import logging

from django.http import HttpResponse, JsonResponse
from django.utils.http import urlquote_plus

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from refvol.models import Patient, Order, Radiologist 
from refvol.views import default_context_dict

from sunburst.models import PatientReportsViewed

from .utils import parseConceptsForVisualization

METAMAP_BIN_DIRECTORY= "/opt/public_mm_2016/bin/"
SOLR_DOCUMENT_URI = 'https://localhost:3097/solr/rad/select'

# Create your views here.
@csrf_exempt
@login_required
def json_sunburst_reports(request, accession=None, start=None, rows=None):
  MAX_REPORTS = 3

  try:
    if accession is None:
      accession = request.POST['accession']
    if start is None:
        start = request.POST.get('start', 0)
    if rows is None:
      rows = request.POST.get('rows', MAX_REPORTS)
      rows = max(rows, MAX_REPORTS)

    accession = int(accession)
    order = Order.objects.get(accession=accession)
    patient = Patient.objects.get(order__accession=accession)

    patient_name = '%s, %s' % (patient.lname, patient.fname)
    rv = PatientReportsViewed(user=request.user, patient=patient)
    rv.save()

    cornell_preceding_orders = patient.order_set.filter(modality=order.modality, finalized=True, finalized_time__lte=order.finalized_time)[:rows]

    solr_query_accessions = []
    for order in cornell_preceding_orders:
      solr_query_accessions.append(urlquote_plus("accession:{0}".format(order.accession)))

    solr_query = '?q=(%s)' % ' OR '.join(solr_query_accessions)

    field_list = ['accession', 'age', 'sex', 'technique_all', 'patient_history_all', 'finalized_time',
                  'impression_all', 'impression_negated', 'impression_positive']
    field_list_str = '%2C'.join(field_list) 

    request_uri =  SOLR_DOCUMENT_URI + solr_query + \
        '&fl='+ field_list_str +'&start=' + str(start) + \
        '&rows=' + str(rows) + '&sort=completed_time desc&wt=json&indent=false'

    req = requests.get(request_uri, verify=False)

    content_type = "application/json"
    content = req.content if req.ok else ''

    reports_dict = json.loads(content)

    for report in reports_dict["response"]["docs"]:
      report["patient_name"] = patient_name
      unnormalized_keys = ["age", "technique_all",
        "impression_all", "impression_positive", "impression_negated"]

      for key in unnormalized_keys:
        if key in report.keys():
          report[key] = report[key][0]
        else:
          report[key] = ""
    
    visualization_json = parseConceptsForVisualization(reports_dict["response"]["docs"], METAMAP_BIN_DIRECTORY)
    resp = JsonResponse(dict(metamap_vis_concepts=visualization_json), content_type=content_type)

    if req.ok:
        return resp
    else:
        logging.warning("return_solr_query Solr Request not OK: %s" % req.content)
        return HttpResponse(req.content, content_type="application/json")

  except Exception as inst:
    if settings.DEBUG:
      logging.warning("json_return_report Failure: %s" % inst)
      return JsonResponse(dict(json_status = "json_return_report Failure: %s" % inst))
    else:
      logging.warning("json_return_report Failure: %s" % inst)
      return JsonResponse(dict(json_status='query failed, see logs %s' % inst))


# Create your views here.
@csrf_exempt
@login_required
def index(request, accession=None):
    d = default_context_dict(
      request.user, rads=["%s %s" % (r.fname, r.lname) for r in Radiologist.objects.all()],
      accession=accession,
    )
    return render(request, "index.html", d)
