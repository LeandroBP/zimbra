#!/usr/bin/env python
# -*- coding: latin-1 -*-
# author: Leandro Pereira
# contato: leandrobatistapereira98@gmail.com
#############################################
import socket
import sys
import time
import ldap
import iptc

servidor = ['servidor1', 'servidor2', 'servidor3']


def conect_ldap():
    # CONEXAO COM OS LDAP'S
    try:
        for s in servidor:
            # CONECTANDO-SE AO LDAP
            conn = ldap.initialize('ldap://%s:389' % s)
            # PASSANDO O USER E SENHA
            conn.simple_bind_s('user bind', 'passwd')
            # TIMEOUT DE 10 SEGUNDOS
            conn.set_option(ldap.OPT_TIMEOUT, 10)
            # BUSCA NA BASE PELO E-MAIL
            conn.search_s('search base',
                          ldap.SCOPE_SUBTREE, '(mail=*)', ['cn', 'mail'])
            # SE TUDO ESTA OK AGUARDA 1s E PRINTA NA TELA
            time.sleep(1)
            print('%s %s Conexao Realizada com Sucesso!') % (time.ctime(), s)
            # CONVERTENDO NOME EM IP
            ip = socket.gethostbyname(s)
            return ip

    # EXCECAO EM CASO DE TIMEOUT
    except (ldap.SERVER_DOWN, ldap.TIMEOUT) as e:
        # SE O ERRO OCORRER AS REGRAS SAO APLICADAS
        if e:
            print("Ocorreu o seguinte error (%s)") % e
            rules_iptables(s)
    # CASO NAO OCORRA O PROGRAMA SAI
        else:
            sys.exit(0)


def rules_iptables(ip):

    try:
        # APLICAR AS REGRAS DE IPTABLES
        print("\nAplicando regras do IPTABLES...")
        # CRIANDO UMA REGRA DO TIPO INPUT
        chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
        # APLICANDO A REGRA
        rule = iptc.Rule()
        # SELECIONANDO A INTERFACE
        rule.in_interface = "eth0"
        # PEGANDO O IP A SER BLOQUEADO
        rule.src = "%s" % ip
        # ADICIONANDO A POLITICA REJECT
        target = iptc.Target(rule, "REJECT")
        rule.target = target
        chain.insert_rule(rule)
        time.sleep(1)
        # ESPERANDO 2 SEGUNDOS
        print("Regras Aplicadas... %s") % time.ctime()
        time.sleep(5)
        flush_rules()
        time.sleep(10)
        conect_ldap()
    except (ldap.SERVER_DOWN, ldap.TIMEOUT) as i:
        if i:
            rules_iptables()
        else:
            pass


def flush_rules():
    # DANDO UM FLUSH NA REGRA DE BLOQUEIO
    chainIn = iptc.Chain(iptc.Table(iptc.Table.FILTER), 'INPUT')
    chainIn.flush()
    # CHAINOUT = IPTC.CHAIN(IPTC.TABLE(IPTC.TABLE.FILTER), 'OUTPUT')
    # CHAINOUT.FLUSH()


conect_ldap()
