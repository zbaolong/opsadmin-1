#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from asset.models import Host

def show_hosts(request):
    host_obj = Host.objects.all()
    return render(request,'asset/host.html',locals())

def show_detail_host(request):
    host_id = request.GET.get("host_id")
    host_obj = Host.objects.filter(id=host_id).first()
    print(host_obj)
    return render(request,'asset/detail_host.html',locals())
