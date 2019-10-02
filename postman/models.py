from postman import db


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    summary = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Blog('{self.title}')"
