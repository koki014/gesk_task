from distutils.debug import DEBUG
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Payload

# Create your views here.

class PayloadList(ListView):
    model = Payload
    template_name = 'payload_list.html'
    context_object_name = 'payloads'
    ordering = ['-timestamp']
    paginate_by = 10



class PayloadDetail(DetailView):
    model = Payload
    template_name = 'payload_detail.html'
    context_object_name = 'payload'
    ordering = ['-timestamp']