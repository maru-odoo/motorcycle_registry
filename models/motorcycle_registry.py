import re
from odoo import api, models, fields
from odoo.exceptions import ValidationError


class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Represents a registered motorcycle'
    _sql_constraints = [
        ('vin_unique', 'UNIQUE(vin)', 'Two registrations cannot have the same VIN.')
    ]

    registry_number = fields.Char(default="MRN0000", copy=False, required=True, readonly=True)
    vin = fields.Char(required=True)
    make = fields.Char(compute="_compute_make")
    model = fields.Char(compute="_compute_model")
    year = fields.Char(compute="_compute_year")
    owner_id = fields.Many2one(comodel_name="res.partner", string="Owner")
    phone = fields.Char(related="owner_id.phone")
    email = fields.Char(related="owner_id.email")
    picture = fields.Image()
    current_mileage = fields.Float()
    license_plate = fields.Char()
    certificate_title = fields.Binary()
    register_date = fields.Date()

    @api.depends("vin")
    def _compute_make(self):
        for record in self:
            record.make = record.vin[0:2]

    @api.depends("vin")
    def _compute_model(self):
        for record in self:
            record.model = record.vin[2:4]

    @api.depends("vin")
    def _compute_year(self):
        for record in self:
            record.year = record.vin[4:6]

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
