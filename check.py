from civo import Civo

hostname_default = 'gitops-civo.example.com'

civo = Civo()
size_id = civo.size.search(filter='name:g2.xsmall')[0]['name']
template = civo.templates.search(filter='code:debian-stretch')[0]['id']
search_hostname = civo.instances.search(filter='hostname:{}'.format(hostname_default))
ssh_id = civo.ssh.search(filter='name:alejandrojnm')[0]['id']

if not search_hostname:
    civo.instances.create(hostname='text.example.com', size=size_id,
                          region='lon1', template_id=template,
                          public_ip='true', ssh_key_id=ssh_id)
    print(template)
