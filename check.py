from civo import Civo


civo = Civo()
template = civo.templates.lists(filter='code:debian-stretch')[0]['id']
print(template)
