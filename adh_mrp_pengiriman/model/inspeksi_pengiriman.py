from odoo import api,fields,models,_

class report_inspeksi_pengiriman(models.AbstractModel):

    _name = 'report.adh_mrp_pengiriman.report_inspeksi_pengiriman'



    @api.model
    # def get_inspeksi_pengiriman_details(self, tanggal_efektif=False):
    def get_inspeksi_pengiriman_details(self, date_start =False,date_stop=False):

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


        inspeksi_pengiriman_ids = self.env['adhimix.mrp.pengiriman'].search([
        	# ('tanggal_efektif','<=',tanggal_efektif)
            ('tanggal_efektif','>=',date_start),
            ('tanggal_efektif','<=',date_stop)
        	])
        uraian_ids = self.env['adhimix.mrp.pengiriman.detail']
        for uraian_id in inspeksi_pengiriman_ids :
            uraian_ids += uraian_id.uraian_ids

        produk_silo_ids = self.env['adhimix.mrp.pengiriman.produk.silo']
        for produk_id in inspeksi_pengiriman_ids :
            produk_silo_ids += produk_id.produk_silo_ids

        aksesoris_silo_ids = self.env['adhimix.mrp.aksesoris.silo']
        for aksesoris_silo_id in inspeksi_pengiriman_ids :
            aksesoris_silo_ids += aksesoris_silo_id.aksesoris_silo_ids

        produk_cold_bin_ids = self.env['adhimix.mrp.pengiriman.produk.cold.bin']
        for produk_cold_bin_id in inspeksi_pengiriman_ids :
            produk_cold_bin_ids += produk_cold_bin_id.produk_cold_bin_ids

        produk_silo_mobile_ids = self.env['adhimix.mrp.produk.silo.mobile']
        for produk_silo_id in inspeksi_pengiriman_ids :
            produk_silo_mobile_ids += produk_silo_id.produk_silo_mobile_ids


        aksesoris_silo_mobile_ids = self.env['adhimix.mrp.aksesoris.silo.mobile']
        for aksesoris_silo_mobile_id in inspeksi_pengiriman_ids :
            aksesoris_silo_mobile_ids += aksesoris_silo_mobile_id.aksesoris_silo_mobile_ids

        aksesoris_drum_mixer_ids = self.env['adhimix.mrp.aksesoris.drum.mixer']
        for aksesoris_drum_mixer_id in inspeksi_pengiriman_ids :
            aksesoris_drum_mixer_ids += aksesoris_drum_mixer_id.aksesoris_drum_mixer_ids





        for x in inspeksi_pengiriman_ids:
            tanggal_efektif = x.tanggal_efektif
            company_id = x.company_id.logo
                    


        return {
            'tanggal_efektif' : tanggal_efektif,
            'company_id' : company_id,
            'uraian_ids': uraian_ids,
            'produk_silo_ids': produk_silo_ids,
            'aksesoris_silo_ids': aksesoris_silo_ids,
            'produk_cold_bin_ids':produk_cold_bin_ids,
            'produk_silo_mobile_ids': produk_silo_mobile_ids,
            'aksesoris_silo_mobile_ids': aksesoris_silo_mobile_ids,
            'aksesoris_drum_mixer_ids' : aksesoris_drum_mixer_ids
        }


    @api.multi
    def render_html(self, docids, data=None):
        data = dict(data or {})        
        # data.update(self.get_inspeksi_pengiriman_details(data['tanggal_efektif']))
        data.update(self.get_inspeksi_pengiriman_details(data['date_start'],data['date_stop']))
        return self.env['report'].render('adh_mrp_pengiriman.report_inspeksi_pengiriman', data)