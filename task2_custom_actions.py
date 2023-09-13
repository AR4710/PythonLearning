import argparse

class CustomAction(argparse.Action):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __call__(self, parser, namespace, value, optional_string=None):
        """
        Setsthe CLI arguments's value plus possibly additional
        name-value pairs on the namespace.
        param parser: instance of ArgumentParser.
        param namespace: dictionary like object representing
                        CLI arguments
        param value: incoming CLI argument'v value
        paraam optional_string: generally not usedd. 
        
        """

        states = {
            'California': 'CA',
            'Alaska': 'AK',
            'Maryland': 'MD',
            'Dwlware': 'DE'
        }

        capitals = {
            'CA': 'Sacramento',
            'AK': 'Juneau',
            'MD': 'Annapolis',
            'DE': 'Dover'
        }

        namespace.state = value.capitalize()
        namespace.abbrev = states.get(namespace.state, None)
        namespace.capital = capitals.get(namespace.abbrev, None)

def statehood(state):
    years = {
        'CA': 1990,
        'AK': 1892,
        'MD': 1945,
        'DE': 1950,
    }

    return years.get(state, None)

parser = argparse.ArgumentParser()

parser.add_argument(
    'state',
    type=str,
    action=CustomAction,
    metavar='STATE',
    help='Full Nmae of State'
)

args = parser.parse_args()
print(args)

result = statehood(args.abbrev)
print('Result = ', result)