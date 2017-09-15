from odoo import api,fields,models,_

class report_evaluasi_penawaran(models.AbstractModel):

    _name = 'report.adh_mrp_evaluasi_penawaran.report_evaluasi_penawaran'

    @api.model
    # def get_evaluasi_penawaran_details(self, tanggal_penawaran=False):
    def get_evaluasi_penawaran_details(self, date_start =False,date_stop=False):
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

    	evaluasi_ids = self.env['adhimix.mrp.evaluasi.penawaran'].search([
        	# ('tanggal_penawaran','<=',tanggal_penawaran)
            ('tanggal_penawaran','>=',date_start),
            ('tanggal_penawaran','<=',date_stop)
        	])


    	for x in evaluasi_ids :
    		name = x.name
                no_penawaran = x.no_penawaran
                tanggal_penawaran = x.tanggal_penawaran
                nama_pelanggan = x.nama_pelanggan
                nama_spesifikasi_produk = x.nama_spesifikasi_produk
                kontak_person = x.kontak_person
                status = x.status
                penyebab_kekalahan = x.penyebab_kekalahan
                pic = x.pic
                company_id =x.company_id.logo
                tanggal_efektif = x.tanggal_efektif
                # period = x.period
               


    	return {
            'evaluasi_ids' : evaluasi_ids,
            'name' : name,
            'no_penawaran' :no_penawaran,
            'tanggal_penawaran':tanggal_penawaran,
            'nama_pelanggan' : nama_pelanggan,
            'nama_spesifikasi_produk' : nama_spesifikasi_produk,
            'kontak_person' : kontak_person,
            'status': status,
            'penyebab_kekalahan':penyebab_kekalahan,
            'pic' : pic,
            'company_id':company_id,
            'tanggal_efektif':tanggal_efektif,
            # 'period' : period

    	   }



    @api.multi
    def render_html(self, docids, data=None):
        data = dict(data or {})        
        # data.update(self.get_evaluasi_penawaran_details(data['tanggal_penawaran']))
        data.update(self.get_evaluasi_penawaran_details(data['date_start'],data['date_stop']))
        return self.env['report'].render('adh_mrp_evaluasi_penawaran.report_evaluasi_penawaran', data)
