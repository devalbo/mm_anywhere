"""
configurations.py
~~~~~~~~~~~~

This module supports accessing and updating device configurations.

:copyright: (c) 2012 by Albert Boehmler
:license: GNU Affero General Public License, see LICENSE for more details.

"""

from flask import Blueprint, render_template, abort, request, url_for
from jinja2 import TemplateNotFound

from settings import mm_core as mmc
import MmAnywhere_pb2
import mm_util

configurations = Blueprint('configurations', __name__,
                           template_folder='templates')

@configurations.route('/')
def index():
    return render_template('configurations.html',
                           configurations=_get_configs_listing())

@configurations.route('/<config_id>/')
def get_configuration_preset(config_id):
    return str(_get_config_listing(config_id))

@configurations.route('/<config_id>/', methods=['POST'])
def set_configuration_preset(config_id):
    value = str(request.form['value'])
    return str(_set_configuration_preset(config_id, value))


def _get_configs_listing():
    configs = []
    for config_id in mmc.getAvailableConfigGroups():
        config = _get_config_listing(config_id)
        configs.append(config)
        
    return configs

def _get_config_listing(config_id):
    config_id = str(config_id)
    config = mmc.getAvailableConfigs(config_id)

    config_listing = MmAnywhere_pb2.MmConfigGroup()
    config_listing.configGroupId = config_id
    config_listing.configGroupLabel = config_id
    config_listing.currentPreset = mmc.getCurrentConfig(config_id)
    config_listing.configGroupUrl = url_for('configurations.get_configuration_preset',
                                            config_id=config_id)
    for cfg_preset in _get_presets_for_config(config_id):
        new_preset = config_listing.configGroupPresets.add()
        new_preset.MergeFrom(cfg_preset)

    return config_listing

def _get_presets_for_config(config_id):
    config_id = str(config_id)
    cfg_presets = []
    for preset_id in mmc.getAvailableConfigs(config_id):
        cfg_preset = MmAnywhere_pb2.MmConfigGroupPreset()
        cfg_preset.presetId = preset_id
        cfg_preset.presetLabel = preset_id
        for i in range(mmc.getConfigData(config_id, preset_id).size()):
            preset_cfg = mmc.getConfigData(config_id, preset_id).getSetting(i)
            cfg_preset.presetPropertyDevices.append(preset_cfg.getDeviceLabel())
            cfg_preset.presetPropertyLabels.append(preset_cfg.getPropertyName())
            cfg_preset.presetPropertyValues.append(preset_cfg.getPropertyValue())
        cfg_presets.append(cfg_preset)
        
    return cfg_presets

def _set_configuration_preset(config_id, preset_id):
    preset_id = str(preset_id)
    config_id = str(config_id)
    mmc.setConfig(config_id, preset_id)
    mmc.waitForConfig(config_id, preset_id)
    return mmc.getCurrentConfig(config_id)


