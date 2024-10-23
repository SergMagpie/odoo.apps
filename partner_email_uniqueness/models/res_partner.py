from odoo import models, api, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.constrains('email')
    def check_partner_email_uniqueness(self):
        """actually the method that checks it all"""
        for rec in self:
            result = self.env['res.partner'].search([
                ('email', '=', rec.email),
                ('id', '!=', rec.id),
            ])
            if result:
                raise ValidationError(_('Contact email is not unique!'))
