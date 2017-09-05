from odoo import api,fields,models,_

class report_klaim_pelanggan(models.AbstractModel):

    _name = 'report.adh_mrp_pemasaran_klaim.report_klaim_pelanggan'

    @api.model
    # def get_klaim_pelanggan_details(self, tanggal_penerimaan=False):
    def get_klaim_pelanggan_details(self, date_start =False,date_stop=False):
        if date_start:
            date_start = fields.Datetime.from_string(date_start)
        else:
            # start by default today 00:00:00
            date_start = today

        if date_stop:
            # set time to 23:59:59
            date_stop = fields.Datetime.from_string(date_stop)
        else:
            # stop by default today 23:59:59
            date_stop = today + timedelta(days=1, seconds=-1)

        # avoid a date_stop smaller than date_start
        date_stop = max(date_stop, date_start)

        date_start = fields.Datetime.to_string(date_start)
        date_stop = fields.Datetime.to_string(date_stop)

    	tanggal_ids = self.env['adhimix.mrp.klaim'].search([
        	# ('tanggal_penerimaan','<=',tanggal_penerimaan)
            ('tanggal_penerimaan','>=',date_start),
            ('tanggal_penerimaan','<=',date_stop)
        	])


    	for x in tanggal_ids :
    		no_klaim = x.name
                company_id = x.company_id.logo
                tanggal_efektif = x.tanggal_efektif
                nama_pelanggan = x.nama_pelanggan
                no_komplain = x.no_komplain
                tanggal_penerimaan = x.tanggal_penerimaan
                nama_pelapor = x.nama_pelapor
                jabatan = x.jabatan
                no_telp = x.no_telp
                uraian = x.uraian
                Komplain_klaim = x.Komplain_klaim
                jenis_komplain = x.jenis_komplain
                tanggal = x.tanggal
                analisa_atas_komplain = x.analisa_atas_komplain
                penyebab_yg_paling_mungkin = x.penyebab_yg_paling_mungkin
                upaya_tindakan = x.upaya_tindakan
                rencana_selesai = x.rencana_selesai
                petugas = x.petugas 
                selesai_tanggal = x.selesai_tanggal
                tanggal_pemberitahuan_penanganan = x.tanggal_pemberitahuan_penanganan
                status = x.status
                realisasi_hasil_komplain = x.realisasi_hasil_komplain
                bagian_yang_menangani = x.bagian_yang_menangani
                dinyatakan_selesai = x.dinyatakan_selesai
                komplain = x.komplain
                klaim = x.klaim


    	return {
            'tanggal_ids' : tanggal_ids,
    		'no_klaim' : no_klaim,
            'company_id': company_id,
            'tanggal_efektif' : tanggal_efektif
    	   }



    @api.multi
    def render_html(self, docids, data=None):
        data = dict(data or {})        
        # data.update(self.get_klaim_pelanggan_details(data['tanggal_penerimaan']))
        data.update(self.get_klaim_pelanggan_details(data['date_start'],data['date_stop']))
        return self.env['report'].render('adh_mrp_pemasaran_klaim.report_klaim_pelanggan', data)
