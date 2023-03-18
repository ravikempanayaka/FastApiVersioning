
from importlib import import_module


def create_version_item(version_name, class_name):
    parent_path = 'client'
    file_name = 'v' + str(version_name)
    return import_module_var('%s.%s.%s' % (parent_path, file_name, class_name), None)()


def import_module_var(path, default):
    module_name, var_name = path.rsplit('.', 1)
    return getattr(import_module(module_name), var_name, default)
