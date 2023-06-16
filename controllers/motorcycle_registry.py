from odoo import http


class MotorcycleController(http.Controller):
    @http.route("/compare", auth="public")
    def compare(self, **kw):
        motorcycles = http.request.env['product.template'].search([('type', '=', 'motorcycle')])
        return http.request.render('motorcycle_registry.motorcycle_registry_template', {
            'motorcycles': motorcycles,
        })
