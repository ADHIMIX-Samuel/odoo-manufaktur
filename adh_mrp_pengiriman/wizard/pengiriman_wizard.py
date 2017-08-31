from odoo import fields,api,models,_
from odoo.exceptions import UserError

class pengiriman_wizard(models.TransientModel):

    _name = "pengiriman.wizard"
    _description = "Inspeksi Pengiriman"

    tanggal_efektif = fields.Date(string="Tanggal Efektif")

 

    @api.multi
    def inspeksi_report(self):
    	data = {'tanggal_efektif':self.tanggal_efektif}
        return self.env['report'].get_action(
            [], 'adh_mrp_pengiriman.report_inspeksi_pengiriman',data=data)
