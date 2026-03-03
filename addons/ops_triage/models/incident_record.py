from odoo import fields, models


class OpsIncident(models.Model):
    _name = "ops.incident"
    _inherit = ["mail.thread"]

    name = fields.Char(required=True, tracking=True)
    severity = fields.Selection([("sev1", "SEV1"), ("sev2", "SEV2"), ("sev3", "SEV3")], default="sev2")
    status = fields.Selection([("open", "Open"), ("mitigated", "Mitigated"), ("resolved", "Resolved")], default="open")
    impact_summary = fields.Text()
    root_cause = fields.Text()
    mitigation = fields.Text()
