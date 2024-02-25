from odoo import models, fields , api # decorators 

class Doctor(models.Model):
    _name = 'hos.doctor'
    _description = 'HOS Doctor Model'
    _rec_name = 'first_name'

    first_name = fields.Char(string='First Name',required=True)
    last_name = fields.Char(string='Last Name', required=True)
    image = fields.Image(string='Image')
    pat_ids = fields.Many2many(comodel_name='hos.patient',string='Patients')

