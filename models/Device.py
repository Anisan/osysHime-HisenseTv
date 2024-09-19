from app.database import Column, Model, SurrogatePK, db

class Device(SurrogatePK, db.Model):
    __tablename__ = 'hisense_device'
    title = Column(db.String(100))
    ip = Column(db.String(100))
    mac = Column(db.String(100))