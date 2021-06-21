import django_tables2 as tables
from .models import Kimetsu

class KimetsuTable(tables.Table):
    class Meta:
        model = Kimetsu
        template_name = 'django_tables2/bootstrap4.html' 
        fields = ('name','gender','features')  