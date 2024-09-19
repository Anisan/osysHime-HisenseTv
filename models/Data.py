from app.database import Column, Model, SurrogatePK, db

class Data(SurrogatePK, db.Model):
    __tablename__ = 'hisense_device_data'
    device_id = Column(db.Integer)
    title = Column(db.String(100))
    value = Column(db.Text)
    updated = Column(db.DateTime)
    linked_object = Column(db.String(100))
    linked_property = Column(db.String(100))
    linked_method = Column(db.String(100))
