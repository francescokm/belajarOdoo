from odoo import api, fields, models

class Istri(models.Model):
    _name = "sepakbola.istri"
    _rec_name = "nama"
    nama = fields.Char("Nama Istri", required = True, size=100)
    keturunan= fields.Char("Keturunan", required = True, size=100)
    kota = fields.Char("Nama Kota", required = True, size=100)
    
    pemain_id = fields.Many2one(
        comodel_name="sepakbola.pemain", #ini data bawaan odoo
        string="Nama Pemain",
        required = True,
    )

    # club_id = fields.One2many(
       # comodel_name="sepakbola.club",
       # string="Pemain",
       # inverse_name="pemain_id", #foreign key
    # )

    #_sql_constraints = [
    #    ('sql_cek_name','UNIQUE(nama)','Nama Tidak Boleh Double'),
    #    ('sql_cek_desc','CHECK(name <> desc)','Name dan Deskripsi Tidak Boleh Sama'),
    #]