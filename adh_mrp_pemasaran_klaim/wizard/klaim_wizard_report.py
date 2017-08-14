from odoo import fields,api,models,_

class klaim_wizard(models.TransientModel):

    _name = "klaim.wizard"
    _description = "Komplain/Klaim Wizard"

 

    @api.multi
    def klaim_report(self):
        return self.env['report'].get_action( self, 'adh_mrp_pemasaran_klaim.report_klaim_pelanggan')