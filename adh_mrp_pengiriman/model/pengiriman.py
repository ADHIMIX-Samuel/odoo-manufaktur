from odoo import api,fields,models,_

class adh_mrp_pengiriman(models.Model):
	_name = "adhimix.mrp.pengiriman"

	name = fields.Char(string="Uraian")
	no_dokumen = fields.Char(string="No Dokumen")
	tanggal_efektif = fields.Date(string="Tanggal Efektif")
	company_id = fields.Many2one(comodel_name ="res.company",string="Company")
	uraian_ids = fields.One2many(comodel_name ="adhimix.mrp.pengiriman.detail.uraian",inverse_name ="reference",string="Uraian")
	# kriteria_ids = fields.One2many(comodel_name ="adhimix.mrp.pengiriman.detail.uraian",inverse_name ="kriteria_id")

	# inspeksi_pengiriman_produk_silo_ids = fields.One2many(comodel_name="adhimix.mrp.pengiriman.produk.silo",
	# 										inverse_name="reference",string="Insepeksi Pengiriman Produk Silo")
	# inspeksi_pengiriman_produk_cold_bin_ids = fields.One2many(comodel_name="adhimix.mrp.pengiriman.produk.cold.bin",
	# 										inverse_name="reference",string="Inspeksi Pengiriman Produk Cold Bin")
	# inspeksi_pengiriman_produk_silo_mobile_ids = fields.One2many(comodel_name="adhimix.mrp.pengiriman.produk.silo.mobile",
	# 										inverse_name="reference",string="Inspeksi Pengiriman Produk Silo Mobile")
	# inspeksi_pengiriman_aksesoris_drum_mixer_ids = fields.One2many(comodel_name="adhimix.mrp.pengiriman.aksesoris.drum.mixer",
	# 										inverse_name="reference",string="Inspeksi Pengiriman Aksesoris Drum Mixer")


class adh_mrp_pengiriman_detail_uraian(models.Model):
	_name ="adhimix.mrp.pengiriman.detail.uraian"

	reference = fields.Many2one(comodel_name = "adhimix.mrp.pengiriman",string="Uraian")
	hasil_1 = fields.Selection([('Bagus','Bagus'),('Kurang Bagus','Kurang Bagus')],string="Hasil Pemeriksaan 1")
	hasil_2 = fields.Selection([('Bagus','Bagus'),('Kurang Bagus','Kurang Bagus')],string="Hasil Pemeriksaan 2")
	keterangan = fields.Char(string="Keterangan")
	kriteria_id = fields.Many2one(comodel_name="adhimix.mrp.pengiriman",string="Kriteria")

class adh_mrp_pengiriman_detail_kriteria(models.Model):
	_name ="adhimix.mrp.pengiriman.detail.kriteria"
	_inherit ="adhimix.mrp.pengiriman"

	kriteria = fields.Char(string="Kriteria")

	


