from typing import List
from app.models import Sources
from app.models import Articles
from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_articles, get_sources

@main.route('/')
def sources():
    
    all_sources = get_sources()
    return render_template("sources.html", sources = all_sources)

@main.route('/articles/<sources_id>')
def articles(sources_id):
    
    news = get_articles(sources_id)
    return render_template("articles.html", id = news)




#@app.route('/movie/<movie_id>')
#def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    #return render_template('movie.html',id = movie_id)




