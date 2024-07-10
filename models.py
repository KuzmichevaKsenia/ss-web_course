from db import db


class EmployeeModel(db.Model):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    position = db.Column(db.String(80), nullable=False)

    # def __init__(self, name, position, id_=None):
    #     if id_:
    #         self.id = id_
    #     self.name = name
    #     self.position = position
