import os

try:
  user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
except KeyError:
  user_paths = []


import os


user_path = os.path.join(user_path, '', ':')