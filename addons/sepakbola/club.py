from odoo import api, fields, models

class Club(models.Model):
    _name = "sepakbola.club"
    _rec_name = "nama"
    nama = fields.Char("Nama Club", required = True, size=100)
    kota = fields.Char("Nama Kota", required = True, size=100)
    alamat = fields.Text("Alamat Lengkap Club")
    #responsible_id = fields.Many2one(
     #   comodel_name="res.users", #ini data bawaan odoo
     #   string="Responsible",
     #   required = True,
    #)

    #session_ids = fields.One2many(
    #    comodel_name="academic.session",
    #    string="Sessions",
    #    inverse_name="course_id", #foreign key
    #)

    _sql_constraints = [
        ('sql_cek_name','UNIQUE(nama)','Nama Tidak Boleh Double'),
    #    ('sql_cek_desc','CHECK(name <> desc)','Name dan Deskripsi Tidak Boleh Sama'),
    ]