# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'

    appraisal_id = fields.Many2one('hr.appraisal', string="Appriasal id")

    @api.model
    def create(self, vals):
        ctx = self.env.context
        if ctx.get('active_id') and ctx.get('active_model') == 'hr.appraisal':
            vals['appraisal_id'] = ctx.get('active_id')
        return super(SurveyUserInput, self).create(vals)