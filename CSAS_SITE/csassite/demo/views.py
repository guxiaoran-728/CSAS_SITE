from django.shortcuts import render
from  .models import Msg
import json
import time
from django.views import View
from django.conf import settings
# Create your views here.


class vulnerab(object):
    def __init__(self):
        self.name = ''
        self.url = ''
        self.vuln_id = ''
        self.cvecode = ''
def store_vulner(filename = "vulner.json"):
    allvulners = []
    vuln_count=0
    with open(filename) as f:
        vuln_list = json.load(f)
    for vuln_dict in vuln_list:
        if vuln_dict['severity'] >= 3:
            new_vuln = vulnerab()
            new_vuln.name = vuln_dict['vt_name']
            new_vuln.url = vuln_dict['affects_url']
            new_vuln.vuln_id = vuln_dict['vuln_id']
            allvulners.append(new_vuln)
            vuln_count = vuln_count+1
    return allvulners


class Main(View):
    def get(self, request):
        for awvs_vuln in awvs_vulns:
            Msg.objects.create(name=awvs_vuln.name, link=awvs_vuln.url)
        data = Msg.objects.all().values()
            # print("漏洞名称："+awvs_vuln.name+"漏洞路径："+awvs_vuln.url)

        return render(request, 'demo/index.html', context={'data':data})
