from app.settings import Instance
from app.handlers import output_formatter

import logging

def check_instance(user_configs, instance_type):
   
    embed = output_formatter.corekeeper_set_instance_success(instance_type)

    if instance_type == Instance.T2_SMALL.value:
        user_configs["instance_type"] = Instance.T2_SMALL.value
    elif instance_type == Instance.T2_MEDIUM.value:
        user_configs["instance_type"] = Instance.T2_MEDIUM.value
    elif instance_type == Instance.G4DN_XLARGE.value:
        user_configs["instance_type"] = Instance.G4DN_XLARGE.value
    elif instance_type == Instance.M5A_LARGE.value:
        user_configs["instance_type"] = Instance.M5A_LARGE.value
    elif instance_type == Instance.M5A_XLARGE.value:
        user_configs["instance_type"] = Instance.M5A_XLARGE.value
    elif instance_type == Instance.C5A_LARGE.value:
        user_configs["instance_type"] = Instance.C5A_LARGE.value
    elif instance_type == Instance.C5A_XLARGE.value:
        user_configs["instance_type"] = Instance.C5A_XLARGE.value
    elif instance_type == Instance.M5N_LARGE.value:
        user_configs["instance_type"] = Instance.M5N_LARGE.value
    elif instance_type == Instance.M5N_XLARGE.value:
        user_configs["instance_type"] = Instance.M5N_XLARGE.value
    elif instance_type == Instance.C5_LARGE.value:
        user_configs["instance_type"] = Instance.C5_LARGE.value
    elif instance_type == Instance.C5_XLARGE.value:
        user_configs["instance_type"] = Instance.C5_XLARGE.value
    elif instance_type == Instance.M5ZN_LARGE.value:
        user_configs["instance_type"] = Instance.M5ZN_LARGE.value
    elif instance_type == Instance.M5ZN_XLARGE.value:
        user_configs["instance_type"] = Instance.M5ZN_XLARGE.value
    elif instance_type == Instance.C5N_LARGE.value:
        user_configs["instance_type"] = Instance.C5N_LARGE.value
    elif instance_type == Instance.C5N_XLARGE.value:
        user_configs["instance_type"] = Instance.C5N_XLARGE.value
    else:
        # invalid instance, ignore user configs
        user_configs = {}
        embed = output_formatter.corekeeper_set_instance_error(instance_type)
    
    return embed
