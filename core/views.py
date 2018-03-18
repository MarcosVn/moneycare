# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from core.models import ReceitaDespesa


def home(request):
    return render(request, 'index.html')


def receita(request):
    return render(request, 'receita_crud.html')

def receita_despesa(request):
    receitas = serialize("json", ReceitaDespesa.objects.all())
    return HttpResponse(receitas, content_type="application/json")





