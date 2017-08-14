#!/usr/bin/python
from pythonzimbra.tools.auth import authenticate
from pythonzimbra.communication import Communication
from pprint import pprint
auth_url = 'https://exemple.com:7071/service/admin/soap'
zimbrauser = 'admin'
zimbrapass = 'password'


def getCota_domais(url, admin, passwd):
    try:
        comm = Communication(url)
        token = authenticate(url, admin, passwd,
                             'name', admin_auth=True, request_type='json')
        request = comm.gen_request(token=token)
        with open('file', 'r') as f:
            domains = f.readlines()
            for d in domains:
                request_dict = {'domain': d.strip(),
                                'allServers': 0,
                                'limit': 0,
                                'sortBy': 'totalUsed',
                                'offset': 0
                                }

                request.add_request(request_name='GetQuotaUsageRequest',
                                    request_dict=request_dict,
                                    namespace='urn:zimbraAdmin')
                response = comm.send_request(request)
                resp = response.get_response()['GetQuotaUsageResponse']
                if resp:
                    for key in resp:
                        try:
                            pprint(resp[key])
                        except KeyError:
                            pprint(resp)
    except Exception as e:
        print 'Error', e

getCota_domais(auth_url, zimbrauser, zimbrapass)
