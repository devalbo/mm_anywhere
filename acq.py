"""
acq.py
~~~~~~~~~~~~

This module supports hosting acquired data.

:copyright: (c) 2012 by Albert Boehmler
:license: GNU Affero General Public License, see LICENSE for more details.

"""

import os
from flask import Blueprint, render_template, abort, url_for, send_file
from jinja2 import TemplateNotFound
import settings

acq = Blueprint('acq', __name__,
                template_folder='templates')

@acq.route('/img/<image_name>')
def download_acquired_image(image_name):
    if '..' in image_name or image_name.startswith('/'):
        abort(404)
    return send_file(os.path.join(settings.MM_ANYWHERE_HOST_DATA_PATH,
                     image_name), mimetype="image/png")

