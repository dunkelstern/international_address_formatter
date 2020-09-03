import yaml
import pystache
import os
from pkg_resources import resource_exists, resource_stream

def first(address):
    def _first(content):
        tokens = [token.strip() for token in content.split('||')]
        for t in tokens:
            result = pystache.render(t, address)
            if result.strip() != '':
                return result
        return ''
    return _first

class AddressFormatter():

    def __init__(self, config=None):
        # if no opencage data file is specified in the configuration
        # we fall back to the one included with this package
        if config is None:

            # assume we are in a virtualenv first
            self.model = None
            try:
                if resource_exists('address_formatter', 'worldwide.yml'):
                    self.model = yaml.load(resource_stream('address_formatter', 'worldwide.yml'), Loader=yaml.FullLoader)
            except ModuleNotFoundError:
                pass

            if self.model is None:
                # if not found, assume we have been started from a source checkout
                my_dir = os.path.dirname(os.path.abspath(__file__))
                config = os.path.abspath(os.path.join(my_dir, 'data/worldwide.yml'))

                with open(config, 'r') as fp:
                    self.model = yaml.load(fp, Loader=yaml.FullLoader)

    def format(self, address, country=None):
        search_key = country.upper() if country is not None else 'default'
        fmt = self.model.get(search_key, None)
        if fmt is None:
            fmt = self.model.get('default', None)
        if fmt is None:
            raise RuntimeError("Configuration file for address formatter has no default value!")

        cleaned_address = {}
        for key, value in address.items():
            if value is not None:
                cleaned_address[key] = value

        cleaned_address['first'] = first(cleaned_address)
        return pystache.render(fmt['address_template'], cleaned_address).strip()

    def one_line(self, address, country=None):
        return ", ".join(self.format(address, country=country).split("\n"))