from distutils.core import setup
import py2exe
import matplotlib

opts = {
    "py2exe": {
        "dll_excludes": ["MSVCP90.dll"],
        "includes": ["matplotlib.backends.backend_tkagg"],
        'packages': ['werkzeug', 'email', 'jinja2.ext'],
        }
    }

setup(console=['mm_anywhere.py'],
      options=opts,
      data_files=matplotlib.get_py2exe_datafiles()
    )
