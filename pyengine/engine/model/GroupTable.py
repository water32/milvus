from engine import db

class GroupTable(db.Model):
    __tablename__ = 'group_table'
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(100))
    file_number = db.Column(db.Integer)

    def __init__(self, group_name):
        self.group_name = group_name
        self.file_number = 0

    def __repr__(self):
        return '<GroupTable $s>' % self.group_name