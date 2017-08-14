#!/usr/bin/python
# -*- coding:utf-8 -*-
import dns.resolver


def consult_mx():

    with open('file domain for delete', 'r') as f:
        domains = f.readlines()
        for x in domains:
            try:
                mx = dns.resolver.query(x.strip(), 'MX')[0].exchange
                dom = str(mx)
                if dom.startswith('mx.u.'):
                    with open('dominios_mxs.txt', 'a') as arq:
                        arq.write('DOMAIN: ' + str(x) +
                                  'MX: ' + str(mx) + '\n\n')
                else:
                    print x, mx

            except Exception as e:
                print 'Error', e
                with open('/home/rootoso/doms_mxs.txt', 'a') as arq_error:
                    arq_error.write('DOMAIN: ' + str(x) + '\n')


consult_mx()
