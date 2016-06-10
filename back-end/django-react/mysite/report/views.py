from django.shortcuts import render
from models import Report
from rest_framework import generics
from serializers import ReportSerializer
from django.core import serializers
from django.http import JsonResponse
import json
import urllib2
import time
from start import startParser

# Create your views here.

def basic_page(request):
    return render(request,'report/index.html')

def all_reports(request):
    return render(request,'report/all_reports.html')

class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

# def band(request, band_id):
#     band = Band.objects.get(pk=band_id)
#     return render(request,'band/band.html',{'band':band})

def parsed_report(request, report_id):
    # print 'Get json from Jai api and process it and get something like below'
  #   new_report = [{
  #   "x": "Oct-02-2015",
  #   "y": "Adrenal Nodules",
  #   "z":"pos",
  #   "s":"Progression of disease with increase in lymphadenopathy and bilateral adrenal nodules"
  # }, {
  #   "x": "Oct-02-2015",
  #   "y": "Retroperitoneal Edema",
  #   "z":"pos",
  #   "s":"Increased mesenteric/retroperitoneal edema"
  # }]
    new_report = startParser(report_id)
  #   new_report = [{"finding": "Hepatic Lesions", "context": "", "sentence": "new suspicious hepatic lesions", "date": "2015-08-09", "colorCode": "neg"}, {"finding": "Lymphadenopathy", "context": "", "sentence": "Mild abdominopelvic lymphadenopathy , with nodes stable or slightly decreased in size", "date": "2015-08-09", "colorCode": "pos"}, {"finding": "Hepatic Metastases", "date": "2015-08-09", "colorCode": "neutral", "context": "", "sentence": ""}, {"finding": "Disease Progression Nos", "date": "2015-08-09", "colorCode": "neutral", "context": "", "sentence": ""}, {"finding": "Hepatic Lesions", "context": "", "sentence": "new hepatic lesions identified", "date": "2015-10-15", "colorCode": "neg"}, {"finding": "Hepatic Metastases", "context": "RIGHT", "sentence": "Interval decrease in size of right hepatic metastases", "date": "2015-10-15", "colorCode": "pos"}, {"finding": "Disease Progression Nos", "date": "2015-10-15", "colorCode": "neutral", "context": "", "sentence": ""}, {"finding": "Lymphadenopathy", "date": "2015-10-15", "colorCode": "neutral", "context": "", "sentence": ""}, {"finding": "Disease Progression Nos", "context": "", "sentence": "Progression of disease with increase in lymphadenopathy and bilateral adrenal nodules", "date": "2015-12-10", "colorCode": "pos"}, {"finding": "Lymphadenopathy", "context": "Increase", "sentence": "Progression of disease with increase in lymphadenopathy and bilateral adrenal nodules", "date": "2015-12-10", "colorCode": "pos"}, {"finding": "Hepatic Metastases", "date": "2015-12-10", "colorCode": "neutral", "context": "", "sentence": ""}, {"finding": "Hepatic Lesions", "date": "2015-12-10", "colorCode": "neutral", "context": "", "sentence": ""}, ["2015-08-09", "2015-10-15", "2015-12-10"], ["Hepatic Metastases", "Disease Progression Nos", "Hepatic Lesions", "Lymphadenopathy"]]
    return JsonResponse(new_report,safe=False)

def report_intro(request, report_id):
    #report = Report.objects.get(pk=report_id)
    # print type(band)
    # print type(str(report_id))
    report_json = {"id":str(report_id)}
    # print 'I am here'
    json_string = json.dumps(report_json)
    # print type(json_string)
    # print json_string
    return render(request, "report/test.html", {'report': json_string})
    # serialized_obj = serializers.serialize('json', [ band, ])
    # print type(serialized_obj)
    # return render(request,'band/test.html',{'band':band})
