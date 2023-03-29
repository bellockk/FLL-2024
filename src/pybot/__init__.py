"""
Automatic Module Organizer.

This will remove a duplicated level of module specification by loading all
modules in this folder into the top level namespace.
"""
import os
import sys
import traceback
_SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, _SCRIPT_PATH)
_MODULE_NAME = os.path.basename(_SCRIPT_PATH)
_MODULES = [os.path.splitext(m)[0] for m in os.ilistdir(_SCRIPT_PATH) if
            (os.path.isfile('/'.join([_SCRIPT_PATH, m])) and m.endswith(
                '.py') and m[0] not in ['_', '.'])]
_MODULES.extend([m for m in os.listdir(_SCRIPT_PATH, m) if
                 (os.path.isdir('/'.join([_SCRIPT_PATH, m])) and m[0] not in
                 ['_', '.']) and m not in ['script']])
__all__ = []
for m in _MODULES:
    try:
        _mod = __import__(m, globals(), locals(), [m])
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print('Within %s, could not load %s library:\n%s' % (
            _SCRIPT_PATH, m, ''.join(traceback.format_exception(
                exc_type, exc_value, exc_traceback))))
        continue
    if hasattr(_mod, '__all__'):
        __all__.extend(_mod.__all__)
        for submod in _mod.__all__:
            if submod in dir(_mod):
                globals()[submod] = getattr(_mod, submod)
            del submod
        del _mod
    del m
del _MODULE_NAME
del _SCRIPT_PATH
del os
del sys
del traceback