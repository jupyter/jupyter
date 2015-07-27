"""Launch the root jupyter command

Alias to jupyter_core
"""

__version__ = '1.0.0'

if __name__ == '__main__':
    from runpy import run_module
    run_module('jupyter_core')
