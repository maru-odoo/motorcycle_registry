import re
from odoo import api, models, fields
from odoo.exceptions import ValidationError


class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _sql_constraints = [
        ('vin_unique', 'UNIQUE(vin)', 'Two registrations cannot have the same VIN.')
    ]

    registry_number = fields.Char(default="MRN0000", copy=False, required=True, readonly=True)
    vin = fields.Char(required=True)
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    picture = fields.Image()
    current_mileage = fields.Float()
    license_plate = fields.Char()
    certificate_title = fields.Binary()
    register_date = fields.Date()

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('registry_number', ('MRN0000')) == ('MRN0000'):
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('registry.number')
        return super().create(vals_list)

    @api.constrains('vin')
    def _check_vin(self):
        for session in self:
            vin = session.vin

            pattern = re.compile("^[A-Z]{4}\d{2}[A-Z\d]{2}\d{6}$")
            match = pattern.match(vin)
            if match is None:
                raise ValidationError('Invalid VIN.')

    @api.constrains('license_plate')
    def _check_license_plate(self):
        for session in self:
            plate = session.license_plate
            if not plate:
                return

            pattern = re.compile("^[A-Z]{1,4}\d{1,3}[A-Z]?[A-Z]?$")
            match = pattern.match(plate)
            if match is None:
                raise ValidationError('Invalid license plate.')
