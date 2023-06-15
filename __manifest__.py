{
    'name': 'Motorcycle Registry',
    'summary': 'Manage Registration of Motorcycles',
    'description': """Motorcycle Registry
    ====================
    This Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycled of the brand.""",
    'author': 'maru-odoo',
    'website': 'https://github.com/maru-odoo/motorcycle_registry',
    'category': 'Kawiil/Kawiil',
    'depends': ['base'],
    'data': [
        'security/motorcycle_registry_groups.xml',
        'security/ir.model.access.csv',
        'data/motorcycle_registry_number.xml',
        'views/motorcycle_registry_actions.xml',
        'views/motorcycle_registry_menuitems.xml',
        'views/motorcycle_registry_views.xml',
    ],
    'demo': [
        'demo/motorcycle_registry_demo.xml',
    ],
    'application': True,
}
