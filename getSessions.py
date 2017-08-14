#!/usr/bin/python
# -*- encoding: utf-8 -*-
from pythonzimbra.tools.auth import authenticate
from pythonzimbra.communication import Communication

auth_url = 'https://exemple.com:7071/service/admin/soap'
zimbrauser = 'Admin'
zimbrapass = 'Password'


def get_sessions_soap(url, admin, passwd):
    try:
        comm = Communication(auth_url)
        token = authenticate(url, admin, passwd,
                             'name', admin_auth=True, request_type='json')
        request = comm.gen_request(token=token)
        request_dict = {'type': 'imap',
                        'refresh': 1
                        }

        request.add_request(request_name='GetSessionsRequest',
                            request_dict=request_dict,
                            namespace='urn:zimbraAdmin')
        response = comm.send_request(request)
        resp = response.get_response()['GetSessionsResponse']
        for _, value in resp.items():
            for v in value:
                print(v['name'])
            print('Total de contas usando imap %s') % (resp['total'])
    except Exception as e:
        pass
get_sessions_soap(auth_url, zimbrauser, zimbrapass)
