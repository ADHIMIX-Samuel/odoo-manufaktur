from odoo import api,fields,models,_
import time

class mrp_bom(models.Model):
	_inherit = 'mrp.bom'

	dibuat_oleh = fields.Many2one(comodel_name="res.users",string="Dibuat oleh",required=True,readonly=True,default=lambda self:self.env.user,)
	created_date = fields.Date(string="Created Date",default=lambda self:time.strftime("%Y-%m-%d"),required=True,readonly=True)