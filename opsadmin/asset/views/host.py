#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from asset.models import Host

def show_hosts(request):
    host_obj = Host.objects.all()
    return render(request,'asset/host.html',locals())
