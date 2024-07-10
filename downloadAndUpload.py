from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key'
app.config['UPLOAD_FOLDER'] = r'C:\Users\user1\Desktop\proForCourse\files' 

class UploadFileForm(FlaskForm):
    file = FileField("file")
    submit = SubmitField("Upload File")


@app.route('/', methods=['GET','POST'])
@app.route('/home',  methods=['GET','POST'])

def home():
    form = UploadFileForm()
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)