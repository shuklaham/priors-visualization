from django.shortcuts import render
from models import Report
from rest_framework import generics
from serializers import ReportSerializer
from django.core import serializers
from django.http import JsonResponse
import json
import urllib2
import time
from startParser import startParser

# Create your views here.

def basic_page(request):
    return render(request,'report/index.html')

def all_reports(request):
    return render(request,'report/all_reports.html')

class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

def parsed_report(request, mrn_id,acc_id):
    # print 'Get json from Jai api and process it and get something like below'
    new_report = startParser(mrn_id,acc_id)
    return JsonResponse(new_report,safe=False)

def report_intro(request, mrn_id,acc_id):
    # report_json = {"id":str(report_id)}
    report_json = {"mrn_id":str(mrn_id),"acc_id":str(acc_id)}
    json_string = json.dumps(report_json)
    return render(request, "report/visualize.html", {'report': json_string})
