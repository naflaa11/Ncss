# -*- coding: utf-8 -*-


from odoo import api,fields,models,_


class LeaveRefuseReason(models.TransientModel):
    _name = "leave.refuse.reason"

    leave_refuse_reason = fields.Char(string = "Refuse Reason", required = True)

    def refuse_reason(self):
        if self.env.context.get('active_model') == 'hr.leave':
            active_model_id = self.env.context.get('active_id')
            hr_obj = self.env['hr.leave'].search([('id','=',active_model_id)])
            if hr_obj:
                hr_obj.write({'leave_refuse_reason':self.leave_refuse_reason})
                hr_obj.action_refuse()
              
	
