# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
import datetime


class hcm_pro(models.Model):
    _name = 'hcm_pro.hcm_pro'


class end_services_benfits(models.Model):
    _name = 'hr.payslip'
    _inherit = 'hr.payslip',
    _description = 'End of service'

    employee_id = fields.Many2one('hr.employee', string="Employee",)
    from_date = fields.Datetime(srting="From Date", required=False)
    to_date = fields.Datetime(srting="To Date", required=False)
    work_years = fields.Integer(String='Work Years', readonly=True, compute='_compute_working')

    def _compute_working(self):
        from_date = False
        if self.from_date:
            from_date = datetime.datetime.date(self.from_date)
            dToday = datetime.datetime.now().date()
            self.work_years = dToday.year - from_date.year
        return self.work_years

