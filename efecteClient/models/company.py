from datetime import datetime
from enum import Enum
from typing import List
from dateutil import parser

from efecteClient.models.country import EfecteCountry


class EfecteCompanyStatusEnum(Enum):
    organization_status_active = "Active"
    organization_status_inactive = "Inactive"
    New = "New"
    Removed = "Removed"


class EfecteCompanyTypeEnum(Enum):
    organization_type_parentcompany = "Parent company"
    organization_type_partner = "Partner"
    organization_type_serviceconsumer = "Service Consumer"
    organization_type_serviceprovider = "Service Provider"
    organization_type_subsidiary = "Subsidiary"


class EfecteOrganizationInternalExternalEnum(Enum):
    organization_external = "External"
    organization_internal = "Internal"


class EfecteWebsite:

    location: str = None
    "Website URL"

    name: str = None
    "Website Name"

    def __init__(self, location: str, name: str):
        self.location = location
        self.name = name


class EfecteCompany:
    folderName: str = None
    "Storage Folder Name"

    company_status: EfecteCompanyStatusEnum = None
    "Status"

    company_name: str = None
    "Name"

    company_description: str = None
    "Description"

    company_id: str = None
    "Organization ID"

    company_type: EfecteCompanyTypeEnum = None
    "Type"

    organization_internal_external: EfecteOrganizationInternalExternalEnum = None
    "Internal or external"

    email_extension: str = None
    "Email extension"

    organization_start_date: datetime = None
    "Organization Start Date"

    organization_end_date: datetime = None
    "Organization End Date"

    street_address: str = None
    "Street address"

    postal_code: str = None
    "Postal code"

    city: str = None
    "City"

    country: EfecteCountry = None
    "Country"

    phone: str = None
    "Phone"

    fax: str = None
    "Fax"

    websites: List[EfecteWebsite] = list()
    "Websites"

    odoo_id: int = None
    "Odoo Id"

    efecte_id: str = None
    "Efecte ID"

    created: datetime = None
    "Created"

    updated: datetime = None
    "Updated"

    creator: object = None
    "Creator"

    last_update_by: object = None
    "Last update by"

    dataCardId: str = None
    "Efecte DatacardId"

    deleted: bool = False
    "Is item deleted"

    hidden: bool = False
    "Item is hidden"

    def __init__(self, data):
        self.dataCardId = data['dataCardId']
        self.folderName = data['folderName']
        if 'data' in data:
            for key, element in data['data'].items():
                if hasattr(self, key):
                    attr_type = self.__annotations__[key]
                    element_type = element['type']
                    values = element['values']
                    if len(values) == 1:
                        if attr_type == str:
                            if element_type != 'string':
                                raise TypeError("Expected string and got {}".format(element_type))
                        if attr_type == datetime:
                            if element_type != 'date':
                                raise TypeError("Expected date and got {}".format(element_type))
                            setattr(self, key, parser.parse(values[0]['value']))
                        elif attr_type == EfecteCompanyStatusEnum:
                            if element_type != 'static-value':
                                raise TypeError("Expected static-value and got {}".format(element_type))
                            setattr(self, key, EfecteCompanyStatusEnum(values[0]['value']))
                        elif attr_type == EfecteCompanyTypeEnum:
                            if element_type != 'static-value':
                                raise TypeError("Expected static-value and got {}".format(element_type))
                            setattr(self, key, EfecteCompanyTypeEnum(values[0]['value']))
                        elif attr_type == EfecteOrganizationInternalExternalEnum:
                            if element_type != 'static-value':
                                raise TypeError("Expected static-value and got {}".format(element_type))
                            setattr(self, key, EfecteOrganizationInternalExternalEnum(values[0]['value']))
                        elif attr_type == [EfecteWebsite]:
                            setattr(self, key, EfecteWebsite(values[0]['location'], values[0]['name']))
                        else:
                            if 'value' in values[0]:
                                setattr(self, key, values[0]['value'])
                    else:
                        if type(getattr(self, key)).__name__ == 'list':
                            items = list()
                            for item in values:
                                if attr_type == [EfecteWebsite]:
                                    items.append(EfecteWebsite(item['location'], item['name']))
                                else:
                                    items.append(item['value'])
                            setattr(self, key, items)
