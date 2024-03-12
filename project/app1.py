from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import cv2
import easyocr
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String[100], unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


with app.app_context():
    db.create_all()
 
upload_folder = os.path.join('static', 'uploads')
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)

app.config['UPLOAD'] = upload_folder


@app.route("/")
def index():

    return render_template("index.html")



@app.route('/signup',methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        hashed_password = generate_password_hash(password)

        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            return redirect('image_render')
    return render_template('login.html')

@app.route('/image_render', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD'], filename))
        
        img = os.path.join(app.config['UPLOAD'], filename)
        image = cv2.imread(img)
        reader = easyocr.Reader(['en'], gpu=False)
        result = reader.readtext(image)
        text_file_path = os.path.join(app.config['UPLOAD'], 'extracted_text.txt')
        with open(text_file_path, 'w') as text_file:
            for t in result:
                bbox, text_, score = t  
                if score > 0.25:
                    text_file.write(text_ + " ")
    
        
        return render_template('image_render.html', img=img, extracted_text =  [a for _,a, score in result if score > 0.25])
    return render_template('image_render.html')

if __name__ == '__main__':
    app.run(debug=True, port=8001)

