from django.db import models

class Kimetsu(models.Model):
  class Meta:
    db_table = 'post'
    
  CHOICE = {
    ('男','男'),
    ('女','女'),
  }

  name = models.CharField(max_length=10,verbose_name='name')
  gender = models.CharField(max_length=2,choices=CHOICE,verbose_name='gender')
  features = models.CharField(max_length=200,verbose_name='features')