#!/usr/bin/python3
# -*- coding:utf-8 -*-
from pythonzimbra.request_json import RequestJson
from pythonzimbra.communication import Communication
from pythonzimbra.request_xml import RequestXml
from pythonzimbra.tools.dict import get_value
from pythonzimbra.tools.auth import authenticate
import json


AUTH_URL = 'https://exemple.com:7071/service/admin/soap'
ZIMBRAUSER = 'Admin'
ZIMBRAPASSWD = 'Password'


def zimbra_comm():
    comm = Communication(AUTH_URL)
    token = authenticate(AUTH_URL, ZIMBRAUSER, ZIMBRAPASSWD,
                         'name', admin_auth=True, request_type='json')
    request = comm.gen_request(token=token)
    request_dict = {'query': '(!(zimbraIsSystemResource=TRUE))', 'countOnly': '0', 'types': 'domains',
                    'offset': 0}
    request.add_request(request_name='SearchDirectoryRequest',
                        request_dict=request_dict, namespace='urn:zimbraAdmin')
    response = comm.send_request(request)
    print json.dumps(response.get_response(), indent=2)

zimbra_comm()
