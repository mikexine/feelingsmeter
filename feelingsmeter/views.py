from flask import render_template, flash, request
from .tools import s3_upload
from .forms import UploadForm
from .app import app


@app.route('/', methods=['POST', 'GET'])
def home():
    form = UploadForm()
    if form.validate_on_submit():
        output = s3_upload(form.file, request.form)
        print(output)
        flash('%s %s %s %s' % (request.form['email'], request.form['text'],
                               request.form['datetime'], request.form['user']))
    return render_template('index.html', form=form)


@app.route('/temp')
def temp():
    form = UploadForm()
    return render_template('tmp.html', form=form)
