#!/usr/bin/env python
import sys
import urllib2
import argparse
import re
import dns.resolver
from urllib2 import urlopen
from colorama import Fore, Back, Style
from colorama import init
init()


def content_test(url, badip):

    try:
        request = urllib2.Request(url)
        opened_request = urllib2.build_opener().open(request)
        html_content = opened_request.read()
        retcode = opened_request.code

        matches = retcode == 200
        matches = matches and re.findall(badip, html_content)

        return len(matches) == 0
    except Exception, e:
        print "Error! %s" % e
        return False

bls = ["b.barracudacentral.org", "bl.spamcannibal.org",
       "bl.spamcop.net", "cbl.abuseat.org", "cdl.anti-spam.org.cn",
       "combined.abuse.ch", "combined.rbl.msrbl.net", "db.wpbl.info",
       "dnsbl-1.uceprotect.net", "dnsbl-2.uceprotect.net",
       "dnsbl-3.uceprotect.net", "dnsbl.cyberlogic.net",
       "dnsbl.sorbs.net", "drone.abuse.ch", "drone.abuse.ch",
       "duinv.aupads.org", "dul.dnsbl.sorbs.net", "dul.ru",
       "dyna.spamrats.com", "dynip.rothen.com",
       "http.dnsbl.sorbs.net", "images.rbl.msrbl.net",
       "ips.backscatterer.org", "ix.dnsbl.manitu.net",
       "korea.services.net", "misc.dnsbl.sorbs.net",
       "noptr.spamrats.com", "orvedb.aupads.org", "pbl.spamhaus.org",
       "phishing.rbl.msrbl.net", "proxy.bl.gweep.ca", "rbl.interserver.net",
       "relays.bl.gweep.ca", "relays.nether.net",
       "residential.block.transip.nl", "smtp.dnsbl.sorbs.net",
       "socks.dnsbl.sorbs.net", "spam.abuse.ch",
       "spam.dnsbl.sorbs.net", "spam.rbl.msrbl.net", "spam.spamrats.com",
       "spamrbl.imp.ch", "tor.dnsbl.sectoor.de",
       "torserver.tor.dnsbl.sectoor.de", "ubl.lashback.com",
       "ubl.unsubscore.com", "virus.rbl.jp",
       "virus.rbl.msrbl.net", "web.dnsbl.sorbs.net", "wormrbl.imp.ch",
       "xbl.spamhaus.org", "zen.spamhaus.org", "zombie.dnsbl.sorbs.net",
       "rracudacentral.org", "cbl.abuseat.org", "http.dnsbl.sorbs.net",
       "misc.dnsbl.sorbs.net", "socks.dnsbl.sorbs.net", "web.dnsbl.sorbs.net",
       "dnsbl-1.uceprotect.net", "dnsbl-3.uceprotect.net", "sbl.spamhaus.org",
       "zen.spamhaus.org", "psbl.surriel.com", "dnsbl.njabl.org", "rbl.spamlab.com",
       "noptr.spamrats.com", "cbl.anti-spam.org.cn", "dnsbl.inps.de",
       "httpbl.abuse.ch", "korea.services.net", "virus.rbl.jp", "wormrbl.imp.ch",
       "rbl.suresupport.com", "ips.backscatterer.org", "opm.tornevall.org", "multi.surbl.org",
       "tor.dan.me.uk", "relays.mail-abuse.org", "rbl-plus.mail-abuse.org",
       "access.redhawk.org", "rbl.interserver.net", "bogons.cymru.com", "bl.spamcop.net",
       "dnsbl.sorbs.net", "dul.dnsbl.sorbs.net", "smtp.dnsbl.sorbs.net", "spam.dnsbl.sorbs.net",
       "zombie.dnsbl.sorbs.net", "dnsbl-2.uceprotect.net", "pbl.spamhaus.org", "xbl.spamhaus.org",
       "ubl.unsubscore.com", "combined.njabl.org", "dyna.spamrats.com", "spam.spamrats.com", "cdl.anti-spam.org.cn",
       "drone.abuse.ch", "dul.ru", "short.rbl.jp", "spamrbl.imp.ch", "virbl.bit.nl", "dsn.rfc-ignorant.org",
       "dsn.rfc-ignorant.org", "netblock.pedantic.org", "ix.dnsbl.manitu.net", "rbl.efnetrbl.org",
       "blackholes.mail-abuse.org", "dnsbl.dronebl.org", "db.wpbl.info", "query.senderbase.org",
       "bl.emailbasura.org", "combined.rbl.msrbl.net", "multi.uribl.com", "black.uribl.com",
       "cblless.anti-spam.org.cn", "cblplus.anti-spam.org.cn", "blackholes.five-ten-sg.com",
       "sorbs.dnsbl.net.au", "rmst.dnsbl.net.au", "dnsbl.kempt.net", "blacklist.woody.ch",
       "rot.blackhole.cantv.net", "virus.rbl.msrbl.net", "phishing.rbl.msrbl.net",
       "images.rbl.msrbl.net", "spam.rbl.msrbl.net", "spamlist.or.kr", "dnsbl.abuse.ch",
       "bl.deadbeef.com", "ricn.dnsbl.net.au", "forbidden.icm.edu.pl", "probes.dnsbl.net.au",
       "ubl.lashback.com", "ksi.dnsbl.net.au", "uribl.swinog.ch", "bsb.spamlookup.net",
       "dob.sibl.support-intelligence.net", "url.rbl.jp", "dyndns.rbl.jp", "omrs.dnsbl.net.au",
       "osrs.dnsbl.net.au", "orvedb.aupads.org", "relays.nether.net", "relays.bl.gweep.ca",
       "relays.bl.kundenserver.de", "dialups.mail-abuse.org", "rdts.dnsbl.net.au",
       "duinv.aupads.org", "dynablock.sorbs.net", "residential.block.transip.nl",
       "dynip.rothen.com", "dul.blackhole.cantv.net", "mail.people.it", "blacklist.sci.kun.nl",
       "all.spamblock.unit.liu.se", "spamguard.leadmon.net", "csi.cloudmark.com"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Is This IP Bad?')
    parser.add_argument('-i', '--ip', help='IP address to check')
    parser.add_argument('--success', help='Also display GOOD',
                        required=False, action="store_true")
    args = parser.parse_args()

    if args is not None and args.ip is not None and len(args.ip) > 0:
        badip = args.ip
    else:
        my_ip = urlopen('http://icanhazip.com').read().rstrip()

    BAD = 0
    GOOD = 0

    for bl in bls:
        try:
            my_resolver = dns.resolver.Resolver()
            query = '.'.join(reversed(str(badip).split("."))) + "." + bl
            my_resolver.timeout = 5
            my_resolver.lifetime = 5
            answers = my_resolver.query(query, "A")
            answer_txt = my_resolver.query(query, "TXT")
            print ((Fore.RED + badip + ' is listed in ' + bl)
                   + ' (%s: %s)' % (answers[0], answer_txt[0]))
            BAD = BAD + 1

        except dns.resolver.NXDOMAIN:
            print (Fore.GREEN + badip + ' is not listed in ' + bl)
            GOOD = GOOD + 1

        except dns.resolver.Timeout:
            print ('WARNING: Timeout querying ' + bl)

        except dns.resolver.NoNameservers:
            print ('WARNING: No nameservers for ' + bl)

        except dns.resolver.NoAnswer:
            print ('WARNING: No answer for ' + bl)

    print('\n{0} is on {1}/{2} blacklists.\n'.format(badip, BAD, (GOOD + BAD)))
