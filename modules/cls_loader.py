import inspect
import sys
import traceback

# List all classes under module path. ex. list_class_names('package.path')
def list_class_names(mod_str):
    __import__(mod_str)
    attrs = inspect.getmembers(sys.modules[mod_str])
    return [name for name, obj in attrs if inspect.isclass(obj)]


# Dynamic import class from full class path. ex. list_class_names('package.path.ClassName')
def import_class(import_str):
    mod_str, _sep, class_str = import_str.rpartition('.')
    __import__(mod_str)
    try:
        return getattr(sys.modules[mod_str], class_str)
    except AttributeError:
        raise ImportError(f'Class {class_str} cannot be found ({traceback.format_exception(*sys.exc_info())})')