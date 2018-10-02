#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import subprocess
import platform
import json
import requests


def get_os_info():
    os_info = {}
    ret = platform.platform().split('-')
    os_info['os_platform'] = ret[0]
    os_info['os_type'] = ret[5]
    os_info['os_kernel'] = ret[1]
    return os_info

def get_cpu_info():
    cpu_info = {}
    cpu_arch_cmd = "lscpu | grep Architecture | awk '{print $2}'"
    cpu_info['cpu_arch'] = subprocess.check_output(cpu_arch_cmd,shell=True).strip('\n')
    cpu_num_cmd = "lscpu | grep ^CPU\(s\) | awk '{print $2}'"
    cpu_info['cpu_num'] = subprocess.check_output(cpu_num_cmd,shell=True).strip('\n')
    return cpu_info

def get_mem_info():
    mem_info = {}
    mem_total_cmd = "cat /proc/meminfo  | grep MemTotal | awk '{print $2}'"
    mem_info['mem_total'] = round(float(subprocess.check_output(mem_total_cmd,shell=True).strip('\n')) / 1024 /1024,2)
    return mem_info

def asset_info():
    asset_data = {}
    asset_data['os_info'] = get_os_info()
    asset_data['cpu_info'] = get_cpu_info()
    asset_data['mem_info'] = get_mem_info()
    return asset_data

def run():
    data = asset_info()
    requests.post(
	    url="",
            data = data,
	)
    


if __name__ == '__main__':
    run()

