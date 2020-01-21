# -*- coding: utf-8 -*-


from odoo import api,fields,models,_


class HolidaysRequest(models.Model):
    _inherit = "hr.leave"

    leave_refuse_reason = fields.Text(string = "Refuse Reason")

    def reason_wizard(self,context=None):
        return {
                'name': ('Refuse Reason'),
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'leave.refuse.reason',
                'view_id': False,
                'type': 'ir.actions.act_window',
                'target':'new'
                }

	

	

	