class adh_mrp_pengiriman_produk_silo(models.Model):
	_name = "adhimix.mrp.pengiriman.produk.silo"

	reference = fields.Many2one(comodel_name="adhimix.mrp.pengiriman",string="No Dokumen")
	tanggal_efektif = fields.Date(string="Tanggal Efektif")

	kriteria_tabung_silo = fields.Char(string="Kriteria")
	toleransi_tabung_silo = fields.Char(string="Toleransi Tabung Silo")
	hasil_pemeriksaan_tabung_silo_i = fields.Text(string="Hasil Pemeriksaan I")
	hasil_pemeriksaan_tabung_silo_ii = fields.Text(string="Hasil Pemeriksaan II")
	keterangan_tabung_silo = fields.Text(string="Keterangan")

	kriteria_bagian_dalam_silo = fields.Char(string="Kriteria")
	toleransi_bagian_dalam_silo = fields.Char(string="Toleransi Bagian Dalam Silo")
	hasil_pemeriksaan_bagian_dalam_silo_i = fields.Text(string="Hasil Pemeriksaan I")
	hasil_pemeriksaan_bagian_dalam_silo_ii = fields.Text(string="Hasil Pemeriksaan II")
	keterangan_bagian_dalam_silo = fields.Text(string="Keterangan")

	kriteria_kaki_silo = fields.Char(string="Kriteria")
	toleransi_kaki_silo = fields.Char(string="Toleransi")
	hasil_pemeriksaan_kaki_silo_i = fields.Text(string="Hasil Pemeriksaan I")
	hasil_pemeriksaan_kaki_silo_ii = fields.Text(string="Hasil Pemeriksaan II")
	keterangan_kaki_silo = fields.Text(string="Keterangan")

	kriteria_air_nozel = fields.Char(string="Kriteria")
	toleransi_air_nozel = fields.Char(string="Toleransi")
	hasil_pemeriksaan_air_nozel_i = fields.Text(string="Hasil Pemeriksaan I")
	hasil_pemeriksaan_air_nozel_ii = fields.Text(string="Hasil Pemeriksaan II")
	keterangan_air_nozel = fields.Text(string="Keterangan")

	kriteria_lubang_outer_semen = fields.Char(string="Kriteria")
	toleransi_lubang_outer_semen = fields.Char(string="Toleransi")
	hasil_pemeriksaan_lubang_outer_semen_i = fields.Text(string="Hasil Pemeriksaan I")
	hasil_pemeriksaan_lubang_outer_semen_ii = fields.Text(string="Hasil Pemeriksaan II")
	keterangan_lubang_outer_semen = fields.Text(string="Keterangan")

	kriteria_main_hole = fields.Char(string="Kriteria")
	toleransi_main_hole = fields.Char(string="Toleransi")
	hasil_pemeriksaan_main_hole_i = fields.Text(string="Hasil Pemeriksaan I")
	hasil_pemeriksaan_main_hole_ii = fields.Text(string="Hasil Pemeriksaan II")
	keterangan_main_hole = fields.Text(string="Keterangan")		

	kriteria_lubang_baut_main_hole = fields.Char(string="Kriteria")
	toleransi_lubang_baut_main_hole = fields.Char(string="Toleransi")
	hasil_pemeriksaan_lubang_baut_main_hole_i = fields.Text(string="Hasil Pemeriksaan I")
	hasil_pemeriksaan_lubang_baut_main_hole_ii = fields.Text(string="Hasil Pemeriksaan II")
	keterangan_lubang_baut_main_hole = fields.Text(string="Keterangan")


	kriteria_jumlah_mur_dan_baut = fields.Char(string="Kriteria")
	toleransi_jumlah_mur_dan_baut = fields.Char(string="Toleransi")
	hasil_pemeriksaan_jumlah_mur_dan_baut_i = fields.Text(string="Hasil Pemeriksaan I")
	hasil_pemeriksaan_jumlah_mur_dan_baut_ii = fields.Text(string="Hasil Pemeriksaan II")
	keterangan_jumlah_mur_dan_baut = fields.Text(string="Keterangan")

	kriteria_pipa_input_semen_silo = fields.Char(string="Kriteria")
	toleransi_pipa_input_semen_silo = fields.Char(string="Toleransi")
	hasil_pemeriksaan_pipa_input_semen_silo_i = fields.Text(string="Hasil Pemeriksaan I")
	hasil_pemeriksaan_pipa_input_semen_silo_ii = fields.Text(string="Hasil Pemeriksaan II")
	keterangan_pipa_input_semen_silo = fields.Text(string="Keterangan")

class adh_mrp_pengiriman_produk_cold_bin(models.Model):
	_name = "adhimix.mrp.pengiriman.produk.cold.bin"

	reference = fields.Many2one(comodel_name="adhimix.mrp.pengiriman",string="No Dokumen")
	tanggal_efektif= fields.Date(string="Tanggal Efektif")

	kriteria_dimensi_produk = fields.Char(string="Kriteria")
	toleransi_dimensi_produk = fields.Char(string="Toleransi")
	hasil_pemeriksaan_dimensi_produk_i = fields.Text(string="Hasil Pemeriksaan I")
	hasil_pemeriksaan_dimensi_produk_ii = fields.Text(string="Hasil Pemeriksaan II")
	keterangan_dimensi_produk = fields.Text(string="Keterangan")

	kriteria_purchase_part = fields.Char(string="Kriteria")
	toleransi_purchase_part = fields.Char(string="Toleransi")
	hasil_pemeriksaan_purchase_part_i = fields.Text(string="Hasil Pemeriksaan I")
	hasil_pemeriksaan_purchase_part_ii = fields.Text(string="Hasil Pemeriksaan II")
	keterangan_purchase_part = fields.Text(string="Keterangan")

	kriteria_kondisi_cat = fields.Char(string="Kriteria")
	toleransi_kondisi_cat = fields.Char(string="Toleransi")
	hasil_pemeriksaan_kondisi_cat_i = fields.Text(string="Hasil Pemeriksaan I")
	hasil_pemeriksaan_kondisi_cat_ii = fields.Text(string="Hasil Pemeriksaan II")
	keterangan_kondisi_cat = fields.Text(string="Keterangan")

	kriteria_pintu_cold_bin = fields.Char(string="Kriteria")
	toleransi_pintu_cold_bin = fields.Char(string="Toleransi")
	hasil_pemeriksaan_pintu_cold_bin_i = fields.Text(string="Hasil Pemeriksaan I")
	hasil_pemeriksaan_pintu_cold_bin_ii = fields.Text(string="Hasil Pemeriksaan II")
	keterangan_pintu_cold_bin = fields.Text(string="Keterangan")


