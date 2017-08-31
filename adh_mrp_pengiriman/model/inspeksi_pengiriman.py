from odoo import api,fields,models,_

class report_inspeksi_pengiriman(models.AbstractModel):

    _name = 'report.adh_mrp_pemasaran.report_inspeksi_pengiriman'



    @api.model
    def get_inspeksi_pengiriman_details(self, tanggal_efektif=False):
        inspeksi_pengiriman_ids = self.env['adhimix.mrp.pengiriman'].search([
        	('tanggal_efektif','<=',tanggal_efektif)
        	])

        for inspeksi_pengiriman in inspeksi_pengiriman_ids:
        	nomor_inspeksi = inspeksi_pengiriman.name


        return {
        	'nomor_inspeksi' : nomor_inspeksi


        }

    @api.multi
    def render_html(self, docids, data=None):
        data = dict(data or {})        
        data.update(self.get_inspeksi_pengiriman_details(data['tanggal_efektif']))
        return self.env['report'].render('adh_mrp_pemasaran.report_inspeksi_pengiriman', data)