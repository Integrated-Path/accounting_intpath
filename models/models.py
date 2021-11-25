# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class ProductProduct(models.Model):
    _inherit="product.product"

    @api.model
    def create(self, vals):
        res =  super(ProductProduct, self).create(vals)

        channel = self.env['mail.channel'].search([('name', '=', 'accounting')])

        if not channel:
            channel = res.env['mail.channel'].create({
            'name': 'accounting',
            })
        
        res.message_post(
            body= 'the following product was created.',
            message_type='notification',
            subtype_id = self.env.ref('mail.mt_comment').id,
            channel_ids= [channel.id],
            partner_ids= [partner_id.id for partner_id in channel.channel_partner_ids]
        )
        return res
    


