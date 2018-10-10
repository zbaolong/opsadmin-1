#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from asset.models import Host
import json

@csrf_exempt
def add_host(request):
    if request.method == 'POST':
        data = json.loads(json.loads(request.body))
        print(data)
        Host.objects.create(**data)
        return HttpResponse("add host ok")
