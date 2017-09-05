from odoo import api,fields,models,_ 

class report_kesiapan_pondasi(models.Model):
	_name = "report.adh_mrp_instalasi.report_kesiapan_pondasi"

	@api.model
	def get_kesiapan_pondasi_details(self,tanggal=False):
	# def get_kesiapan_alat_details(self, date_start =False,date_stop=False):

		# if date_start:
		# 	date_start = fields.Datetime.from_string(date_start)
		# else:
		# 	# start by default today 00:00:00
		# 	date_start = today

		# if date_stop:
		# 	# set time to 23:59:59
		# 	date_stop = fields.Datetime.from_string(date_stop)
		# else:
		# 	# stop by default today 23:59:59
		# 	date_stop = today + timedelta(days=1, seconds=-1)

		# # avoid a date_stop smaller than date_start
		# date_stop = max(date_stop, date_start)

		# date_start = fields.Datetime.to_string(date_start)
		# date_stop = fields.Datetime.to_string(date_stop)

		kesiapan_pondasi_ids = self.env['adhimix.mrp.kesiapan.pondasi.produk'].search([
        	('tanggal','<=',tanggal)
            # ('tanggal','>=',date_start),
            # ('tanggal','<=',date_stop)
        	])

		for x in kesiapan_pondasi_ids:
			nomor_pondasi = x.name 
			tanggal = x.tanggal
			tanggal_efektif = x.tanggal_efektif
			lokasi_install = x.lokasi_install
			nama_pekerjaan = x.nama_pekerjaan
			company_id = x.company_id.logo
			produk_silo_coldbin_ids = x.produk_silo_coldbin_ids
			uraian_pondasi = x.produk_silo_coldbin_ids.uraian_id.name
			kriteria_pondasi = x.produk_silo_coldbin_ids.kriteria_id.name

		return{
			'nomor_pondasi' : nomor_pondasi,
			'tanggal' : tanggal,
			'tanggal_efektif':tanggal_efektif,
			'lokasi_install' : lokasi_install,
			'nama_pekerjaan' : nama_pekerjaan,
			'company_id' : company_id,
			'produk_silo_coldbin_ids':produk_silo_coldbin_ids,
			'kesiapan_pondasi_ids': kesiapan_pondasi_ids,
			'uraian_pondasi' : uraian_pondasi,
			'kriteria_pondasi': kriteria_pondasi

			}


	@api.multi
	def render_html(self, docids, data=None):
		data = dict(data or {})        
		data.update(self.get_kesiapan_pondasi_details(data['tanggal']))
		# data.update(self.get_kesiapan_alat_details(data['date_start'],data['date_stop']))
		return self.env['report'].render('adh_mrp_instalasi.report_kesiapan_pondasi', data)
