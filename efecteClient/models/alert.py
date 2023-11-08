from datetime import datetime
from enum import Enum
from typing import List

from .base import EfecteBaseModel


class EfecteAlertStatusEnum(Enum):
    event_status_new = "1 - New"
    event_status_solving = "2 - Solving"
    event_status_closed = "3 - Closed"
    event_status_cancelled = "4 - Cancelled"


class EfecteAlertSourceEnum(Enum):
    event_source_application = "Application Capacity Monitor"
    event_source_erpusagemonitor = "ERP Usage Level"
    event_source_firewallmonitor = "Firewall Monitor"
    event_source_mailserver = "Mail Server Availability"
    event_source_networkmonitor = "Network Availablity Monitor"


class EfecteAlertTypeEnum(Enum):
    event_type_alert = "Alert"
    event_type_exception = "Exception"
    event_type_information = "Information"
    event_type_security = "Security event"
    event_type_warning = "Warning"


class EfecteAlert(EfecteBaseModel):

    event_primary_id: str
    "Event primary ID"

    subject: str
    "Subject"

    description: str
    "Description"

    file_attachments: List[object]
    "File attachments"

    email_from: str
    "Source"

    rule_name: str
    "Rule name"

    source_ip: str
    "Source IP"

    source_network: str
    "Source Network"

    source_username: str
    "Source Username (from event)"

    destination_ip: str
    "Destination IP"

    destination_port: str
    "Destination Port"

    destination_username: str
    "Destination Username (from Asset Identity)"

    destination_network: str
    "Destination Network"

    protocol: str
    "Protocol"

    qid: str
    "QID"

    event_name: str
    "Event Name"

    event_description: str
    "Event Description"

    category: str
    "Category"

    log_source_id: str
    "Log Source ID"

    log_source_name: str
    "Log Source Name"

    payload: str
    "Payload"

    related_incident: object
    "Related incident"

    alert_status: EfecteAlertStatusEnum
    "Alert status"

    alert_source: EfecteAlertSourceEnum
    "Alert source"

    alert_type: EfecteAlertTypeEnum
    "Alert type"

    alert_time: datetime
    "Alert time"

    additional_information: str
    "Additional information"

    efecte_id: str
    "Efecte ID"
