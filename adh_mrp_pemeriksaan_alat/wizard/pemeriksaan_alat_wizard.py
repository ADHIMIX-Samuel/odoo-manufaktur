from odoo import fields,api,models,_
from odoo.exceptions import UserError

class pemeriksaan_alat_wizard(models.TransientModel):

	_name = "pemeriksaan.alat.wizard"
	_description = "pemeriksaan Kerusakan Alat"


	tanggal_masuk_alat = fields.Date(string="Tanggal Masuk Alat",required=True)
	# start_date = fields.Datetime(required=True)
	# end_date = fields.Datetime(required=True, default=fields.Datetime.now)

	# @api.onchange('start_date')
	# def _onchange_start_date(self):
	# 	if self.start_date and self.end_date and self.end_date < self.start_date:
	# 		self.end_date = self.start_date

	# @api.onchange('end_date')
	# def _onchange_end_date(self):
	# 	if self.end_date and self.end_date < self.start_date:
	# 		self.start_date = self.end_date


 

	@api.multi
	def generate_report(self,data):
		data = {'tanggal_masuk_alat': self.tanggal_masuk_alat}
		# data = {'date_start': self.start_date, 'date_stop': self.end_date}
		return self.env['report'].get_action(
			[], 'adh_mrp_pemeriksaan_alat.report_pemeriksaan_alat', data=data)
		