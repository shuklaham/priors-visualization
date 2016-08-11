from django.conf.urls import patterns, include, url
from django.contrib import admin
# Create your views here.
import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^$',views.basic_page),
	url(r'^(?P<mrn_id>(\d+))/(?P<acc_id>(\d+))/$',views.report_intro),
	url(r'^get_parsed_report/(?P<mrn_id>(\d+))/(?P<acc_id>(\d+))/$',views.parsed_report),
	url(r'^api/(?P<pk>\d+)/$',views.ReportDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)