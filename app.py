from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Notes(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100))
    content =db.Column(db.Text)

@app.route('/')
def home():
    notes = Notes.query.all()
    return render_template('index.html',notes=notes)

@app.route('/add',methods=['POST'])
def add():
    title = request.form['title']
    content = request.form['content']
    new_notes = Notes(title=title,content=content)
    db.session.add(new_notes)
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    note = Notes.query.get(id)
    db.session.delete(note)
    db.session.commit()
    return redirect('/')

@app.route('/edit/<int:id>')
def edit(id):
    note = Notes.query.get_or_404(id)
    return render_template('edit.html',note=note)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    note = Notes.query.get_or_404(id)
    note.title = request.form['title']
    note.content = request.form['content']
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # This creates the table if it doesn't exist
    app.run(debug=True)