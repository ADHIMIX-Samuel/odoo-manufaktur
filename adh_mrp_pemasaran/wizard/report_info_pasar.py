from odoo import fields,api,models,_

class info_pasar_wizard(models.TransientModel):

    _name = "info.pasar.wizard2"
    _description = "Info Pasar Wizard"

    # tanggal_informasi = fields.Date(string="Tanggal Informasi Pasar",required=True)
    # info_pasar_id = fields.One2many(comodel_name="adhimix.mrp.info.pasar",inverse_name="name")

    @api.multi
    def generate_report(self):
        # data = {'tanggal_informasi': self.tanggal_informasi, 'info_pasar_id': self.info_pasar_id}
        return self.env['report'].get_action( self, 'adh_mrp_pemasaran.info_pasar_report')


   
