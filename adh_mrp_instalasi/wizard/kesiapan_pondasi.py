from odoo import fields,api,models,_

class kesiapan_pondasi_wizard(models.Model):

    _name = "kesiapan.pondasi.wizard"
    _description = "Kesiapan Alat Dan Bahan"

 

    @api.multi
    def kesiapan_pondasi_report(self):
        return self.env['report'].get_action( self, 'adh_mrp_instalasi.report_kesiapan_pondasi')