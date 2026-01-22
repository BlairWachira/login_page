from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class person(db.Model):
  id=db.Column(db.Integer, primary_key=True)
  username=db.Column(db.String(200), nullable=False)
  password=db.Column(db.String(200), nullable=False)

  def __repr__(self):
    return super().__repr__()