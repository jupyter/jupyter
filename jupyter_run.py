"""Launch the root jupyter command

Alias to jupyter_core
"""

__version__ = '1.0.0'

def main():
    from runpy import run_module
    run_module('jupyter_core')

if __name__ == '__main__':
    main()
