#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from asset.models import Host
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def show_hosts(request):
    curren_page = request.GET.get('p')
    if not curren_page:
        curren_page = 1
    host_obj = Host.objects.all()
    paginator = Paginator(host_obj,1)
    try:
        posts = paginator.page(curren_page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'asset/host.html',locals())

def show_detail_host(request):
    host_id = request.GET.get("host_id")
    host_obj = Host.objects.filter(id=host_id).first()
    print(host_obj)
    return render(request,'asset/detail_host.html',locals())
