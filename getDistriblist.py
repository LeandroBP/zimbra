#!/usr/bin/python
# -*- encoding: utf8 -*-
from pythonzimbra.tools.auth import authenticate
from pythonzimbra.communication import Communication

admurl = 'https://exemple.com:7071/service/admin/soap'
zimbruser = 'admin'
zimbrpass = 'password'
with open('list', 'r') as f:
    domains = f.readlines()


def get_distribution_lists(url, admin, password):
    comm = Communication(url)
    token = authenticate(url, admin, password,
                         admin_auth=True, request_type='json')
    request = comm.gen_request(token=token)
    #request_dict{}
    request.add_request(request_name='GetHsmStatusRequest',
                        #request_dict=request_dict,
                        namespace='urn:zimbraAdmin')
    response = comm.send_request(request)
    resp = response.get_response()['GetHsmStatusResponse']
    print(resp)


get_distribution_lists(admurl, zimbruser, zimbrpass)
