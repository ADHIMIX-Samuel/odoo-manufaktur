from odoo import fields,api,models,_
# from odoo.exceptions import UserError

class pengiriman_wizard(models.TransientModel):

    _name = "pengiriman.wizard"
    _description = "Inspeksi Pengiriman"

 

    @api.multi
    def klaim_report(self):
    	# klaim_report = self.env['adhimix.mrp.klaim'].search([('','=',production.id), ('reference','=',production.line_produksi.id)])
        return self.env['report'].get_action( self, 'adh_mrp_pengiriman.report_inspeksi_pengiriman')
        # raise UserError(_('Error wa'))