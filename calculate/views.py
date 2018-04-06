# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from django.template.defaulttags import register

from .models import Sheet

@register.filter
def get_item(dictionary, col,row):
    return dictionary.get('%s%s' % (col, row))

@register.simple_tag
def my_tag(col, row, sheet, dict):
    key = '%s_%s%s' % (sheet, col, row)

    if key in dict:
        return dict[key]
    else:
        return ''




# Create your views here.
def generate_sheets():
    cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    rows = range(1, 21)
    sheets = {}
    sheets['cols'] = cols
    sheets['rows'] = rows
    return sheets


def index(request):
    context = generate_sheets()
    sheet = Sheet.objects.get(id=1)
    context['sheets'] = sheet.get_sheet_parameters()
    return render(request, "index.html", context)


def admin(request):
    if request.method == "GET":
        context = generate_sheets()
        sheet = Sheet.objects.get(id=1)
        context['sheets'] = sheet.get_sheet_parameters()
        context['is_admin'] = True
        return render(request, "index.html", context)
    else:
        cells_dict = {}
        for key in request.POST:
            if key.startswith('cell'):
                sheet = key.split('-')[1]
                col = key.split('-')[2]
                row = key.split('-')[3]
                if request.POST[key]:
                    if request.POST[key].startswith('='):
                        type = 'formula'
                    else:
                        type = 'value'
                    cells_dict['%s_%s%s' % (sheet, col, row)] = {'value': request.POST[key], 'type': type}
        sheet = Sheet.objects.get(id=1)
        sheet.set_sheet_parameters(cells_dict)
        return redirect('/calculation/admin')


def ret_json(request):
    sheet = Sheet.objects.get(id=1)
    json_sheet = sheet.get_sheet_parameters()
    return JsonResponse(json_sheet)
