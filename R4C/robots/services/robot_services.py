def set_robot_serial(instance):
    if instance.model and instance.version:
        instance.serial = f"{instance.model}-{instance.version}"
