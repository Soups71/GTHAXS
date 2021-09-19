"""
Created by: Soups
Edited last by: Soups
Edited last: 19SEPT21
"""

import libgtfo as gtfo

if __name__ == "__main__":
    args = gtfo.Start()
    git_scraper = gtfo.Scrape()
    if not args.options.not_update:
        git_scraper.update(args.options.update)
    search_engine = gtfo.Search()
    if args.options.list_functions:
        search_engine.dispFunctions(args.options.binary)
    elif args.options.exist:
        search_engine.exist(args.options.binary)
    elif args.options.search:
        search_engine.search(args.options.binary)
    elif args.options.function is None:
        search_engine.dispExploits(args.options.binary)
    else:
        search_engine.dispExploits(args.options.binary, args.options.function)