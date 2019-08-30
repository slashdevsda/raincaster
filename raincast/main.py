import requests
import argparse
import logging
from datetime import datetime
#from typing import List, Dict, Any
logger = logging.getLogger(__name__)

# from https://www.metaweather.com/api/
RAINY_STATE = {
    'hr': 'heavy rain',
    'lr': 'light rain',
    's': 'showers',
}

def display_forecast(args, forecast):


    today = datetime.now().strftime('%Y-%m-%d')
    today_fcast = next(filter(lambda x: x['applicable_date'] == today, forecast))


    maybe_rain = RAINY_STATE.get(today_fcast['weather_state_abbr'])
    if not maybe_rain:
        if args.m:
            print('no')
        else:
            print(f'It\'s not going to rain in {args.city}')
        exit(0)
    else:
        if args.m:
            print('yes')
        else:        
            print(f'It\'s going to rain in {args.city}, expect {maybe_rain}.')
        if args.exit_with_error:
            exit(1)
        exit(0)



def main():
    parser = argparse.ArgumentParser(prog='raincast')
    parser.add_argument('city', help='is it going to rain in this city today?')
    parser.add_argument('-m', action='store_true',
                        help='machine readable and predictible output')
    parser.add_argument('-e', '--exit-with-error', action='store_true', help=(
        'exits with error (1) if it\'s raining. '
        'Handy when used in conjuction with `set -e`, '
        'disallowing scripts to run on a rainy day'))
    args = parser.parse_args()
    session = requests.Session()

    try:
        r = session.get(
            f'https://www.metaweather.com/api/location/search/?query={args.city}')

        match = r.json()
        if not len(match):
            print(f'city {args.city} not found on MetaWeather')
            exit(2)
        woeid = match[0]['woeid']

        r = session.get(
            f'https://www.metaweather.com/api/location/{woeid}/')
        forecast = r.json()
        display_forecast(args, forecast['consolidated_weather'])


    except requests.RequestException:
        logger.exception('Network/http error')
        exit(3)
    #
    
if __name__ == '__main__':
    main()
