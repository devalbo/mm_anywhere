"""
mm_app_core.py
~~~~~~~~~~~~

This module supports accessing image acquisition functionality, similar to the
main Micro-Manager dialog.

:copyright: (c) 2012 by Albert Boehmler
:license: GNU Affero General Public License, see LICENSE for more details.

"""

import sys, os, time, thread
from flask import Blueprint, render_template, abort, url_for, redirect, request
from pylab import imsave, cm

import MMCorePy
from settings import mm_core as mmc
import settings
import configurations
import mm_util

mm_app_core = Blueprint('mm_app_core', __name__,
                        template_folder='templates')


@mm_app_core.route('/')
def index():
    return render_template('acquisition.html',
                           mm_app_core=sys.modules[__name__],
                           configurations=configurations._get_configs_listing())

def get_allowed_binning_values():
    return mmc.getAllowedPropertyValues(mmc.getCameraDevice(),
                                        MMCorePy.g_Keyword_Binning)

def get_available_shutters():
    return mmc.getLoadedDevicesOfType(MMCorePy.ShutterDevice)

@mm_app_core.route('/binning/')
def get_binning():
    return mmc.getProperty(mmc.getCameraDevice(),
                           MMCorePy.g_Keyword_Binning)

@mm_app_core.route('/binning/', methods=['POST'])
def set_binning():
    binning_value = int(request.form['binning'])
    return _set_binning(binning_value)

@mm_app_core.route('/shutter/')
def get_shutter():
    return mmc.getShutterDevice()

@mm_app_core.route('/exposure/')
def get_exposure():
    return mmc.getExposure()

@mm_app_core.route('/exposure/', methods=['POST'])
def set_exposure():
    exposure_value = float(request.form['exposure'])
    return _set_exposure(exposure_value)

@mm_app_core.route('/auto-shutter/')
def get_auto_shutter():
    return mmc.getAutoShutter()

@mm_app_core.route('/auto-shutter/', methods=['POST'])
def set_auto_shutter():
    auto_shutter_value = mm_util.from_js_boolean(request.form['auto-shutter'])
    return _set_auto_shutter(auto_shutter_value)

@mm_app_core.route('/open-shutter/')
def get_shutter_open():
    return mmc.getShutterOpen()

@mm_app_core.route('/open-shutter/', methods=['POST'])
def set_shutter_open():
    open_shutter_value = mm_util.from_js_boolean(request.form['open-shutter'])
    return _set_shutter_open(open_shutter_value)

@mm_app_core.route('/active-shutter/')
def get_active_shutter():
    return mmc.getShutter()

@mm_app_core.route('/active-shutter/', methods=['POST'])
def set_active_shutter():
    active_shutter_value = str(request.form['active-shutter'])
    return _set_active_shutter(active_shutter_value)

@mm_app_core.route('/snap-image/')
def snap_image():
    image_name = _snap_image()
    return render_template('snap-image.html',
                           img_url=url_for('acq.download_acquired_image',
                                           image_name=image_name))


def _is_camera_available():
    return None != mmc.getCameraDevice()
    
def _set_binning(binning_value):
    if (_is_camera_available()):
	mmc.setProperty(mmc.getCameraDevice(),
                        MMCorePy.g_Keyword_Binning,
                        binning_value)
	return mmc.getProperty(mmc.getCameraDevice(),
                               MMCorePy.g_Keyword_Binning)

def _set_exposure(exposure_value):
    mmc.setExposure(exposure_value)
    return str(mmc.getExposure())

def _set_auto_shutter(auto_shutter_value):
    mmc.setAutoShutter(auto_shutter_value)
    return str(mmc.getAutoShutter())

def _set_shutter_open(shutter_open_value):
    mmc.setShutterOpen(shutter_open_value);
    return str(mmc.getShutterOpen())

def _set_active_shutter(active_shutter_value):
    return mmc.setShutterDevice(active_shutter_value)
    return mmc.getShutterDevice()

def _snap_image():
    image_name = "acq-%s.png" % int(time.time() * 1000)
    save_location = os.path.join(settings.MM_ANYWHERE_HOST_DATA_PATH,
                                 image_name)
    camera = ""
##    thread.start_new_thread(_execute_snap_image, (camera, save_location))
##    time.sleep(0.1)
    _execute_snap_image(camera, save_location)
    return image_name

def _execute_snap_image(camera, save_location):
    mmc.snapImage()
    mmc.waitForSystem()
    img = mmc.getImage()

    imsave(save_location, img, cmap = cm.gray)

    
