import argparse


class CustomAction(argparse.Action):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __Call__(self, parser, namespace, value, optional_string=None):
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