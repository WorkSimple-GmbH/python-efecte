import typing
from datetime import datetime
from enum import Enum
from typing import List
from dateutil import parser

# Local Module imports
from .base import EfecteBaseModel


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

    def __init__(self, location: str, name: str = None):
        self.location = location
        if name is not None:
            self.name = name
        else:
            self.name = location


class EfecteCompany(EfecteBaseModel):

    template_code: str = "company"
    "Static template code value"

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

    country: object = None
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

