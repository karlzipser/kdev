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
    n=3,
)
p=getparser(**args)
gacp="git add .;git commit -m 'gacp';git push origin "
for f in p.repos:
    if p.task=='pull':
        os_system('cd; cd',f,'; pwd; git pull',e=1,a=1)
    elif p.task=='gacp':
        os_system('cd; cd',f,'; pwd;',gacp,e=1,a=1)
    elif p.task=='stable':
        os_system("""
         cd;cd F;
         git checkout -b stableN;
         git add .;
         git commit -m 'stableN';
         git push -u origin stableN;
         git checkout master;
         git branch;
         cd;
        """.replace('F',f).replace('N',str(p.n)),a=1,e=1)
    else:
        assert False



## 79 ########################################################################
#EOF
