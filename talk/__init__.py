import os
from os.path import join, exists, isdir, isfile, dirname, abspath, expanduser
from defs import *

is_uninstalled = False
def _check(path):
    return exists(path) and isdir(path) and isfile(path+"/AUTHORS")

name = join(dirname(__file__), '..')
if _check(name):
    is_uninstalled = True

if is_uninstalled:
#    print 'uninstalled, adding %s to sys.path' % abspath(join(dirname(__file__), '..', 'data'))
    SHARED_DATA_DIR = abspath(join(dirname(__file__), '..', 'data'))
else:
    SHARED_DATA_DIR = join(DATA_DIR, 'talk-clutter')

