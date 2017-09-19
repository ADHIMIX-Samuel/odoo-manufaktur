from odoo import fields,api,models,_
import calendar
from datetime import datetime
import time


class evaluasi_penawaran_wizard(models.TransientModel):

	_name = "evaluasi.penawaran.wizard"
	_description = "Evaluasi Penawaran"

	# def get_end_of_month(self):
	# 	sekarang = datetime.now()
	# 	end_date = str(calendar.monthrange(sekarang.year, sekarang.month)[1])
	# 	end = sekarang.strftime('%Y-%m-' + end_date)
	# 	return end


	# tanggal_penawaran = fields.Date(string="Tanggal Penawaran",required=True)
	# start_date = fields.Datetime(required=True,default=time.strftime('%Y-%m-01'))
	start_date = fields.Datetime(required=True)
	end_date = fields.Datetime(required=True,default=fields.Datetime.now)

	@api.onchange('start_date')
	def _onchange_start_date(self):
		if self.start_date and self.end_date and self.end_date < self.start_date:
			self.end_date = self.start_date

	@api.onchange('end_date')
	def _onchange_end_date(self):
		if self.end_date and self.end_date < self.start_date:
			self.start_date = self.end_date


 

	@api.multi
	def evaluasi_penawaran_report(self,data):
		# data = {'tanggal_penawaran': self.tanggal_penawaran}
		data = {'date_start': self.start_date, 'date_stop': self.end_date}
		return self.env['report'].get_action(
			[], 'adh_manufaktur.report_evaluasi_penawaran', data=data)
