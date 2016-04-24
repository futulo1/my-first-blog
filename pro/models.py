from django.db import models
from django.contrib.auth.models import User


# from Main_Static.event_creation_logic import find_time
class pro_users(models.Model):
    users = models.ForeignKey(User)
    start_working = models.TimeField(default="00:00:00")
    finish_working = models.TimeField(default="00:00:00")
    date_of_working = models.DateField(default="2016-04-21")
    holidays = models.DateField(default="2016-04-21")


# Create your models here.
class vstrecha(models.Model):
    start = models.TimeField(default="00:00:00")
    finish = models.TimeField(default="00:00:00")
    length = models.TimeField(default="00:00:00")
    date_of_meeting = models.DateField(default="2016-04-21")
    index = models.AutoField(primary_key=True)
    name = models.CharField(max_length=127)

class users_vstrecha(models.Model):
    vstrecha_obj = models.ForeignKey(vstrecha, on_delete=models.CASCADE)
    user_obj = models.ForeignKey(pro_users, on_delete=models.CASCADE)


