from odoo import fields,api,models,_
import time

class kesiapan_alat_wizard(models.TransientModel):

    _name = "kesiapan.alat.wizard"
    _description = "Kesiapan Alat Dan Bahan"



    # tanggal = fields.Date(string="Tanggal")
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
    def generate_report(self):
        data = {'date_start': self.start_date, 'date_stop': self.end_date}
        # data = {'tanggal':self.tanggal}
        return self.env['report'].get_action(
            [], 'adh_mrp_instalasi.report_kesiapan_alat',data=data)
