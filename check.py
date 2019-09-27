import time
from fabric import Connection
from civo import Civo

hostname_default = 'gitops-civo.example.com'

civo = Civo()
size_id = civo.size.search(filter='name:g2.xsmall')[0]['name']
template = civo.templates.search(filter='code:debian-stretch')[0]['id']
search_hostname = civo.instances.search(filter='hostname:{}'.format(hostname_default))
ssh_id = civo.ssh.search(filter='name:alejandrojnm')[0]['id']

if not search_hostname:
    instance = civo.instances.create(hostname=hostname_default, size=size_id, region='lon1', template_id=template,
                                     public_ip='true', ssh_key_id=ssh_id)
    status = instance['status']

    while status != 'ACTIVE':
        status = civo.instances.search(filter='hostname:{}'.format(hostname_default))[0]['status']
        time.sleep(10)

ip_server = civo.instances.search(filter='hostname:{}'.format(hostname_default))[0]['public_ip']
username = 'civo'

c = Connection('{}@{}'.format(username, ip_server))
c.run('uname -s')
