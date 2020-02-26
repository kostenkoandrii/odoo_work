# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Dashboards',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Build your own dashboards',
    'description': """
Lets the user create a custom dashboard.
===============================================

In Odoo, analytic accounts are linked to general accounts but are treated
totally independently. So, you can enter various different analytic operations
that have no counterpart in the general financial accounts.
    """,
    'data': [

        'views/board.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
}
