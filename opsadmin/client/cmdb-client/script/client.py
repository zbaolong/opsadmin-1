#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import platform
import json
import requests
import socket
import uuid
import psutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import settings


def get_mac():
    ret = {}
    result=uuid.UUID(int = uuid.getnode()).hex[-12:]
    ret['mac'] = ":".join([result[e:e+2] for e in range(0,11,2)])
    return ret

def get_hostname():
    ret = {}
    host_file = os.path.join(BASE_DIR,'file',settings.HOST_FILE)
    if not os.path.exists(settings.HOST_FILE):
    	hostname = socket.gethostname()
    	ret['hostname'] = hostname
        with open(host_file,'w') as f:
	    json.dump(ret,f)
    with open(host_file) as f:
	ret['hostname'] = json.load(f)['hostname']
    return ret

def get_ip():
    ret = {}
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
	ret['outer_ip'] = s.getsockname()[0]
    finally:
        s.close()
    return ret

def get_os_info():
    ret = {}
    result = platform.platform().split('-')
    ret['os_platform'] = result[0]
    ret['os_type'] = result[5]
    ret['os_version'] = result[-2]
    ret['os_kernel'] = result[1]
    return ret

def get_cpu_info():
    ret = {}
    cpu_arch_cmd = "lscpu | grep Architecture | awk '{print $2}'"
    ret['cpu_arch'] = subprocess.check_output(cpu_arch_cmd,shell=True).strip('\n')
    ret['cpu_physical_num'] = psutil.cpu_count(logical=False)
    ret['cpu_logical_num'] = psutil.cpu_count()
    return ret

def get_mem_info():
    ret = {}
    mem_total_cmd = "cat /proc/meminfo  | grep MemTotal | awk '{print $2}'"
    ret['mem_total'] = "%s %s" %(str(round(float(subprocess.check_output(mem_total_cmd,shell=True).strip('\n')) / settings.MEM_UNIT_DICT[settings.MEM_UNIT],2)),settings.MEM_UNIT)
    return ret

def asset_info():
    asset_data = {}
    hostname = get_hostname()
    mac = get_mac()
    outer_ip = get_ip()
    os_info = get_os_info()
    cpu_info = get_cpu_info()
    mem_info = get_mem_info()
    asset_data.update(hostname)
    asset_data.update(mac)
    asset_data.update(outer_ip)
    asset_data.update(os_info)
    asset_data.update(cpu_info)
    asset_data.update(mem_info)
    return asset_data

def run():
    data = asset_info()
    headers = {}
    r = requests.post(
	    url=settings.ASSET_API,
	    headers = headers,
            json = json.dumps(data),
	)
    print(r)
    


if __name__ == '__main__':
    run()
    #print(asset_info())

