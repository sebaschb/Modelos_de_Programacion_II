import builtins as _mod_builtins

__doc__ = None
__file__ = '/usr/lib/python3.7/lib-dynload/_dbm.cpython-37m-x86_64-linux-gnu.so'
__name__ = '_dbm'
__package__ = ''
class error(_mod_builtins.OSError):
    __class__ = error
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = '_dbm'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

library = 'Berkeley DB'
def open(filename, flags, mode):
    'Return a database object.\n\n  filename\n    The filename to open.\n  flags\n    How to open the file.  "r" for reading, "w" for writing, etc.\n  mode\n    If creating a new file, the mode bits for the new file\n    (e.g. os.O_RDWR).'
    pass

