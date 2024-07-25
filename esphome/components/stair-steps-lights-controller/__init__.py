import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID

StairStepsLightsController_ns = cg.esphome_ns.namespace('StairStepsLightsController')
StairStepsLightsController = StairStepsLightsController_ns.class_('StairStepsLightsController', cg.Component)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(StairStepsLightsController)
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
