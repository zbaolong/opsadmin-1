#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render,redirect
from django.http import HttpResponse
from asset.models import Host
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
#from django.forms.models import model_to_dict
#from django.http import JsonResponse
import json

class PrivatePaginator(Paginator):
    def __init__(self,curren_page,per_page_num,*args,**kwargs):
        self.curren_page = int(curren_page)
        self.per_page_num = int(per_page_num)
        super(PrivatePaginator,self).__init__(*args,**kwargs)

    def perge_num_range(self):
        part = int(self.per_page_num / 2)
        if self.num_pages < self.per_page_num:
            return range(1,self.num_pages+1)
        if self.curren_page <= self.per_page_num:
            return range(1,self.per_page_num+1)
        if (self.curren_page + part) > self.num_pages:
            return range(self.num_pages-self.per_page_num,self.num_pages+1)
        return range(self.curren_page-part,self.curren_page+part+1)


def show_hosts(request):
    curren_page = request.GET.get('p')
    if not curren_page:
        curren_page = 1
    host_obj = Host.objects.all()
    paginator = PrivatePaginator(curren_page,1,host_obj,1)
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

def del_host(request):
    host_id = request.GET.get('host_id')
    Host.objects.filter(id=host_id).delete()
    return redirect("/show_hosts/")

@csrf_exempt
def add_host(request):
    data = {}
    if request.POST.get('hostname'):
        data['hostname'] = request.POST.get('hostname')
    if request.POST.get('mac'):
        data['mac'] = request.POST.get('mac')
    if request.POST.get('outer_ip'):
        data['outer_ip'] = request.POST.get('outer_ip')
    if request.POST.get('os_platform'):
        data['os_platform'] = request.POST.get('os_platform')
    if request.POST.get('os_type'):
        data['os_type'] = request.POST.get('os_type')
    if request.POST.get('os_version'):
        data['os_version'] = request.POST.get('os_version')
    if request.POST.get('os_kernel'):
        data['os_kernel'] = request.POST.get('os_kernel')
    if request.POST.get('cpu_arch'):
        data['cpu_arch'] = request.POST.get('cpu_arch')
    if request.POST.get('cpu_physical_num'):
        data['cpu_physical_num'] = request.POST.get('cpu_physical_num')
    if request.POST.get('cpu_logical_num'):
        data['cpu_logical_num'] = request.POST.get('cpu_logical_num')
    if request.POST.get('mem_total'):
        data['mem_total'] = request.POST.get('mem_total')
    Host.objects.create(**data)
    return HttpResponse("OK")