class adh_mrp_pengiriman_produk_silo_mobile(models.Model):
	_name = "adhimix.mrp.pengiriman.produk.silo.mobile"

	reference=fields.Many2one(comodel_name="adhimix.mrp.pengiriman",string="No Dokumen")
	tanggal_efektif = fields.Date(string="Tanggal Efektif")

	kriteria_tabung_silo_mobile = fields.Char(string="Kriteria")
	toleransi_tabung_silo_mobile = fields.Char(string="Toleransi")
	hasil_pemeriksaan_tabung_silo_mobile_i = fields.Text(string="Hasil Pemeriksaan I")
	hasil_pemeriksaan_tabung_silo_mobile_ii = fields.Text(string="Hasil Pemeriksaan II")
	keterangan_tabung_silo_mobile = fields.Text(string="Keterangan")

	kriteria_bagian_dalam_silo_mobile = fields.Char(string="Kriteria")
	toleransi_bagian_dalam_silo_mobile = fields.Char(string="Toleransi")
	hasil_pemeriksaan_bagian_dalam_silo_mobile_i = fields.Text(string="Hasil Pemeriksaan I")
	hasil_pemeriksaan_bagian_dalam_silo_mobile_ii = fields.Text(string="Hasil Pemeriksaan II")
	keterangan_bagian_dalam_silo_mobile = fields.Text(string="Keterangan")

	kriteria_frame_silo_mobile = fields.Char(string="Kriteria")
	toleransi_frame_silo_mobile = fields.Char(string="Toleransi")
	hasil_pemeriksaan_frame_silo_mobile_i = fields.Text(string="Hasil Pemeriksaan I")
	hasil_pemeriksaan_frame_silo_mobile_ii = fields.Text(string="Hasil Pemeriksaan II")
	keterangan_frame_silo_mobile = fields.Text(string="Keterangan")

	kriteria_valve_in_out = fields.Char(string="Kriteria")
	toleransi_valve_in_out = fields.Char(string="Toleransi")
	hasil_pemeriksaan_valve_in_out_i = fields.Text(string="Hasil Pemeriksaan I")
	hasil_pemeriksaan_valve_in_out_ii = fields.Text(string="Hasil Pemeriksaan II")
	keterangan_valve_in_out = fields.Text(string="Keterangan")

	kriteria_valve_material = fields.Char(string="Kriteria")
	toleransi_valve_material= fields.Char(string="Toleransi")
	hasil_pemeriksaan_valve_material_i = fields.Text(string="Hasil Pemeriksaan I")
	hasil_pemeriksaan_valve_material_ii = fields.Text(string="Hasil Pemeriksaan II")
	keterangan_valve_material = fields.Text(string="Keterangan")

	kriteria_main_hole = fields.Char(string="Kriteria")
	toleransi_main_hole = fields.Char(string="Toleransi")
	hasil_pemeriksaan_main_hole_i = fields.Text(string="Hasil Pemeriksaan I")
	hasil_pemeriksaan_main_hole_ii = fields.Text(string="Hasil Pemeriksaan II")
	keterangan_main_hole= fields.Text(string="Keterangan")



class adh_mrp_pengiriman_aksesoris_drum_mixer(models.Model):
	_name = "adhimix.mrp.pengiriman.aksesoris.drum.mixer"

	reference = fields.Many2one(comodel_name="adhimix.mrp.pengiriman",string="No Dokumen")
	tanggal_efektif = fields.Date(string="Tanggal Efektif")

	kriteria_kondisi_produk = fields.Char(string="Kriteria")
	toleransi_kondisi_produk = fields.Char(string="Toleransi")
	hasil_pemeriksaan_kondisi_produk_i = fields.Text(string="Hasil Pemeriksaan I")
	hasil_pemeriksaan_kondisi_produk_ii = fields.Text(string="Hasil Pemeriksaan II")
	keterangan_kondisi_produk = fields.Text(string="Keterangan")





	
