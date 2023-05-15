from odoo import api, fields, models
from odoo.exceptions import ValidationError
import time


STATES = [
    ('draft','Draft'),
    ('confirmed','Confirmed'),
    ('done','Done')
]

class Session(models.Model):
    _name = "academic.session"

    name = fields.Char("Session Name", required = True, size=100)
    course_id = fields.Many2one(comodel_name="academic.course", string="Course")
    instructor_id = fields.Many2one(comodel_name="res.partner", string="Instructor")
    start_date = fields.Date("Start Date", default = lambda self:time.strftime("%Y-%m-%d"))
    duration = fields.Integer("Duration")
    seats = fields.Integer("Seats")
    active = fields.Boolean("Is Active", default="True")
    attendee_ids = fields.One2many(
        comodel_name = "academic.attendee",
        string = "Attendees",
        inverse_name = "session_id",
    )
    taken_seats = fields.Float(string="Taken Seats", compute="_compute_taken_seats") 
    image_small = fields.Binary("image")
    state = fields.Selection(
        string = "State",
        selection=STATES,
        readonly=True,
        required=True,
        default=STATES[0][0]
    )


    def _hitungSeats(self, len_att_ids, seats):
        if seats > 0 :
            taken_seats = 100.0 * len_att_ids / seats
            return taken_seats
        else:
            return 0.0

    def _compute_taken_seats(self):
        for data in self :
            if data.seats > 0 :
                data.taken_seats = self._hitungSeats(len(data.attendee_ids), data.seats)
                
    @api.onchange('seats')
    def onchange_seats(data):
        if data.seats > 0 :
            data.taken_seats = data._hitungSeats(len(data.attendee_ids), data.seats)
        
    @api.constrains('attendee_ids')
    def _check_instructor(self):
        for session in self :
            # x = []
            # for attendee in session.attendee_ids :
            #     x.append( attendee.partner_id.id)
            
            x = [ att.partner_id.id for att in session.attendee_ids ]

            if session.instructor_id.id in x :
                raise ValidationError("Tidak boleh merangkap")
        return True
    
    @api.multi
    def copy(self, default=None):
        default = dict(default or {}, name=self.name + " (copy) ")
        return super(Session, self).copy(default=default)
    

    @api.multi
    def action_confirm(self):
        self.state = STATES[1][0] 

    @api.multi
    def action_done(self):
        self.state = STATES[2][0] 

    @api.multi
    def action_draft(self):
        self.state = STATES[0][0]