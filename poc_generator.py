from efecteClient import EfecteClient
from private_credentials import *

efectetype = dict()
efectetype['number'] = 'int'
efectetype['string'] = 'str'
efectetype['date'] = 'datetime'
efectetype['reference'] = 'TypedDict'
efectetype['external-reference'] = 'object'
efectetype['static-value'] = 'object'
efectetype['worklog'] = 'object'

test = EfecteClient.EfecteClient(URL)
test.login(USER, PASS)
template = test.get_template("person")
for k,v in template['attributes'].items():
    if v['type'] == 'static-value':
        print("\tclass {0}Enum(enum):".format(k.title()))
        for item in v['values']:
            print("\t\t{} = auto()".format(item['code']))
    if v['type'] in ['file']:
        continue
    typ = efectetype[v['type']]
    if v['type'] == 'static-value':
        typ = "{0}Enum".format(k.title())
    if v['multiValue']:
        print("{0}: List[{1}]".format(k, typ))
    else:
        print("{0}: {1}".format(k, typ))
    print('"{0}"\r\n'.format(v['name']))
