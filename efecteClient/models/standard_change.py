import typing
from datetime import datetime
from enum import Enum
from typing import List

from .base import EfecteBaseModel
from .company import EfecteCompany
from .person import EfectePerson


class EfecteStandardChangeStatusEnum(Enum):
    standard_change_status_waitingforapproval = "01 - Waiting for approval"
    standard_change_status_waitingforassignement = "02 - Waiting for assignment"
    standard_change_status_waitingforscheduling = "03 - Waiting for scheduling"
    standard_change_status_waitingforimplementation = "04 - Waiting for implementation"
    standard_change_status_inimplementation = "05 - In implementation"
    standard_change_status_waitingforreview = "06 - Waiting for review"
    standard_change_status_inreview = "07 - In review"
    standard_change_status_completed = "08 - Closed - completed"
    standard_change_status_incomplete = "09 - Closed - incomplete"
    standard_change_status_approvalincomplete = "10 - Canceled - approval incomplete"
    standard_change_status_taskincomplete = "11 - Canceled - task incomplete"
    standard_change_status_canceledbycustomer = "12 - Canceled - by customer"


class EfecteStandardChangeContactTypeEnum(Enum):
    schg_agent = "Agent"
    schg_email = "E-Mail"
    schg_houston = "Houston"
    schg_phone = "Phone"


class EfecteStandardChangeImplementationResultEnum(Enum):
    schg_impl_successful = "1 - Successful"
    schg_impl_successful_incomplete = "2 - Successful - incomplete"
    schg_impl_fail_rollback = "3 - Failed - rolled back"


class EfecteStandardChange(EfecteBaseModel):

    template_code: str = "standard_change"
    "Static template code value"

    folderName: str = None
    "Storage Folder Name"

    def __init__(self, json_data=None):
        super().__init__(json_data)
        if json_data is None:
            return
        # EfecteBaseModel.__init__ does not parse reference fields into model
        # objects (it only handles 'value' keys, not 'dataCardId'). We handle
        # the company reference manually here.
        # Note: Standard Change uses 'schg_company' instead of 'company'.
        data = json_data.get('data', {})
        company_data = data.get('schg_company', {})
        values = company_data.get('values', [])
        if values and 'dataCardId' in values[0]:
            comp = EfecteCompany()
            comp.dataCardId = values[0]['dataCardId']
            self.schg_company = comp

    # Identification
    name: str = None
    "Primary S-Change ID"

    efecte_id: str = None
    "Efecte ID"

    ticket_link: str = None
    "Ticket link"

    # Core data
    subject: str = None
    "Subject"

    description: str = None
    "Description"

    subject_old: str = None
    "Subject_OLD"

    change_source_type: str = None
    "Change source type"

    # Odoo integration
    odoo_sale_order_id: str = None
    "Odoo Sale Order Id"

    odoo_sale_order_link: str = None
    "Odoo Sale Order Link"

    odoo_sale_order_status: str = None
    "Odoo Sale Order Status"

    # Person references
    requester: EfectePerson = None
    "Requester"

    change_manager: EfectePerson = None
    "Change manager"

    assigned_to: EfectePerson = None
    "Assigned to"

    # Organization references
    schg_company: EfecteCompany = None
    "Organization"

    category: EfecteBaseModel = None
    "Category"

    service: EfecteBaseModel = None
    "Service"

    change_source: EfecteBaseModel = None
    "Change source"

    standard_change_template: EfecteBaseModel = None
    "Content template"

    # Classification
    status: EfecteStandardChangeStatusEnum = None
    "Status"

    schg_contacttype: EfecteStandardChangeContactTypeEnum = None
    "Contact type"

    implementation_result: EfecteStandardChangeImplementationResultEnum = None
    "Implementation result"

    schg_reason_for_abandoning: str = None
    "Reason for abandoning"

    # Costs
    cost_estimate: int = None
    "Cost estimate"

    # Planning
    implementation_plan: str = None
    "Implementation plan"

    rollback_plan: str = None
    "Rollback plan"

    schg_affected_cis: str = None
    "Affected CIs"

    requested_time: datetime = None
    "Requested completion"

    wish_start: datetime = None
    "Wunschzeitraum von"

    wish_end: datetime = None
    "Wunschzeitraum bis"

    planned_start: datetime = None
    "Planned start"

    planned_end: datetime = None
    "Planned end"

    planned_duration: int = None
    "Planned duration"

    scheduling_implementation_approved_rejected: str = None
    "Implementation Approved / Rejected"

    # Implementation
    implementation_start: datetime = None
    "Implementation start"

    implementation_end: datetime = None
    "Implementation end"

    duration: int = None
    "Duration"

    change_review: str = None
    "Change review"

    # Timestamps
    change_closed: datetime = None
    "Change closed"

    # Related items
    select_task_Set: EfecteBaseModel = None
    "Select task set"

    change_tasks: List[object] = None
    "Change tasks"

    parent_issue_schg: EfecteBaseModel = None
    "Parent ISS Issue"

    child_iss_issues_schg: List[object] = None
    "Child ISS Issues"

    houston_notification: EfecteBaseModel = None
    "Houston notification"

    # Workflow
    workflow_name: str = None
    "Workflow name"

    workflow_phase: str = None
    "Workflow phase"

    workflow_status: str = None
    "Workflow status"
