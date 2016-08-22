from django.conf.urls import patterns, url

urlpatterns = patterns('sunburst.views',
          url(r'^sunburst/(?P<accession>\d+)$', 'index', name='sunburst_index'),
          url(r'^sunburst/json/reports/(?P<accession>\d+)$', 'json_sunburst_reports', name='json_sunburst_reports'),
          url(r'^sunburst/json/post/reports/$', 'json_sunburst_reports', name='json_sunburst_reports'),
)
