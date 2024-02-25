from odoo import models, fields, api

class Department(models.Model):
    _name = 'hos.department'
    _description = 'Hospital Department'

    name = fields.Char(string='Name', required=True)
    capacity = fields.Integer(string='Capacity')
    is_opened = fields.Boolean(string='Is Opened', default=True)
    pat_ids = fields.One2many(comodel_name='hos.patient',inverse_name='department_id',string='Patients')

    # You can add additional fields and methods as needed
