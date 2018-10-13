#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render,redirect
from asset.models import Host
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

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

