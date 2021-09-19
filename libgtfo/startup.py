"""
Created by: Soups
Edited last by: Soups
Edited last: 19SEPT21
"""

import argparse

class Start():
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-b',
                                '--binary',
                                dest='binary', 
                                help='Specify Binary Name',
                                required=True)
        self.parser.add_argument('-f',
                                '--function',
                                dest='function', 
                                help='Search for specific function to exploit')
        self.parser.add_argument('-u', 
                                '--update', 
                                action='store_true',
                                dest='update', 
                                help='Force update of local data')
        self.parser.add_argument('-e', 
                                '--exist', 
                                action='store_true',
                                dest='exist', 
                                help='Check if binary exists. Does not return functions that can be exploited')
        self.parser.add_argument('-s', 
                                '--search', 
                                action='store_true',
                                dest='search', 
                                help='Returns binarys that are close to the given binary string')
        self.parser.add_argument('-lf', 
                                '--list_functions', 
                                action='store_true',
                                dest='list_functions', 
                                help='List functions availible for specific binary')
        self.parser.add_argument('-d', 
                                '--dont_update', 
                                action='store_true',
                                dest='not_update', 
                                help='Skip updating local data even if new records found')
        self.parser.set_defaults(update = False, exists = False, search = False, list_functions = False, not_update = False)
        self.options = self.parser.parse_args()