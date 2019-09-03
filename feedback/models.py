from feedback import db


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    service = db.Column(db.String(120))
    rating = db.Column(db.Integer)
    comment = db.Column(db.Text)

    def __repr__(self):
        return '<Feedback {}>'.format(self.name)
