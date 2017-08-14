#!/usr/bin/python
# -*- coding:utf-8 -*-
import dns.resolver


def consult_mx():

    with open('file domains') as f:
        domains = f.readlines()
        for x in domains:
            try:
                mx = dns.resolver.query(x.strip(), 'MX')[0].exchange
                print x, mx

            except Exception as e:
                print 'Error',e

consult_mx()
