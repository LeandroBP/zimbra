#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests


def put_api():
    with open('/home/rootoso/dominios_mx_u.txt') as d:
        domain_urls = d.readlines()
        url = 'http://localhost:81/mxhero/mxlite/domain/'
        data = {"inbound_server": "mta-in",
                "default_rules": "true",
                "directory_type": "zimbra",
                "adsync_host": "ldap host",
                "adsync_port": "389",
                "adsync_user": "uid=zimbra,cn=admins,cn=zimbra",
                "adsync_pass": "passwd",
                "admin_email": "e-mail admin"}
        headers = {
            'access-control-allow-origin': '*',
            'accept': 'application/json',
            'content-type': 'application/json',
        }
    for doms in domain_urls:
        try:
            response = requests.put(
                url + doms.strip(), json=data, headers=headers)
            if response.status_code == 201:
                with open('novos_domains.txt', 'a') as f:
                    f.write(response.text)
            elif response.status_code == 501:
                print 'Erro inesperado.'
            else:
                print 'O dominio ja existe:', doms
        except Exception as e:
            print 'Failed my boy: ', e


put_api()
