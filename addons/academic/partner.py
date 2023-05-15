from odoo import api, fields, models

class Partner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner" # ini wajib klo mau edit table bawaaan odoo
    
    is_instructor = fields.Boolean("Is Instructor", default=True)