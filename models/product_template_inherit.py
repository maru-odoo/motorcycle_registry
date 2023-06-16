from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    detailed_type = fields.Selection(selection_add=[
        ('motorcycle', 'Motorcycle')
    ], ondelete={'motorcycle': 'set service'})
    type = fields.Selection(selection_add=[
        ('motorcycle', 'Motorcycle')
    ], ondelete={'motorcycle': 'set service'})

    make = fields.Char()
    model = fields.Char()
    year = fields.Char()
    horsepower = fields.Float()
    top_speed = fields.Float()
    torque = fields.Float()
    battery_capacity = fields.Selection([
        ('xs', 'Extra Small'),
        ('s', 'Small'),
        ('m', 'Medium'),
        ('l', 'Large'),
        ('xl', 'Extra Large'),
    ])
    charge_time = fields.Float()
    range = fields.Float()
    curb_weight = fields.Float()
    launch_date = fields.Date()
