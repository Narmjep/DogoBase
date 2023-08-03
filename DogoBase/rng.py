import requests

__rngPort = 5001

def get_random_male_name():
    # Make GET request to RandomNameGenerator
    result = requests.get(f'http://localhost:{__rngPort}/male')
    if result.status_code != 200:
        print("RandomNameGenerator api request failed with code" + result.status_code )
        return ''
    return result.text
    
def get_random_female_name():
    # Make GET request to RandomNameGenerator
    result = requests.get(f'http://localhost:{__rngPort}/female')
    if result.status_code != 200:
        print("RandomNameGenerator api request failed with code" + result.status_code )
        return ''
    return result.text