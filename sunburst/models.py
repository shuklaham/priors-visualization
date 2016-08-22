from django.db import models
from django.contrib.auth.models import User
from refvol.models import Patient

# Create your models here.
class PatientReportsViewed(models.Model):
    def mrn_no_leading_zeros(self):
        return self.patient.mrn_no_leading_zeros()

    user = models.ForeignKey(User)
    patient = models.ForeignKey(Patient)
    viewed = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Prior Reports Visualization viewed' 