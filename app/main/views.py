from flask import render_template,request,redirect,url_for,abort
from . import main
# from ..request import get_movies,get_movie,search_movie
from .forms import pitchForm,UpvoteForm
from ..models import User,pitch,upvote,downvote
from flask_login import login_required,current_user
from .. import db,photos

# Views
@main.route('/',methods=['GET','POST'])
def index():
  
    '''
    View root page function that returns the index page and its data
    '''
    upvote=Upvote.get_all_upvotes(pitch_id=pitch.id)
    title="WELCOME"

    return render_template('index.html',title =title,upvotes=upvotes)
@main.route('/pitch/<int:id>')
def pitch(id):

    '''
    View pitch page function that returns the pitch details page and its data
    '''
    pitch = get_pitch(id)
    title = f'{pitch.title}'
    reviews = Review.get_reviews(pitch.id)

    return render_template('pitch.html',title = title,pitch = pitch,reviews = reviews)



@main.route('/pitch/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_pitch(id):

    form = PitchForm()
    pitch = get_pitch(id)

    if form.validate_on_submit():
        title = form.title.data
        new_upvote= Upvote(pitch.id,title,pitch.poster,pitch_upvote=review,user=current_user)
        #save review method
        new_pitch.save_pitch()
        return redirect(url_for('.pitch',id = pitch.id ))

    title = f'{pitch.title} pitch'
    return render_template('new_pitches.html',title = title, form=form)

@main.route('/pitch/upvote/<int:pitch_id>/upvote', methods = ['GET', 'POST'])
@login_required
def upvote(pitch_id):
    pitch = Pitch.query.get(pitch_id)
    user = current_user
    pitch_upvotes = Upvote.query.filter_by(pitch_id= pitch_id)
    
    if Upvote.query.filter(Upvote.user_id==user.id,Upvote.pitch_id==pitch_id).first():
        return  redirect(url_for('main.index'))


    new_upvote = Upvote(pitch_id=pitch_id, user = current_user)
    new_upvote.save_upvotes()
    return redirect(url_for('main.index'))



@main.route('/pitch/downvote/<int:pitch_id>/downvote', methods = ['GET', 'POST'])
@login_required
def downvote(pitch_id):
    pitch = Pitch.query.get(pitch_id)
    user = current_user
    pitch_downvotes = Downvote.query.filter_by(pitch_id= pitch_id)
    
    if Downvote.query.filter(Downvote.user_id==user.id,Downvote.pitch_id==pitch_id).first():
        return  redirect(url_for('main.index'))


