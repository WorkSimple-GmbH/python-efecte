from efecteClient import EfecteClient
from private_credentials import *

client = EfecteClient.EfecteClient(URL)
echo1 = client.echo("blubb")
print(echo1)
client.login(USER, PASS)
echo2 = client.echo_jwt("blubb")
print(echo2)
templates = client.get_templates()
template = client.get_template("person")
print(templates)
test1 = client.get_datacards('person', limit=1, data_cards=True)
person1 = {
        'first_name': {
          'values': [{'value': 'Kurt'}]
        },
        'first_name': {
            'values': [{'value': 'Kleinlich'}]
        },
        'external_id': {
            'values': [{'value': '1332'}]
        },
        'status': {
            'values': [{'value': 'Deleted'}]
        }
    }
person2 = {
    'first_name': {
        'values': [{'value': 'Wurst'}]
    }
}

# Create new person
test3 = client.create_datacard('person','personnel', person1)
# Update created persons firstname
test3 = client.update_datacard('person','personnel', test3, person2)

print(test3)