# Odoo Module For Slack

Odoo Module for Slack. You get a warning on a specific channel, every time a new lead is created.

## Why You Need It

Contact form in website will create a lead in the CRM. Problem is that most of the time 
you will not open the pipeline to see what is new because you might be busy with other stuff.

This module will send you a notification to Slack (Desktop/Mobile) so that you reply your 
leads in time.

## Dependencies

pip3 install -r requirements.txt

## Configuration

In Sales >> Settings find (Slack integration) or

ir.config_parameter

In Settings > Technical > Parameters > System Parameters

slack.sales_channel --> Channel where want to get the crm leads
slack.api_token --> the slack api token
