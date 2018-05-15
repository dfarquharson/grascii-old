get_config().InteractiveShellApp.exec_lines = \
    [
        '%load_ext autoreload',
        '%autoreload 2',
        'from pprint import pprint',
        'import os',
        'import toolz.curried as T',
        'import grascii as G'
    ]
print("---------->>>>>>>>>> CUSTOM CONFIG LOADED <<<<<<<<<<----------")
