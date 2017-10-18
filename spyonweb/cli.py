import argparse
import configparser
import os
import sys
import json
from .api import SpyOnWeb, SpyOnWebNotFound, SpyOnWebInvalidToken, SpyOnWebError

def main():
    parser = argparse.ArgumentParser(description='Request SpyOnWeb')
    subparsers = parser.add_subparsers(help='Commands')
    parser_a = subparsers.add_parser('config', help='Configuration of the tool')
    parser_a.add_argument('--token', '-t', help='Configure the tool')
    parser_a.set_defaults(which='config')
    parser_b = subparsers.add_parser('domain', help='Query a domain')
    parser_b.add_argument('DOMAIN', help='Domain to be requested')
    parser_b.add_argument('--json', '-j', action='store_true', help='Show raw json')
    parser_b.set_defaults(which='domain')
    parser_c = subparsers.add_parser('adsense', help='Query an adsense id')
    parser_c.add_argument('ID', help='id to be requested')
    parser_c.add_argument('--raw', '-r', action='store_true',
            help='Print raw list of domains')
    parser_c.add_argument('--json', '-j', action='store_true',
            help='Print raw json result')
    parser_c.set_defaults(which='adsense')
    parser_d = subparsers.add_parser('analytics', help='Query a Google Analytics id')
    parser_d.add_argument('ID', help='id to be requested')
    parser_d.add_argument('--raw', '-r', action='store_true',
            help='Print raw list of domains')
    parser_d.add_argument('--json', '-j', action='store_true',
            help='Print raw json')
    parser_d.set_defaults(which='analytics')
    parser_e = subparsers.add_parser('ip', help='Query an IP Address')
    parser_e.add_argument('IP', help='IP address to be requested')
    parser_e.add_argument('--raw', '-r', action='store_true',
            help='Print raw list of domains')
    parser_e.add_argument('--json', '-j', action='store_true',
            help='Print raw json')
    parser_e.set_defaults(which='ip')
    parser_f = subparsers.add_parser('nsdomain', help='Query an Name Server domain')
    parser_f.add_argument('DOMAIN', help='Name Server Domain to be requested')
    parser_f.add_argument('--raw', '-r', action='store_true',
            help='Print raw list of domains')
    parser_f.set_defaults(which='nsdomain')
    parser_g = subparsers.add_parser('nsip', help='Query a Name Server IP address')
    parser_g.add_argument('IP', help='Name Server IP Address to be requested')
    parser_g.add_argument('--raw', '-r', action='store_true',
            help='Print raw list of domains')
    parser_g.set_defaults(which='nsip')
    args = parser.parse_args()

    configfile = os.path.expanduser('~/.config/spyonweb')

    if hasattr(args, 'which'):
        if args.which == 'config':
            if args.token:
                config = configparser.ConfigParser()
                config['SpyOnWeb'] = {'token': args.token }
                with open(configfile, 'w') as cf:
                    config.write(cf)
            if os.path.isfile(configfile):
                print('In %s:' % configfile)
                with open(configfile, 'r') as cf:
                    print(cf.read())
            else:
                print('No configuration file, please create one with config --token')
        else:
            if not os.path.isfile(configfile):
                print('No configuration file, please create one with config --token')
                sys.exit(1)
            config = configparser.ConfigParser()
            config.read(configfile)
            s = SpyOnWeb(config['SpyOnWeb']['token'])
            if args.which == 'domain':
                try:
                    res = s.summary(args.DOMAIN)
                except SpyOnWebNotFound:
                    print('Domain not found')
                except SpyOnWebInvalidToken:
                    print('Invalid configuration')
                except SpyOnWebError as e:
                    print('Weird error: %s' % e.message)
                else:
                    if args.json:
                        print(json.dumps(res, sort_keys=True, indent=4))
                    else:
                        print('--------------- %s -----------------' % args.DOMAIN)
                        print('IP:')
                        for i in res['ip']:
                            print('-%s: %i entries' % (i, res['ip'][i]))
                        if 'adsense' in res:
                            print('AdSense:')
                            for i in res['adsense']:
                                print('-%s: %i entries' % (i, res['adsense'][i]))
                        if 'analytics' in res:
                            print('Analytics:')
                            for i in res['analytics']:
                                print('-%s: %i entries' % (i, res['analytics'][i]))
                        if 'dns_servers' in res:
                            print('DNS Servers:')
                            for i in res['dns_servers']:
                                print('-%s: %i entries' % (i, res['dns_servers'][i]))
            elif args.which == 'adsense':
                try:
                    res = s.adsense(args.ID)
                except SpyOnWebNotFound:
                    print('Adsense id not found')
                except SpyOnWebInvalidToken:
                    print('Invalid configuration')
                except SpyOnWebError as e:
                    print('Weird error: %s' % e.message)
                else:
                    if args.raw:
                        for i in res['items']:
                            print(i)
                    elif args.json:
                        print(json.dumps(res, sort_keys=True, indent=4))
                    else:
                        print('--------------- %s -----------------' % args.ID)
                        print('Fetched %i domains over %i' % (res['fetched'], res['found']))
                        for i in res['items']:
                            print('-%s (%s)' % (i, res['items'][i]))
            elif args.which == 'analytics':
                try:
                    res = s.analytics(args.ID)
                except SpyOnWebNotFound:
                    print('Analytic id not found')
                except SpyOnWebInvalidToken:
                    print('Invalid configuration')
                except SpyOnWebError as e:
                    print('Weird error: %s' % e.message)
                else:
                    if args.raw:
                        for i in res['items']:
                            print(i)
                    elif args.json:
                        print(json.dumps(res, sort_keys=True, indent=4))
                    else:
                        print('--------------- %s -----------------' % args.ID)
                        print('Fetched %i domains over %i' % (res['fetched'], res['found']))
                        for i in res['items']:
                            print('-%s (%s)' % (i, res['items'][i]))
            elif args.which == 'ip':
                try:
                    res = s.ip(args.IP)
                except SpyOnWebNotFound:
                    print('IP address not found')
                except SpyOnWebInvalidToken:
                    print('Invalid configuration')
                except SpyOnWebError as e:
                    print('Weird error: %s' % e.message)
                else:
                    if args.raw:
                        for i in res['items']:
                            print(i)
                    elif args.json:
                        print(json.dumps(res, sort_keys=True, indent=4))
                    else:
                        print('--------------- %s -----------------' % args.IP)
                        print('Fetched %i domains over %i' % (res['fetched'], res['found']))
                        for i in res['items']:
                            print('-%s (%s)' % (i, res['items'][i]))
            elif args.which == 'nsdomain':
                try:
                    res = s.nameserver_domain(args.DOMAIN)
                except SpyOnWebNotFound:
                    print('Name Server domain not found')
                except SpyOnWebInvalidToken:
                    print('Invalid configuration')
                except SpyOnWebError as e:
                    print('Weird error: %s' % e.message)
                else:
                    if args.raw:
                        for i in res['items']:
                            print(i)
                    else:
                        print('--------------- %s -----------------' % args.DOMAIN)
                        print('Fetched %i domains over %i' % (res['fetched'], res['found']))
                        for i in res['items']:
                            print('-%s (%s)' % (i, res['items'][i]))
            elif args.which == 'nsip':
                try:
                    res = s.nameserver_ip(args.IP)
                except SpyOnWebNotFound:
                    print('Name Server IP not found')
                except SpyOnWebInvalidToken:
                    print('Invalid configuration')
                except SpyOnWebError as e:
                    print('Weird error: %s' % e.message)
                else:
                    if args.raw:
                        for i in res['items']:
                            print(i)
                    else:
                        print('--------------- %s -----------------' % args.IP)
                        print('Fetched %i domains over %i' % (res['fetched'], res['found']))
                        for i in res['items']:
                            print('-%s (%s)' % (i, res['items'][i]))
            else:
                parser.print_help()
    else:
        parser.print_help()



