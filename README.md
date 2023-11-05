# Readme python-efecte

## Motivation and Background

We are currently implementing [Efecte&reg;](https://www.efecte.com/solutions/it-service-management) for our ITSM service processes.
It is necessary to integrate it into our existing data sources. 
Odoo is one of those data sources utilizing python as programming language.
The targeted integration should create or update Organization and Person datacards.
Please don't consider this a beautiful full-featured client SDK.

## References
This library uses the documented External REST api.
The OpenAPI specification can be found as reference in this repository:
[openapi.json](/docs/openapi.json)

## Targeted Features:
- Login to Efecte using the External API ✅
- Echo methods (authenticated, unauthenticated) are implemented ✅
- Load defined templates ✅
- Load specific template definition ✅
- Load datacards with or without query ✅
- Create a new datacard ✅
- Update an existing datacard ✅
- Delete datacard
- Use a well defined model

## Usage

```python
from efecteClient import EfecteClient

# Create new Efecte client object
# e.g. URL = "https://HOST/rest-api/itsm/v1"
client = EfecteClient.EfecteClient(URL)

# Login
client.login(USER, PASS)

# Test authenticated echo service
# Function returns the provided message
echo_return = client.echo_jwt("blubb")
```

You can find some usage examples within the examples.py file.

Please create your own private_settings.py before testing it. You can find an example in the folder.

## Disclaimer
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

Efecte is a registered Trademark of Efecte Oyj, 02600, Espoo, FI. 
This project is not affiliated with or endorsed by Efecte.
If there are any product related query please contact the vendor.
