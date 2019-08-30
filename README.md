# Raincast

_A command line tool that takes a city name as a parameter and displays if it’s going to rain today using MetaWeather (https://www.metaweather.com/api/)_


Installation is done using pip. Python3 is needed:

```
pip install -e git+ssh://git@github.com/slashdevsda/raincaster.git#egg=raincast
```

# Help

```
$ raincastcli -h
usage: raincast [-h] [-m] [-e] city

positional arguments:
  city                  is it going to rain in this city today?

optional arguments:
  -h, --help            show this help message and exit
  -m                    machine readable and predictible output
  -e, --exit-with-error
                        exits with error (1) if it's raining. Handy when used
                        in conjuction with `set -e`, disallowing scripts to
                        run on a rainy day
```

# Exit status:

- 0: everything went fine
- 1: (implies -e) it's raining
- 2: city not found
- 3: network error
- 4: unhandled error
