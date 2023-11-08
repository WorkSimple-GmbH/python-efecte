import typing
from datetime import datetime
from enum import Enum
from typing import List
from dateutil import parser

# Local Module imports
from .base import EfecteBaseModel
from .company import EfecteCompany


class EfectePersonPersonVipEnum(Enum):
    person_is_vip = 'Yes'


class EfectePersonEmployeeNatureEnum(Enum):
    employment_nature_hourly = 'Hour-based'
    employment_nature_other = 'Other'
    employment_nature_permanent = 'Permanent'
    employment_nature_temporary = 'Temporary'


class EfectePersonEmployeeTypeEnum(Enum):
    Employee = 'Employee'
    employment_type_external = 'External'
    External_Admin_user = 'External Admin user'
    External_Consultant = 'External Consultant'
    External_Project_Manager = 'External Project Manager'
    employment_type_guest = 'Guest'
    employment_type_internal = 'Internal'
    employment_type_other = 'Other'
    employment_type_trainee = 'Trainee'


class EfectePersonStatusEnum(Enum):
    Active = 'Active'
    Anonymised = 'Anonymised'
    Deleted = 'Deleted'
    Disabled = 'Disabled'
    disabled_password_doesnt_expire = "Disabled, password doesn't expire"
    enabled_password_doesnt_expire = "Enabled, password doesn't expire"
    Manually_locked = 'Manually locked'


class EfectePersonEmailNotificationEnum(Enum):
    No = 'No'


class EfectePerson(EfecteBaseModel):

    template_code: str = "person"
    "Static template code value"

    first_name: str = None
    "First name"

    given_name: str = None
    "Spoken / Preferred Name"

    middle_name: str = None
    "Middle name"

    last_name: str = None
    "Last name"

    initials: str = None
    "Initials"

    full_name: str = None
    "Full name"

    display_name: str = None
    "Display name"

    person_vip: EfectePersonPersonVipEnum = None
    "Person is VIP"

    title: str = None
    "Title"

    date_of_birth: datetime = None
    "Date of birth"

    mobile: str = None
    "Mobile"

    home_phone: str = None
    "Home phone"

    phone: str = None
    "Phone"

    fax: int = None
    "Fax"

    email: str = None
    "E-Mail"

    social_security_number: str = None
    "Social security number"

    ess_info: str = None
    "ESS info"

    employee_nature: EfectePersonEmployeeNatureEnum = None
    "Employment nature"

    employee_type: EfectePersonEmployeeTypeEnum = None
    "Employment type"

    employee_number: str = None
    "Employee number"

    ess_external: str = None
    "ESS external"

    cost_center_string: str = None
    "Provisioning engine Cost center"

    company_string: str = None
    "Provisioning engine Organization"

    company: EfecteCompany = None
    "Organization"

    department: str = None
    "Department"

    office: str = None
    "Office"

    status: EfectePersonStatusEnum = None
    "Identity repository status"

    description: str = None
    "Description"

    home_directory: str = None
    "Home directory"

    home_drive: str = None
    "Home drive"

    login_script_path: str = None
    "Login script path"

    samaccountname: str = None
    "SAM-Account-Name"

    active_directory_account: str = None
    "Active Directory account"

    last_password_reset: datetime = None
    "Last password reset"

    active_directory_creation_time: datetime = None
    "Active Directory creation time"

    active_directory_modify_time: datetime = None
    "Active Directory modify time"

    account_expires: datetime = None
    "Account expires"

    customer_name: str = None
    "Customer name"

    department_number: str = None
    "Department number"

    dn: str = None
    "Distinguished name (DN)"

    upn: str = None
    "UPN"

    ext_id_type_name: str = None
    "ext_id_type_name"

    int_id_type_name: str = None
    "int_id_type_name"

    internal_id: str = None
    "Internal id"

    repr_name: str = None
    "repr_name"

    room_number: str = None
    "Room number"

    service_provider_name: str = None
    "Service provider name"

    city: str = None
    "City"

    cn: str = None
    "Common name (CN)"

    country: str = None
    "Country"

    location: str = None
    "Location"

    street_address: str = None
    "Street address"

    zip_code: str = None
    "Zip code"

    agent_id: str = None
    "Agent ID"

    account_id: str = None
    "Account ID"

    external_id: str = None
    "External ID"

    object_guid: str = None
    "objectGUID"

    active_directory_id: str = None
    "Active directory Id"

    last_logon_stamp_ad: str = None
    "Last Logon Stamp AD"

    odoo_id: int = None
    "Odoo Id"

    data_source_id: str = None
    "Data SourceID"

    azuredatasourceid: str = None
    "Azure-DatasourceID"

    azureid: str = None
    "AzureID"

    groups_ess: List[str] = None
    "ESS Groups"

    ess_deputies_with_delegation_period: List[str] = None
    "ESS deputies with delegation period"

    emai_notification: EfectePersonEmailNotificationEnum = None
    "Email notifications"

    efecte_user: object = None
    "Efecte user"

    person_site_ess: str = None
    "Self-service site"

    additional_information: str = None
    "Additional information"

    efecte_id: str = None
    "Efecte ID"

