"""
Created by: Soups
Edited last by: Soups
Edited last: 19SEPT21
"""

import pathlib
from github import Github
import requests
import json
import yaml

class Scrape:

    def __init__(self, base_url = "https://gtfobins.github.io", git_url = "https://github.com/GTFOBins/GTFOBins.github.io", filename = "data/data.json") -> None:
        self.base_url = base_url
        self.git_url = git_url 
        self.data_file = filename
        self.git = Github()
        self.repo = self.git.get_repo("GTFOBins/GTFOBins.github.io")
        self.vulns = {
            "base_url": self.base_url,
            "last_updated": "",
            "vulnerable_bins":[

            ]
        }
        data_dir = pathlib.Path(filename[:filename.find("/")])
        data_dir.mkdir(parents=True, exist_ok=True)


    def update(self, force = False):
        if force:
            self.scrape()
            self.save()
            return 0
        data_location = pathlib.Path(self.data_file)
        if data_location.exists():
            with open(self.data_file, 'r') as data_reader:
                data = json.load(data_reader)
                if data["last_updated"] == self.lastUpdated(self.base_url):
                    return 0
        self.scrape()
        self.save()
        return 0


    def lastUpdated(self, url):
        header_request = requests.head(url)
        url_time = header_request.headers['last-modified']
        return url_time


    def scrape(self):
        self.vulns["last_updated"] = self.lastUpdated(self.base_url)
        vuln_files = self.repo.get_contents("_gtfobins")
        vuln_data_formatted = {}
        for each in vuln_files:
            if ".md" in each.name:
                vuln_bin = each.name.replace('.md', '')
                vuln_data_formatted = {
                "name": vuln_bin,
                "bin_url": self.base_url+f"/gtfobins/{vuln_bin}",
                "exploits": []
                }
                raw_vuln_data = requests.get(each.download_url)
                vuln_data = yaml.safe_load(raw_vuln_data.text.replace("---", ""))
                for key, value in vuln_data["functions"].items():
                    specific_exploit = {
                        "function": key,
                        "examples": value
                    }
                    vuln_data_formatted["exploits"].append(specific_exploit)
                self.vulns["vulnerable_bins"].append(vuln_data_formatted)


    def save(self):
        with open(self.data_file, "w") as json_writer:
            json.dump(self.vulns, json_writer, indent=4)


        