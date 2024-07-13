from django.db import models
from doctor.models import Doctor,AvailableTime
from patient.models import Patient

APPINTMENT_STATUS =[

    ('Complated','Complated'),
    ('Running','Running'),
    ('Pending','Pending'),
]
APPINTMENT_TYPE =[
    ('Online','Online'),
    ('Offline','Offline'),
]
class Appintment(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    appoinment_type=models.CharField(choices=APPINTMENT_TYPE ,max_length=50)
    appoinment_status=models.CharField(choices=APPINTMENT_STATUS,max_length=50,default="Pending")
    symptom=models.TextField()
    time=models.ForeignKey(AvailableTime,on_delete=models.CASCADE)
    cancel=models.BooleanField(default=False)

    def __str__(self):
        return f"Doctor :{self.doctor.user.first_name}, Patient {self.patient.user.first_name}"