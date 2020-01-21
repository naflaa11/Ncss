# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class ProjectTaskType(models.Model):
    _inherit = "project.task.type"
 
    stage_instructions = fields.Text(string="Stage Instructions",help="This field shows the instuctions, Which is define by user.")



