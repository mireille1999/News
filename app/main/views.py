from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_articles
from ..models import Source,Article


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    business = get_sources('business')
    general = get_sources('general')
    technology = get_sources('technology')
    health = get_sources('health')
    entertainment = get_sources('entertainment')
    sports = get_sources('sports')
    science = get_sources('science')


    title = 'Home - Welcome to The best News App'
    return render_template('index.html', title = title,business = business,general = general,technology = technology,health = health,entertainment = entertainment,sports = sports,science = science)




@main.route('/sources/<id>')
def articles(id):
    '''
    View article page function that returns the article details page and its data
    '''
    articles = get_articles(id)
    title = f'You are viewing {id}'
    return render_template('articles.html',title = title,articles = articles)

