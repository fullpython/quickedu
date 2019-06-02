from django.shortcuts import render

from django.views.generic import TemplateView

class AdminHomeView(TemplateView):
    template_name = 'my_admin/index.html'

