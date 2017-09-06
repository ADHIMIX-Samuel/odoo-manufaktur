from odoo import fields,api,models,_
from odoo.exceptions import UserError

class pengiriman_wizard(models.TransientModel):

    _name = "pengiriman.wizard"
    _description = "Inspeksi Pengiriman"

    # tanggal_efektif = fields.Date(string="Tanggal Efektif")
    start_date = fields.Datetime(required=True,)
    end_date = fields.Datetime(required=True, default=fields.Datetime.now)

    @api.onchange('start_date')
    def _onchange_start_date(self):
        if self.start_date and self.end_date and self.end_date < self.start_date:
            self.end_date = self.start_date

    @api.onchange('end_date')
    def _onchange_end_date(self):
        if self.end_date and self.end_date < self.start_date:
            self.start_date = self.end_date

    @api.multi

 

    @api.multi
    def inspeksi_report(self):
    	# data = {'tanggal_efektif':self.tanggal_efektif}
    	data = {'date_start': self.start_date, 'date_stop': self.end_date}
        return self.env['report'].get_action(
            [], 'adh_mrp_pengiriman.report_inspeksi_pengiriman',data=data)
