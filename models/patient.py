
from odoo import models, fields , api # decorators 
from odoo.exceptions import ValidationError 

class Patient(models.Model):
    _name = 'hos.patient'
    _description = 'Hospital Patient'
    _rec_name = 'first_name'
    

    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    birth_date = fields.Date(string='Birth Date')
    history = fields.Html(string='History')
    cr_ratio = fields.Float(string='CR Ratio')
    blood_type = fields.Selection([
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-')], string='Blood Type')
    patient_state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious')], string='Patient State', default='undetermined')
    pcr = fields.Boolean(string='PCR')
    image = fields.Binary(string='Image')
    address = fields.Text(string='Address')
    age = fields.Char(string='Age',compute='_compute_age',default=0)
    ref = fields.Char(string='Ref',default='New',copy=0)
    doc_ids = fields.Many2many(comodel_name='hos.doctor',string='doctors')
    department_id = fields.Many2one(comodel_name='hos.department',string='Department')
    pat_logs = fields.One2many(comodel_name='hos.loghistory',inverse_name='patient_id',string='Patient Logs')


    # set pcr true when age < 30 
    @api.onchange('age')
    def set_pcr_true(self):
        if int(self.age) < 30 :
            self.pcr = True
            return {'warning': {'title': "Warning", 'message': "PCR has been automatically checked due to age < 30.", 'type': 'notification'},}
    
    # make the CR Ratio is required when PCR is True
    @api.constrains('cr_ratio')
    def _check_pcr_true(self):
        if self.pcr and self.cr_ratio == 0.0:
            raise ValidationError('CR Ratio is required when PCR is True.')
    # compute age 
    @api.depends('birth_date')
        # you need to get today date - birthdate
    def _compute_age(self):
        today = fields.Date.today()
        for rec in self:
            rec.age = (today.year - rec.birth_date.year)

    def set_state_new(self):
        self.write({'state':'new'})
    
    def set_state_used(self):
        self.write({'state':'used'})

    def set_state_draft(self):
        self.write({'state':'draft'})
    
    @api.model
    def create(self,vals):
        res = super(Patient,self).create(vals)
        print('HHHHHHHHHHHHHHHH')
        res.ref = self.env["ir.sequence"].sudo().next_by_code("patient_ref_seq")
        return res
    
    @api.onchange('patient_state')
    def create_new_log(self):
        # new log history will be created
        print(self._origin.id)
        
        if self.patient_state and self._origin.id :
            new_log = self.env['hos.loghistory'].create({
                'patient_id':self._origin.id,
                'date': fields.Datetime.now(),
                'created_by': self.env.user.id,
                'description':f'State changed to {self.patient_state}'
            })
