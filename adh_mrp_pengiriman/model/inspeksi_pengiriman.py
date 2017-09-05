from odoo import api,fields,models,_

class report_inspeksi_pengiriman(models.AbstractModel):

    _name = 'report.adh_mrp_pengiriman.report_inspeksi_pengiriman'



    @api.model
    def get_inspeksi_pengiriman_details(self, tanggal_efektif=False):
        inspeksi_pengiriman_ids = self.env['adhimix.mrp.pengiriman'].search([
        	('tanggal_efektif','<=',tanggal_efektif)
        	])

        for x in inspeksi_pengiriman_ids:
        	nomor_inspeksi = x.name
                tanggal_efektif = x.tanggal_efektif
                company_id = x.company_id.logo

                uraian_detail = x.produk_silo_ids.uraian_id.name
                hasil_1_detail = x.produk_silo_ids.hasil_1
                kriteria_detail = x.produk_silo_ids.kriteria_id.name
                hasil_2_detail = x.produk_silo_ids.hasil_2
                keterangan_detail = x.produk_silo_ids.keterangan

                uraian_silo = x.produk_cold_bin_ids.uraian_id.name
                hasil_1_silo = x.produk_cold_bin_ids.hasil_1
                kriteria_silo = x.produk_cold_bin_ids.kriteria_id.name
                hasil_2_silo = x.produk_cold_bin_ids.hasil_2
                toleransi_silo = x.produk_silo_ids.toleransi
                keterangan_silo = x.produk_cold_bin_ids.keterangan

                # for y in inspeksi_pengiriman_ids.produk_silo_ids.aksesoris_silo_id:
                uraian_aksesoris_silo = y.produk_silo_ids.aksesoris_silo_id.uraian_id.name
                toleransi_aksesoris_silo = y.produk_silo_ids.aksesoris_silo_id.toleransi
                hasil_1_aksesoris_silo = y.produk_silo_ids.aksesoris_silo_id.hasil_1
                hasil_2_aksesoris_silo = y.produk_silo_ids.aksesoris_silo_id.hasil_2
                keterangan_aksesoris_silo = y.produk_silo_ids.aksesoris_silo_id.keterangan
                    


        return {
        	'nomor_inspeksi' : nomor_inspeksi,
            'tanggal_efektif' : tanggal_efektif,
            'company_id' : company_id,
            'inspeksi_pengiriman_ids' : inspeksi_pengiriman_ids,
            'produk_silo_ids': produk_silo_ids,
            'produk_cold_bin_ids': produk_cold_bin_ids,

            'uraian_detail' : uraian_detail,
            'kriteria_detail' : kriteria_detail,
            'hasil_1_detail' : hasil_1_detail,
            'hasil_2_detail' : hasil_2_detail,
            'keterangan_detail' :keterangan_detail,
            
            'uraian_silo' : uraian_silo,
            'hasil_1_silo' : hasil_1_silo,
            'kriteria_silo' : kriteria_silo,
            'hasil_2_silo' : hasil_2_silo,
            'keterangan_silo' : keterangan_silo,
        }

        # uraian_detail_ids = self.env['adhimix.mrp.pengiriman.detail'].search([
        #     ])

        # for y in inspeksi_pengiriman_ids.uraian_ids:
        #     uraian_detail = y.uraian_id.name
        #     hasil_1_detail = y.hasil_1
        #     kriteria_detail = y.kriteria_id
        #     hasil_2_detail = y.hasil_2
        #     keterangan_detail = y.keterangan

        # return {
        #         'uraian_detail' : uraian_detail,
        #         'kriteria_detail' : kriteria_detail,
        #         'hasil_1_detail' : hasil_1_detail,
        #         'hasil_2_detail' : hasil_2_detail,
        #         'keterangan_detail' :keterangan_detail
        # }

    @api.multi
    def render_html(self, docids, data=None):
        data = dict(data or {})        
        data.update(self.get_inspeksi_pengiriman_details(data['tanggal_efektif']))
        return self.env['report'].render('adh_mrp_pengiriman.report_inspeksi_pengiriman', data)