from flask import Blueprint, render_template, request
import functions
from exception import DataError
import logging

main_blueprint = Blueprint('main_blueprint', __name__)
logger = logging.getLogger('logger')


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_post():
    s = request.args.get('s', '')
    search_posts = functions.search_post_cont(s)
    logger.info(f'Выполняется поиск по слову: {s.title()}')
    return render_template('post_list.html', posts=search_posts, s=s)

@main_blueprint.errorhandler(DataError)
def file_error(e):
    logger.error('Файл поврежден')
    return 'Файл поврежден'
