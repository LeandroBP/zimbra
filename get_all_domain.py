#!/usr/bin/python
# -*- encoding: utf8 -*-
from pythonzimbra.tools.dict import get_value
from pythonzimbra.request_xml import RequestXml
from pythonzimbra.tools.auth import authenticate
from pythonzimbra.request_json import RequestJson
from pythonzimbra.communication import Communication

adurl = 'https://exemple.com:7071/service/admin/soap'
zbruser = 'account admin'
zbrpass = 'password'
with open('file domains', 'r') as f:
    domains = f.readlines()


def get_domain(url, admin, passwd):
    comm = Communication(url)
    token = authenticate(url, admin, passwd,
                         admin_auth=True, request_type='json')
    request = comm.gen_request(token=token)
    request_dict = {'query': '(zimbraMailAddress=*)',
                    'countOnly': 0,
                    'types': 'accounts',
                    'offset': 0,
                    'limit': 0,
                    }
    request.add_request(request_name='SearchDirectoryRequest',
                        request_dict=request_dict,
                        namespace='urn:zimbraAdmin'
                        )
    response = comm.send_request(request)
    resp = response.get_response()
    print resp
get_domain(adurl, zbruser, zbrpass)
