import typing
from datetime import datetime
from enum import Enum
from typing import List

from .base import EfecteBaseModel
from .company import EfecteCompany
from .person import EfectePerson


class EfecteChangeStatusEnum(Enum):
    change_status_draft = "00 - Draft"
    change_status_rfc = "01 - RfC"
    change_status_assessment = "02 - Assessment"
    change_status_waitingforapproval = "03 - Waiting for provider approval"
    change_status_approved = "04 - Provider approved"
    change_status_waitingforcustomerapproval = "05 - Waiting for customer approval"
    change_status_customerapproved = "06 - Customer approved"
    change_status_waitingforscheduling = "07 - Waiting for scheduling"
    change_status_scheduling = "08 - Scheduling"
    change_status_waitingforimpl = "09 - Waiting for implementation"
    change_status_inimplementation = "10 - In implementation"
    change_status_waitingforreview = "11 - Waiting for review"
    change_status_reviewed_success = "12 - Reviewed - successful"
    change_status_reviewed_unsuccess = "13 - Reviewed - unsuccessful"
    change_status_closed = "14 - Closed"
    change_status_canceled = "15 - Canceled"
    change_status_rejected = "16 - Rejected"
    change_status_expired = "17 - Expired"


class EfecteChangeSizeEnum(Enum):
    major_change = "1. Major"
    medium_change = "2. Medium"
    minor_change = "3. Minor"


class EfecteChangeImpactEnum(Enum):
    change_impact_high = "1. High"
    change_impact_medium = "2. Medium"
    change_impact_low = "3. Low"


class EfecteChangeUrgencyEnum(Enum):
    change_urgency_high = "1. High"
    change_urgency_medium = "2. Medium"
    change_urgency_low = "3. Low"


class EfecteChangePriorityEnum(Enum):
    change_priority_high = "1. High"
    change_priority_medium = "2. Medium"
    change_priority_low = "3. Low"


class EfecteChangeEmergencyEnum(Enum):
    change_is_emergency = "Yes"


class EfecteChangeBusinessCriticalityEnum(Enum):
    change_business_criticality_affected_mostcritical = "1 - Most critical"
    change_business_criticality_affected_normal = "2 - Normal criticality"
    change_business_criticality_affected_somewhatcritical = "3 - Somewhat critical"


class EfecteChangeContactTypeEnum(Enum):
    schg_agent = "Agent"
    schg_email = "E-Mail"
    schg_houston = "Houston"
    schg_phone = "Phone"


class EfecteChangeApprovalEnum(Enum):
    change_implementation_approved = "Approved"
    change_implementation_rejected = "Rejected"


class EfecteChangeImplementationResultEnum(Enum):
    change_implementation_successful = "1 - Successful"
    change_implementation_success_errors = "2 - Successful - incomplete"
    change_implementation_fail_rollback = "3 - Failed - rolled back"


class EfecteChange(EfecteBaseModel):

    template_code: str = "change"
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
        data = json_data.get('data', {})
        company_data = data.get('company', {})
        values = company_data.get('values', [])
        if values and 'dataCardId' in values[0]:
            comp = EfecteCompany()
            comp.dataCardId = values[0]['dataCardId']
            self.company = comp

    # Identification
    name: str = None
    "Change primary ID"

    efecte_id: str = None
    "Efecte ID"

    datacard_link: str = None
    "Datacard link"

    ticket_link: str = None
    "Ticket link"

    # Core data
    subject: str = None
    "Subject"

    description: str = None
    "Description"

    justification: str = None
    "Justification"

    customer_reference: str = None
    "Customer reference"

    # Odoo integration
    odoo_sale_order_id: str = None
    "Odoo Sale Order Id"

    odoo_sale_order_link: str = None
    "Odoo Sale Order Link"

    odoo_sale_order_status: str = None
    "Odoo Sale Order Status"

    # Person references
    customer: EfectePerson = None
    "Customer"

    requester: EfectePerson = None
    "Requester"

    change_manager: EfectePerson = None
    "Change manager"

    assigned_to_person: EfectePerson = None
    "Assigned to person"

    cab_participants: List[object] = None
    "CAB participants"

    # Organization references
    company: EfecteCompany = None
    "Organization"

    assigned_to: EfecteBaseModel = None
    "Assigned to group"

    cost_center: EfecteBaseModel = None
    "Cost center"

    change_category: EfecteBaseModel = None
    "Category"

    change_service: EfecteBaseModel = None
    "Service"

    # Classification
    status: EfecteChangeStatusEnum = None
    "Status"

    change_type: EfecteChangeSizeEnum = None
    "Change size"

    impact: EfecteChangeImpactEnum = None
    "Impact"

    urgency: EfecteChangeUrgencyEnum = None
    "Urgency"

    priority: EfecteChangePriorityEnum = None
    "Priority"

    emergency: EfecteChangeEmergencyEnum = None
    "Emergency"

    business_criticality: EfecteChangeBusinessCriticalityEnum = None
    "Business criticality"

    contact_type: EfecteChangeContactTypeEnum = None
    "Contact type"

    # Status details
    reason_abandoning: str = None
    "Reason for abandoning"

    rejection_reason: str = None
    "Rejection reason"

    rejection_reason_log: str = None
    "Latest CAB rejection"

    # Planning
    work_estimate: int = None
    "Work estimate"

    cost_estimate: int = None
    "Cost estimate"

    followup_estimate: int = None
    "Follow-up cost estimate"

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

    target_assessment_time: datetime = None
    "Target assessment time"

    # Implementation
    implementation_plan: str = None
    "Implementation plan"

    test_plan: str = None
    "Test plan"

    rollback_plan: str = None
    "Rollback plan"

    chg_acceptance_criteria: str = None
    "Acceptance criteria"

    change_risks: str = None
    "Risks"

    approval_for_implementation: EfecteChangeApprovalEnum = None
    "Approval for implementation"

    implementation_approved: datetime = None
    "Implementation approved"

    implementation_start: datetime = None
    "Actual start"

    implementation_end: datetime = None
    "Actual end"

    duration: int = None
    "Actual duration"

    implementation_result: EfecteChangeImplementationResultEnum = None
    "Implementation result"

    implementation_review: str = None
    "Implementation review"

    implementation_costs: int = None
    "Implementation costs"

    # Timestamps
    change_closed: datetime = None
    "Change closed"

    approved_on: datetime = None
    "Approved/Rejected on"

    actual_implementation_start: datetime = None
    "Actual implementation start"

    actual_implementation_end: datetime = None
    "Actual implementation end"

    change_manager_changed: datetime = None
    "Manager changed"

    assigned_person_changed: datetime = None
    "Person changed"

    assigned_group_changed: datetime = None
    "Group changed"

    chg_customer_reviewed: datetime = None
    "Customer reviewed"

    # Related items
    related_changes: List[object] = None
    "Related changes"

    related_oa: List[object] = None
    "Related OAs"

    affected_related_incidents: List[object] = None
    "Related incidents"

    affected_related_problems: List[object] = None
    "Related problems"

    affected_cis: List[object] = None
    "Affected CIs"

    tasks: List[object] = None
    "Change Tasks"

    acceptance_criteria: List[object] = None
    "Acceptance criteria"

    # Workflow
    workflow_name: str = None
    "Workflow name"

    workflow_phase: str = None
    "Workflow phase"

    workflow_status: str = None
    "Workflow status"
