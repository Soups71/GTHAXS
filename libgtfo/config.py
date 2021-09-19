"""
Created by: Soups
Edited last by: Soups
Edited last: 19SEPT21
"""

from termcolor import cprint

# Fancy print
def print_warning(output, newline=True):
    if newline:
        cprint(output, 'red')
    else:
        cprint(output, 'red', end='')
def print_good(output, newline=True):
    if newline:
        cprint(output, 'green')
    else:
        cprint(output, 'green', end='')
def print_update(output, newline=True):
    if newline:
        cprint(output, 'yellow')
    else:
        cprint(output, 'yellow', end='')

