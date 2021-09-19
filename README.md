# GTHAXS

This purpose behind this project was to create a command line interface for the popular website [GTFObins](https://gtfobins.github.io/)

## Usage:

```
usage: gthaxs.py [-h] -b BINARY [-f FUNCTION] [-u] [-e] [-s] [-lf] [-d]

optional arguments:
  -h, --help            show this help message and exit
  -b BINARY, --binary BINARY
                        Specify Binary Name
  -f FUNCTION, --function FUNCTION
                        Search for specific function to exploit
  -u, --update          Force update of local data
  -e, --exist           Check if binary exists. Does not return functions that can be exploited
  -s, --search          Returns binarys that are close to the given binary string
  -lf, --list_functions
                        List functions availible for specific binary
  -d, --dont_update     Skip updating local data even if new records found
```

## Thank You
I would like to thank the people over at [GTFObins](https://gtfobins.github.io/). Without them publicly providing this data I would not have been able to make this command line tool. Please make sure to check them out!!!