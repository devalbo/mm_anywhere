from distutils.core import setup
import os
import py2exe
import matplotlib

opts = {
    "py2exe": {
        "dll_excludes": ["MSVCP90.dll"],
        "includes": ["matplotlib.backends.backend_tkagg"],
        'packages': ['werkzeug', 'email', 'jinja2.ext'],
        }
    }

data_files = []
data_files.extend(matplotlib.get_py2exe_datafiles())
for dir_image in ['./static', './templates']:
    for root, dirs, files in os.walk(dir_image):
        file_list = []
        if files:
            for filename in files:
                file_list.append(os.path.join(root, filename))
        if file_list:
            data_files.append((root, file_list))
data_files.append(('', ['mm_anywhere.ini']))
print data_files

setup(console=['mm_anywhere.py'],
      options=opts,
      data_files=data_files
    )
