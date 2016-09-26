from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView


def index(request):
    return render_to_response('index.html')

class index2(TemplateView):
    template_name = 'index.html'