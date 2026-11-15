# Part 3: __all__, import * and sys.modules in logtools
# Every cell of the notebook, in order, as one script (run: python Part_3____all____import___and_sys_modules_in_logto.py)

# Sharing names with `__all__`

# import * brings only the shared names

from logtools.summary import *
print(headline(3))
print('_tidy' in dir())

# sys.modules: how Python remembers imports

import sys
print('logtools' in sys.modules)

# ModuleNotFoundError: a wrong package name
