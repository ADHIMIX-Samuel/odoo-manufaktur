from odoo import fields,api,models,_
from odoo.exceptions import UserError

class pengiriman_wizard(models.TransientModel):

    _name = "pengiriman.wizard"
    _description = "Inspeksi Pengiriman"

 

    @api.multi
    def inspeksi_report(self):
    	# raise UserError(_('Maaf anda belum beruntung'))	
    	# print "aaaaaaaaaaaa"
    	return self.env['report'].get_action( self,'adh_mrp_pengiriman.report_inspeksi_pengiriman')
