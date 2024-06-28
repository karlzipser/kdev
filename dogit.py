#!/usr/bin/env python3
## 79 ########################################################################
from utilz2 import *
args=dict(
    task='',
    repos=[
        'projutils',
        'kdev',
        'tac',
        'tac_attn',
        'tac_ideal',
        'kmodule',
        'kllm',
        'utilz2.2.102',
    ],
)
p=getparser(**args)
gacp="git add .;git commit -m 'gacp';git push origin "
for f in p.repos:
    if p.task=='pull':
        os_system('cd; cd',f,'; pwd; git pull',e=1,a=1)
    elif p.task=='gacp':
        os_system('cd; cd',f,'; pwd;',gacp,e=1,a=1)
    else:
        assert False



## 79 ########################################################################
#EOF
