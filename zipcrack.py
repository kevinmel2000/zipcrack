#!/usr/bin/env python
import optparse, zipfile
from threading import Thread
import sys, time
B = '\x1b[34m'
Y = '\x1b[33m'
G = '\x1b[32m'
W = '\x1b[0m'
R = '\x1b[31m'
date = time.asctime()

def banner():
    print G + ' ____  _      _____             __   ' + W + '|' + R + '    zip cracker'
    print G + '/_  / (_)__  / ___/______ _____/ /__ ' + W + '|'
    print G + " / /_/ / _ \\/ /__/ __/ _ `/ __/  '_/ " + W + '|' + B + ' [=] ' + W + 'author : Ci Ku'
    print G + '/___/_/ .__/\\___/_/  \\_,_/\\__/_/\\_\\  ' + W + '|' + B + ' [=] ' + W + 'I LOVE YOU ' + R + ':*'
    print G + '     /_/  ' + W + date + '\n'


def extract_zip(zfile, password):
    try:
        zfile.extractall(pwd=password)
        print B + '[=] ' + G + ' password found : ' + Y + password + '\n'
    except:
        pass


def main():
    parser = optparse.OptionParser(B + '[+]' + Y + ' Usage :' + G + ' python2 ' + sys.argv[0] + ' -f ' + B + '<' + G + 'file' + B + '> ' + G + '-d ' + B + '<' + G + 'wordlist' + B + '>')
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', help=' specify dictionary file')
    options, arg = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        banner()
        print parser.usage
        print B + '   [-]' + W + ' python2 ' + sys.argv[0] + ' -f file.zip -d list.txt\n'
        exit()
    else:
        zname = options.zname
        dname = options.dname
    banner()
    zfile = zipfile.ZipFile(zname)
    passfile = open(dname)
    for line in passfile.readlines():
        password = line.strip('\n')
        t = Thread(target=extract_zip, args=(zfile, password))
        t.start()

    return


if __name__ == '__main__':
    main()
