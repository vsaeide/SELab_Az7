from django.db import models
from django.contrib.auth.models import User


USER_TYPE = (
    (0, 'doctor'),
    (1, 'patient'),

)

class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    password = models.TextField()
    national_id = models.CharField(max_length=50)
    type = models.IntegerField(choices=USER_TYPE)
