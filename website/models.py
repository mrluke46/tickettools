from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model) :
    id = db.Column(db.Integer, primary_key = True, unique = True)
    data = db.Column(db.String(99999))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

class Ticket(db.Model) :
    ticket_ref = db.Column(db.String(7), primary_key = True, unique = True) # a referance code for ticket (a key)
    code = db.Column(db.String(10)) # generator will do just 8 chars, reserved 2 slots for future changes | (a value)
    permission = db.Column(db.Integer, db.ForeignKey('user.user_role'), default = 0) # 0 = check the validation only, 1 = full permission;
    valid_until = db.Column(db.DateTime(timezone=True))
    issued_date = db.Column(db.DateTime(timezone=True))
    is_apply = db.Column(db.Boolean(), default = False) # the ticket is applied or not
    applied_date = db.Column(db.DateTime(timezone=True))
    issued_by = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    issued_to = db.Column(db.Integer, db.ForeignKey('user.user_id'))

class User(db.Model, UserMixin) :
    user_id = db.Column(db.Integer, primary_key = True, unique = True)
    user_role = db.Column(db.Integer, default=0) # 0 = user, 1 = admin
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship("Note")

 