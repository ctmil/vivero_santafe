# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
'name': 'Vivero Santa Fe',
'version': '1.0',
'category': 'Tools',
'summary': 'Vivero Santa Fe',
'depends': ['web','sale','product','base'],
'data': [
    'security/ir.model.access.csv',
    'vivero_view.xml',
],
'demo': [
    #'data/demo.xml',
],
'css': [],
'installable': True,
'auto_install': False,
'application': True,
}
