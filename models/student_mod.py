from dbconn import db

class Stu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name  = db.Column(db.String(200), nullable=False)
    last_name  = db.Column(db.String(200), nullable=False)  
    dob = db.Column(db.Date,nullable=False)  
    email = db.Column(db.String(120), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "dob": self.dob.isoformat(),
            "email": self.email,
            
        }

  