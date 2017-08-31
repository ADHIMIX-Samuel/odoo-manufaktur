from odoo import api,fields,models,_

class report_klaim_pelanggan(models.AbstractModel):

    _name = 'report.adh_mrp_pemasaran.report_klaim_pelanggan'

    @api.model
    def get_klaim_pelanggan_details(self, tanggal=False):

    	tanggal_ids = self.env['adhimix.mrp.info.klaim'].search([
        	('tanggal_penerimaan','<=',tanggal_penerimaan)
        	])


    	for tanggal in tanggal_ids :
    		no_klaim = tanggal.name



    	return {
    		'no_klaim' : no_klaim
    	}



    @api.multi
    def render_html(self, docids, data=None):
        data = dict(data or {})        
        data.update(self.get_klaim_pelanggan_details(data['tanggal']))
        return self.env['report'].render('adh_mrp_pemasaran_klaim.report_klaim_pelanggan', data)
