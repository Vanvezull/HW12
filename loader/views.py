from flask import Blueprint, render_template, request
import functions
from exception import FileTypeError
import logging


loader_blueprint = Blueprint('loader_blueprint', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'tiff'}

logger = logging.getLogger('logger')


def is_filename_allowed(file_type):
    if file_type not in ALLOWED_EXTENSIONS:
        return False
    return True


@loader_blueprint.route('/post_form/')
def upload_post():
    return render_template('post_form.html')


@loader_blueprint.route('/post_uploaded/', methods=["POST"])
def upload_posts():
    picture = request.files.get('picture')
    content = request.form.get('content')
    filename = picture.filename
    file_type = filename.split('.')[-1]
    if file_type not in ALLOWED_EXTENSIONS:
        raise FileTypeError("Неподдерживаемый формат")
    picture.save(f'./uploads/images/{filename}')
    file = f'/uploads/images/{filename}'
    functions.add_post(file, content)
    return render_template('post_uploaded.html', picture=picture, content=content)


@loader_blueprint.errorhandler(FileTypeError)
def file_error(e):
    logger.error('загруженный файл - не картинка')
    return 'Неподдерживаемый формат'
