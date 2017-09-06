from odoo import api,fields,models,_ 

class report_pemeriksaan_alat(models.Model):
	_name = "report.adh_mrp_pemeriksaan_alat.report_pemeriksaan_alat"

	@api.model
	def get_pemeriksaan_alat_details(self,tanggal_masuk_alat = False):
	# def get_pemeriksaan_alat_details(self, date_start =False,date_stop=False):

	# 	if date_start:
	# 		date_start = fields.Datetime.from_string(date_start)
	# 	else:
	# 		# start by default today 00:00:00
	# 		date_start = today

	# 	if date_stop:
	# 		# set time to 23:59:59
	# 		date_stop = fields.Datetime.from_string(date_stop)
	# 	else:
	# 		# stop by default today 23:59:59
	# 		date_stop = today + timedelta(days=1, seconds=-1)

	# 	# avoid a date_stop smaller than date_start
	# 	date_stop = max(date_stop, date_start)

	# 	date_start = fields.Datetime.to_string(date_start)
	# 	date_stop = fields.Datetime.to_string(date_stop)

		pemeriksaan_alat = self.env['adhimix.mrp.pemeriksaan.kerusakan.alat'].search([
        	('tanggal_masuk_alat','<=',tanggal_masuk_alat)
            # ('tanggal','>=',date_start),
            # ('tanggal','<=',date_stop)
        	])
		pemeriksaan_alat_ids = self.env['adhimix.mrp.pemeriksaan.alat.detail']
		for alat_id in pemeriksaan_alat :
			pemeriksaan_alat_ids += alat_id.pemeriksaan_alat_ids



		for x in pemeriksaan_alat:
			tanggal_masuk_alat = x.tanggal_masuk_alat
			company_id = x.company_id.logo
	

		return{
			'tanggal_masuk_alat':tanggal_masuk_alat,
			'company_id' : company_id,
			'pemeriksaan_alat':pemeriksaan_alat,
			'pemeriksaan_alat_ids':pemeriksaan_alat_ids

			}


	@api.multi
	def render_html(self, docids, data=None):
		data = dict(data or {})      
		data.update(self.get_pemeriksaan_alat_details(data['tanggal_masuk_alat']))
		# data.update(self.get_pemeriksaan_alat_details(data['date_start'],data['date_stop']))
		return self.env['report'].render('adh_mrp_pemeriksaan_alat.report_pemeriksaan_alat', data)
