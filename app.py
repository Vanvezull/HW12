from flask import Flask, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint
import logger_main
import logging

UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

logger_main.create_logger()
logger = logging.getLogger('logger')


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run(debug=True)



