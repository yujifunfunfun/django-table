from django.views.generic.edit import FormView
from django.views.generic import View
from django.shortcuts import render, redirect
from .forms import KimetsuForm
from .models import Kimetsu

class AddView(FormView):
  template_name = 'hello/add.html'
  form_class = KimetsuForm
  success_url = '/list'

  def form_valid(self, form):
    form.save()
    return super().form_valid(form)

class ListView(View):
  def get(self,request):
    data = Kimetsu.objects.all()
    params = {'data': data}
    return render(request, 'hello/list.html', params)

