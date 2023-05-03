from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretzkey$$'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    short_description = db.Column(db.String(100))
    image_url = db.Column(db.String(1000))
    modal_body = db.Column(db.String(1000))


    def to_dict(self):
        """
        Returns a dictionary representation of the Projects object.
        """
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

#Line below only required once, when creating DB.
db.create_all()


@app.route('/')
def run():
    projects = db.session.query(Projects).all()
    return render_template('index.html', data=[row.to_dict() for row in projects])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)