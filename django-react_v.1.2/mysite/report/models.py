from django.db import models
import datetime
from django.utils import timezone
from django.conf import settings
# Create your models here.

# Models file is how Django build database tables to store band objects.
DATE_INPUT_FORMATS = ('%b %d, %Y')

class Report(models.Model):
    name = models.CharField(max_length=128,null=False,blank=False,unique=True)
    date1 = models.DateField(default= timezone.now())
    impressions_negated_date1 = models.TextField(max_length=5000,null=True,blank=True)
    impressions_positive_date1 = models.TextField(max_length=5000,null=True,blank=True)
    date2 = models.DateField(default= timezone.now())
    impressions_negated_date2 = models.TextField(max_length=5000,null=True,blank=True)
    impressions_positive_date2 = models.TextField(max_length=5000,null=True,blank=True)
    date3 = models.DateField(default= timezone.now())
    impressions_negated_date3 = models.TextField(max_length=5000,null=True,blank=True)
    impressions_positive_date3 = models.TextField(max_length=5000,null=True,blank=True)
