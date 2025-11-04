from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    group_name = db.Column(db.String(50), default='General')
    phone = db.Column(db.String(20), nullable=False)
    backup_phone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    home_address = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'group': self.group_name,
            'phone': self.phone,
            'backupPhone': self.backup_phone,
            'email': self.email,
            'homeAddress': self.home_address,
            'createdAt': self.created_at.isoformat(),
            'updatedAt': self.updated_at.isoformat()
        }
