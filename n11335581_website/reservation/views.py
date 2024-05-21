from flask import Blueprint, render_template, redirect, url_for, request, flash, url_for
from .forms import ContactForm, HotelForm, RegisterForm, DestinationForm, CommentForm
from . import db
from .models import Hotel, User, Destination, Comment
from flask_login import login_required, current_user


mainbp = Blueprint('main',__name__)

@mainbp.route('/')
def index():
    tag_line='You need a vacation'
    hotels = Hotel.query.all() #get the hotels
    form=ContactForm()
    return render_template('index.html', tag_line=tag_line,
                    form=form, hotels=hotels)

##for the destinations screen
##@mainbp.route('/destinations/show', methods=['GET,', 'POST'])
##@login_required
##def index():
##    hotels = Hotel.query.all() #get the hotels
##    form=ContactForm()
##    return render_template('show.html',
##                    form=form, hotels=hotels)


@mainbp.route('/hotel/create', methods=['GET','POST']) # both get and post
@login_required
def add_hotel():
     
     if current_user.usertype != 'admin':
          flash("Need administrator login")
          return redirect(url_for('auth.login'))
     
     
     print('In create hotel')
     form = HotelForm()
     
     if form.validate_on_submit():
          print("Form has been submitted successfully")
          #create a new hotel with the information passed
          new_hotel = Hotel(name=form.name.data, description=form.description.data,
                              image=form.image.data)
          # when creating a room, pass the hotel and set the attribute 
          db.session.add(new_hotel)
          db.session.commit()
          return redirect(url_for('main.add_hotel'))
          
     return render_template('forms.html', form=form)


