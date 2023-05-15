from odoo import api, fields, models

class Pemain(models.Model):
    _name = "sepakbola.pemain"
    _rec_name = "nama"
    nama = fields.Char("Nama Pemain", required = True, size=100)
    no_baju = fields.Char("Nomor Punggung", required = True, size=2)
    kota = fields.Char("Asal Kota", required = True, size=100)
    
    club_id = fields.Many2one(
        comodel_name="sepakbola.club", #ini data bawaan odoo
        string="Nama Club",
        required = True,
    )
    
    istri_ids = fields.One2many(
        comodel_name="sepakbola.istri",
        string="Istri",
        inverse_name="pemain_id", #foreign key
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