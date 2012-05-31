"""
devices.py
~~~~~~~~~~~~

This module supports accessing and updating devices and device properties.

:copyright: (c) 2012 by Albert Boehmler
:license: GNU Affero General Public License, see LICENSE for more details.

"""

from flask import Blueprint, render_template, abort, request, url_for
from jinja2 import TemplateNotFound

from settings import mm_core as mmc
import MmAnywhere_pb2
import mm_util

devices = Blueprint('devices', __name__,
                    template_folder='templates')

@devices.route('/')
def index():
    return render_template('devices.html',
                           devices=_get_devices_listing())

@devices.route('/<device_id>/')
def get_device(device_id):
    return str(_get_device_listing(device_id))

@devices.route('/<device_id>/properties/')
def get_device_properties(device_id):
    return str([str(dp) for dp in _get_properties_for_device(device_id)])

@devices.route('/<device_id>/properties/<property_id>/')
def get_device_property(device_id, property_id):
    return str(_get_property_for_device(device_id, property_id))

@devices.route('/<device_id>/properties/<property_id>/', methods=['POST'])
def set_device_property(device_id, property_id):
    value = str(request.form['propVal'])
    return str(_set_property_for_device(device_id, property_id, value))


def _get_devices_listing():
    devices = []
    for device_id in mmc.getLoadedDevices():
        device = _get_device_listing(device_id)
        devices.append(device)
        
    return devices

def _get_device_listing(device_id):
    device_id = str(device_id)
    device_type = mmc.getDeviceType(device_id)

    device_listing = MmAnywhere_pb2.MmDeviceListing()
    device_listing.deviceId = device_id
    device_listing.deviceLabel = device_id
    device_listing.deviceType = str(device_type)
    device_listing.deviceUrl = url_for('devices.get_device',
                                       device_id=device_id)
    for dev_prop in _get_properties_for_device(device_id):
        new_prop = device_listing.deviceProperties.add()
        new_prop.MergeFrom(dev_prop)

    return device_listing

def _get_properties_for_device(device_id):
    dev_properties = []
    for prop_name in mmc.getDevicePropertyNames(str(device_id)):
        prop = _get_property_for_device(device_id, prop_name)
        dev_properties.append(prop)
        
    return dev_properties

def _get_property_for_device(device_id, property_id):
    device_id = str(device_id)
    property_id = str(property_id)
    property_type = mmc.getPropertyType(device_id, property_id)
    property_value = mmc.getProperty(device_id, property_id)

    device_property = MmAnywhere_pb2.MmDeviceProperty()
    device_property.propertyId = property_id
    device_property.propertyLabel = property_id
    device_property.propertyType = mm_util.get_property_type_str(property_type)
    device_property.propertyValue = property_value
    device_property.propertyUrl = url_for('devices.get_device_property',
                                          device_id=device_id,
                                          property_id=property_id)

    return device_property

def _set_property_for_device(device_id, property_id, value):
    device_id = str(device_id)
    property_id = str(property_id)
    value = str(value)
    mmc.setProperty(device_id, property_id, value)
    mmc.waitForDevice(device_id)
    return mmc.getProperty(device_id, property_id)
    

