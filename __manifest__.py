# -*- coding: utf-8 -*-
{
    'name': "HOS APP",
    'summary': """""",
    'description': """ """,
    'author': "Abdelrhman Gouda",
    'category': 'Productivity',
    'version': '16.0.1.0',
    'depends': ['base'],
    'application': True,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/base_menus.xml',
        'views/doctor_view.xml',
        'views/patient_view.xml',
        'views/departmen_view.xml',
        'views/log_history_views.xml',
    ],
}
