from app.settings import Instance
from app.handlers import output_formatter

import logging

def check_instance(embed, user_configs, instance_type):

    if instance_type == Instance.T2_SMALL.value:
        user_configs["instance_type"] = Instance.T2_SMALL.value
    elif instance_type == Instance.T2_MEDIUM.value:
        user_configs["instance_type"] = Instance.T2_MEDIUM.value
    elif instance_type == Instance.G4DN_XLARGE.value:
        user_configs["instance_type"] = Instance.G4DN_XLARGE.value
    elif instance_type == Instance.C5A_LARGE.value:
        user_configs["instance_type"] = Instance.C5A_LARGE.value
    elif instance_type == Instance.C5A_XLARGE.value:
        user_configs["instance_type"] = Instance.C5A_XLARGE.value
    elif instance_type == Instance.C5A_2XLARGE.value:
        user_configs["instance_type"] = Instance.C5A_2XLARGE.value
    elif instance_type == Instance.R5A_LARGE.value:
        user_configs["instance_type"] = Instance.R5A_LARGE.value
    elif instance_type == Instance.R5A_XLARGE.value:
        user_configs["instance_type"] = Instance.R5A_XLARGE.value
    elif instance_type == Instance.R5A_2XLARGE.value:
        user_configs["instance_type"] = Instance.R5A_2XLARGE.value
    elif instance_type == Instance.R6A_LARGE.value:
        user_configs["instance_type"] = Instance.R6A_LARGE.value
    elif instance_type == Instance.R6A_XLARGE.value:
        user_configs["instance_type"] = Instance.R6A_XLARGE.value
    elif instance_type == Instance.R6A_2XLARGE.value:
        user_configs["instance_type"] = Instance.R6A_2XLARGE.value
    else:
        # invalid instance, ignore user configs
        user_configs.clear()
        output_formatter.set_instance_error(embed, instance_type)
    
    return embed
