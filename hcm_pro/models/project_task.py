# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class ProjectTask(models.Model):
    _inherit = "project.task"
 
    stage_instructions = fields.Text(string="Stage Instructions",readonly=True,help='This field shows the instuctions, when click on the status button.')

    #This function will get satge_id and its instruction.
    def write(self, vals):
        for record in self:
            if vals.get('stage_id',False):
                temp = vals['stage_id']
                temp = self.env['project.task.type'].browse(temp).stage_instructions
                vals['stage_instructions']=temp
            return super(ProjectTask, self).write(vals)
        
