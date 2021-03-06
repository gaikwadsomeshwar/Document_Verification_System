from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, VerificationForm, EditForm, RegistrationForm
from flask_login import current_user, login_user, login_required, logout_user
from app.models import User, Aadhar, PAN
from werkzeug.urls import url_parse

@app.route('/', methods=['GET', 'POST'])
@app.route('/mainpage', methods=['GET', 'POST'])
def mainpage():
    form = VerificationForm()
    if form.validate_on_submit():
        if(form.type.data=='Aadhar Card'):
            doc = Aadhar.query.all();
            for d in doc:
                if(d.check_data(form.docid.data, form.firstname.data, form.lastname.data)):
                    flash('Document Exists. Valid Document.')
                    return redirect(url_for('mainpage'))
            flash('Document Does Not Exist')
            return redirect(url_for('mainpage'))
        else:
            doc = PAN.query.all();
            for d in doc:
                if(d.check_data(form.docid.data, form.firstname.data, form.lastname.data)):
                    flash('Document Exists. Valid Document.')
                    return redirect(url_for('mainpage'))
            flash('Document Does Not Exist')
            return redirect(url_for('mainpage'))
    return render_template('mainpage.html', title='Home',form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('Already Logged In')
        return redirect(url_for('edit'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('edit')
        flash('Logged In')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('Logged Out')
    return redirect(url_for('mainpage'))

@app.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    if current_user.is_authenticated:
        return redirect(url_for('register'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditForm()
    if form.validate_on_submit():
        doc = PAN()
        docs = PAN.query.all()
        if(form.type.data=='Aadhar Card'):
            doc = Aadhar()
            docs = Aadhar.query.all()
        doc.set_data(form.docid.data, form.firstname.data, form.lastname.data)
        for d in docs:
            if(d.check_docid(form.docid.data)):
                flash("Document Already Exists")
                return redirect(url_for('edit'))
        db.session.add(doc)
        db.session.commit()
        flash('Document Added Succesfully')
        return redirect(url_for('edit'))
    return render_template('edit.html', title='Add a Doc', form=form)

@app.route('/contactus')
def contactus():
    return render_template('contactus.html', title='Contact Us')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html', title='About Us')
