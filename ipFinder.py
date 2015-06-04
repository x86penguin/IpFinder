#/usr/bin/env python

import socket, itertools, sys, argparse, smtplib

print '''================================================
 ___       _____ _           _
|_ _|_ __ |  ___(_)_ __   __| | ___ _ __
 | || '_ \| |_  | | '_ \ / _` |/ _ \ '__|
 | || |_) |  _| | | | | | (_| |  __/ |
|___| .__/|_|   |_|_| |_|\__,_|\___|_|
    |_|

    @x86p3nguin
================================================'''

ipList = []
subdomains = []
itcnt = 0
parser = argparse.ArgumentParser()
parser.add_argument('-sM',
    action='store_true',
    help='Do not record the same IP address in the log.')
parser.add_argument('domain',
    help='The domain to find IP addresses of.')
parser.add_argument('-cS',
    nargs=1,
    default='1',
    help='The number of the character set to try.\n'+
         '    [1]-abcdefghijklmnopqrstuvwxyz   --\n'+
         '    [2]-abcdefghijklmnopqrstuvwxyz.    \n'+
         '    [3]-abcdefghijklmnopqrstuvwxyz0123456789\n'+
         '    [4]-abcdefghijklmnopqrstuvwxyz0123456789.\n'+
         '    [5]-aabcdeefghhiijklmnnoopqrssttuvwxyz00112233445566778899.\n'+
         '    [6]-aabcdeefghhiijklmnnoopqrssttuvwxyz')
args = parser.parse_args()
args.cS = int(args.cS[0])-1
if args.domain.startswith('.') == False:
    args.domain = '.'+args.domain
charset = ['abcdefghijklmnopqrstuvwxyz',
           'abcdefghijklmnopqrstuvwxyz.',
           'abcdefghijklmnopqrstuvwxyz0123456789',
           'abcdefghijklmnopqrstuvwxyz0123456789.',
           'aabcdeefghhiijklmnnoopqrssttuvwxyz00112233445566778899.',
           'aabcdeefghhiijklmnnoopqrssttuvwxyz']
print '['+ str(args.cS+1) +']', charset[args.cS]
for length in range(60):
    for i in itertools.permutations(charset[args.cS],length):
        i = ''.join(i)
        if i in subdomains:
            continue
        subdomains.append(i)
        if itcnt % 1000 == 0:
            print i+args.domain, itcnt
        try:
            ip = socket.gethostbyname(i+args.domain)
            print 'The IP address of '+i+args.domain+' is: '+ ip
            if ip not in ipList:
                if args.sM:
                    ipList.append(ip)
                with open('ip.log', 'a+') as logFile:
                    logFile.write(ip+'  '+i+args.domain+'\n')
        except:
            pass
        itcnt += 1
