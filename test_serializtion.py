from efecteClient import EfecteClient
from efecteClient.models.company import EfecteCompany
from efecteClient.models.person import EfectePerson
from private_credentials import *

client = EfecteClient.EfecteClient(URL)
echo1 = client.echo("blubb")
print(echo1)
client.login(USER, PASS)


orgs_data = client.get_datacards('company', limit=None, data_cards=True)
companies = list()
for org_data in orgs_data:
    company = EfecteCompany(org_data)
    companies.append(company)

for company in companies:
    print(company.get_efecte_json())

persons_data = client.get_datacards('person', limit=None, data_cards=True)
persons = list()
for person_data in persons_data:
    person = EfectePerson(person_data)
    persons.append(person)

for person in persons:
    print(person.get_efecte_json())


