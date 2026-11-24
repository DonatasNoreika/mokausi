{
    'name': 'Mokausi – mokymosi svetainė',
    'summary': 'Interaktyvi mokymosi svetainė su versijų įkėlimu ir progreso saugojimu',
    'description': """
Rodo mokymosi svetainę adresu /mokausi (ir be Odoo apipavidalinimo – /mokausi/app).
Naujas svetainės versijas (vienas HTML failas) galima įkelti per meniu Mokausi → Svetainės versijos.
Prisijungusių naudotojų progresas saugomas Odoo duomenų bazėje.
""",
    'version': '18.0.1.0.0',
    'category': 'Website',
    'author': 'Mokausi',
    'license': 'LGPL-3',
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'views/mokausi_views.xml',
        'views/templates.xml',
        'data/initial_version.xml',
    ],
    'application': True,
    'installable': True,
}
