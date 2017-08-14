#!/usr/bin/python
# -*- encoding: utf8 -*-
from pythonzimbra.tools.auth import authenticate
from pythonzimbra.communication import Communication

admurl = 'https://exemple.com:7071/service/admin/soap'
zimbruser = 'admin'
zimbrpass = 'password'
with open('file', 'r') as f:
    domains = f.readlines()


def getallaccount(url, zimbuser, zimbpass):
    comm = Communication(url)
    token = authenticate(url, zimbuser, zimbpass,
                         admin_auth=True, request_type='json')
    request = comm.gen_request(token=token)
    for d in domains:
        request_dict = {'domain': {
            '_content': d.strip(),
            'by': 'name'
        }
        }
        request.add_request(request_name='GetAllAccountsRequest',
                            request_dict=request_dict,
                            namespace='urn:zimbraAdmin')
        response = comm.send_request(request)
        resp = response.get_response()['GetAllAccountsResponse']
        if resp:
            for key in resp:
                try:
                    print(str(resp[key][0]['name']))
                except KeyError:
                    print(str(resp[key]['name']))


getallaccount(admurl, zimbruser, zimbrpass)
