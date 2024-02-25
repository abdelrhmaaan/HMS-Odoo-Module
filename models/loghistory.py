from odoo import models, fields, api

class PatientLogHistory(models.Model):
    _name = 'hos.loghistory'
    _description = 'Patient Log History'

    created_by = fields.Many2one('res.users', string='Created By',default= lambda self : self.env.user, readonly=True)
    date = fields.Datetime(string='Date', default=fields.Datetime.now)
    description = fields.Text(string='Description')
    patient_id = fields.Many2one(comodel_name='hos.patient', string='Patient', required=True)
