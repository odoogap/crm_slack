# -*- coding: utf-8 -*-
{
    'name': 'Slack CRM integration',
    'version': '10.0',
    'author': 'OdooGAP',
    'summary': 'Slack CRM integration',
    'description': """
Slack CRM integration
=====================
Get Notification when you have a new lead

# Odoo Module For Slack

Odoo Module for Slack. You get a warning on a specific channel, every time a new lead is created.

## Configuration

In Sales >> Settings find (Slack integration) or

ir.config_parameter

In Settings > Technical > Parameters > System Parameters

slack.sales_channel --> Channel where want to get the crm leads
slack.api_token --> the slack api token

    """,
    'website': 'http://www.odoogap.com',
    'depends': ['crm'],
    'category': 'Communication',
    'data': [
        'data/slack_data.xml',
        'views/res_config_views.xml'
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
