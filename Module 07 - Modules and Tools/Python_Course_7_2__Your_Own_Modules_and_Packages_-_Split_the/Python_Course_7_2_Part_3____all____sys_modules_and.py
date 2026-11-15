# Python Course 7.2 Part 3: __all__, sys.modules and ModuleNotFoundError
# Every cell of the notebook, in order, as one script (run: python Python_Course_7_2_Part_3____all____sys_modules_and.py)

# ## Hide helpers with `__all__` in a new module

# ## Star import and `__all__`: only the shared names

from logtools.summary import *
print(headline(3))
print('_tidy' in dir())

# ## sys.modules: how Python remembers imported modules

import sys
print('logtools' in sys.modules)

# ## ModuleNotFoundError: the most common import mistake
