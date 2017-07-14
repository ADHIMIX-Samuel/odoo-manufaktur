# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Maintenance Management',
    'version' : '1.1',
    'summary': '',
    'sequence': '',
    'description': """
==================== 
    """,
    'category': 'Manufacturing',
    'website': 'https://www.adhimix.co.id',
    'author' :'PT.WITACO-Samuel-Haerul_RP',
    'email' : 'chaerulrifatpauji@gmail.com',
    ''
    'depends' : [
            'base',
            'mrp',
            'report',
            'product'
            ],
    'data': [
        'view/maintenance_view.xml',
        'menu.xml',
        
        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
