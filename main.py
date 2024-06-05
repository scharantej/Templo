
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Create a Flask app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///temples.db'
db = SQLAlchemy(app)

# Define the 'temples' table within the database
class Temple(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    location = db.Column(db.String(120), nullable=False)
    deities_worshipped = db.Column(db.String(255), nullable=False)
    history = db.Column(db.Text, nullable=True)
    architecture = db.Column(db.Text, nullable=True)
    current_status = db.Column(db.String(80), nullable=False)
    image_url = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return '<Temple %r>' % self.name

# Create the database and tables
db.create_all()

# Define the home page route
@app.route('/')
def index():
    """Renders the home page with a list of all temples."""
    temples = Temple.query.all()
    return render_template('temples.html', temples=temples)

# Define the route to display a specific temple
@app.route('/temple/<temple_name>')
def temple(temple_name):
    """Renders the details of a specific temple."""
    temple = Temple.query.filter_by(name=temple_name).first_or_404()
    return render_template('temple.html', temple=temple)

# Define the route to add a new temple
@app.route('/add_temple', methods=['GET', 'POST'])
def add_temple():
    """Adds a new temple to the database."""
    if request.method == 'POST':
        new_temple = Temple(
            name=request.form['name'],
            location=request.form['location'],
            deities_worshipped=request.form['deities_worshipped'],
            history=request.form['history'],
            architecture=request.form['architecture'],
            current_status=request.form['current_status'],
            image_url=request.form['image_url']
        )
        db.session.add(new_temple)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add_temple.html')

# Define the route to edit a temple
@app.route('/edit_temple/<temple_name>', methods=['GET', 'POST'])
def edit_temple(temple_name):
    """Edits an existing temple in the database."""
    temple = Temple.query.filter_by(name=temple_name).first_or_404()

    if request.method == 'POST':
        temple.name = request.form['name']
        temple.location = request.form['location']
        temple.deities_worshipped = request.form['deities_worshipped']
        temple.history = request.form['history']
        temple.architecture = request.form['architecture']
        temple.current_status = request.form['current_status']
        temple.image_url = request.form['image_url']
        db.session.commit()
        return redirect(url_for('temple', temple_name=temple_name))

    return render_template('edit_temple.html', temple=temple)

# Define the route to delete a temple
@app.route('/delete_temple/<temple_name>')
def delete_temple(temple_name):
    """Deletes a temple from the database."""
    temple = Temple.query.filter_by(name=temple_name).first_or_404()
    db.session.delete(temple)
    db.session.commit()
    return redirect(url_for('index'))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
