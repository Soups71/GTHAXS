"""
Created by: Soups
Edited last by: Soups
Edited last: 19SEPT21
"""
import json
from libgtfo.config import *

class Search():
    def __init__(self, path = "data/data.json") -> None:
        self.base_path = path
        with open(self.base_path, 'r') as reader:
            self.data = json.load(reader)

    def getExploits(self, bin_name):
        bin_name = bin_name.lower()
        for each_bin in self.data["vulnerable_bins"]:
            if each_bin["name"].lower() == bin_name:
                return each_bin["exploits"], each_bin["bin_url"]
        return [{"error": "Exploit for Binary not found"}] , "" 

    def craftString(self, bin_name, exploit, bin_url):
        print(f"Binary Name: ", end="")
        print_update(f"{bin_name}\n")
        for each in exploit:
            print(f"Type of Exploit: ", end="")
            print_update(f"{each['function']}")
            for example in each["examples"]:
                if "description" in example:
                    cleaned = example["code"].strip().replace('\n', '\n\t\t')
                    print(f"\tDescription: ", end="")
                    print_update(f"{example['description']}")
                    print("\tExample:")
                    print_good(f"\t\t{cleaned}\n")
                else:
                    cleaned = example["code"].strip().replace('\n', '\n\t\t')
                    print(f"\tExample: ")
                    print_good(f"\t\t{cleaned}\n")
        print_update(f"Find more information at: {bin_url}")
        return 0
            

    def dispExploits(self, bin_name=None, function=None) -> int:
        if bin_name is not None:
            bin_exploit, bin_url = self.getExploits(bin_name)
            for each in bin_exploit:
                if "error" in each:
                    print_warning(f"No record was found for {bin_name}")
                    return 1
            if function is None:
                self.craftString(bin_name, bin_exploit, bin_url )
                return 0
            else:
                for functions in bin_exploit:
                    try:
                        if(functions.get("function") == function):
                            self.craftString(bin_name, [functions], bin_url)
                            return 0
                    except Exception as e:
                        print(e)
                        return -1
        else:
            return -1

    def dispFunctions(self, bin_name=None):
        if bin_name is not None:
            bin_exploit, bin_url = self.getExploits(bin_name)
            for each in bin_exploit:
                if "error" in each:
                    print_warning(f"No record was found for {bin_name}")
                    return 1
            print(f"Functions of {bin_name}: ")
            for each in bin_exploit:
                print_good(f'\t{each["function"]}')
        else:
            return -1
        print_update(f"Find more information at: {bin_url}")
        return 0
    
    def exist(self, bin_name=None):
        if bin_name is not None:
            bin_exploit, bin_url = self.getExploits(bin_name)
            if "error" in bin_exploit[0]:
                print_warning(f"No record was found for {bin_name}")
                return 1
            else:
                print_good(f"A record was found for {bin_name}")
        else:
            return -1
        return 0
    
    def search(self, bin_name=None):
        possible_match = []
        if bin_name is not None:
            for each_bin in self.data["vulnerable_bins"]:
                if bin_name.lower() in each_bin["name"].lower():
                    possible_match.append(each_bin["name"])
        if len(possible_match)>0:
            print("Possible Matches:")
            for each in possible_match:
                print_good(f"\t{each}")
        else:
            print_warning(f"No poossible matches was found for {bin_name}")
        return 0

            

        