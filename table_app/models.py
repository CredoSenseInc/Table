from django.db import models

# Create your models here.

class Table(models.Model):
    s_1 = models.IntegerField(db_column='s_1', blank = False, default= -214748)
    s_2 = models.IntegerField(db_column='s_2', blank = False, default= -214748)
    s_3=  models.IntegerField(db_column='s_3', blank = False, default= -214748)
    time_date= models.CharField(db_column='time_date', max_length=255, blank= False)
