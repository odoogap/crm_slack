# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleConfiguration(models.TransientModel):
    _inherit = 'res.config.settings'

    module_crm_slack = fields.Boolean("Slack integration", help="Integration with slack, so that you"
                                      "can be warned on slack everytime you get a new lead on the CRM app")
    slack_api_key = fields.Char(string='Slack API Key')
    slack_channel = fields.Char(string='Slack Channel')

    @api.model
    def set_values(self):
        self.env['ir.config_parameter'].set_param(
            'slack_api_key', (self.slack_api_key or '').strip(), groups=['base.group_system'])
        self.env['ir.config_parameter'].set_param(
            'sales_channel', (self.slack_channel or '').strip(), groups=['base.group_system'])

    @api.model
    def get_values(self):
        slack_api_key = self.env['ir.config_parameter'].get_param('slack.api_token', default='')
        slack_channel = self.env['ir.config_parameter'].get_param('slack.sales_channel', default='#general')
        return dict(slack_api_key=slack_api_key, slack_channel=slack_channel)
