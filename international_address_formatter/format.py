import yaml
import pystache
import os


def first(address):
    def _first(content):
        tokens = [token.strip() for token in content.split("||")]
        for t in tokens:
            result = pystache.render(t, address)
            if result.strip() != "":
                return result
        return ""

    return _first


class AddressFormatter:
    def __init__(self, config=None):
        # if no opencage data file is specified in the configuration
        # we fall back to the one included with this package
        if config is None:
            # if not found, use a relative path definition
            my_dir = os.path.dirname(os.path.abspath(__file__))
            config = os.path.abspath(os.path.join(my_dir, "data/worldwide.yml"))

        with open(config, "r", encoding="utf-8") as fp:
            self.model = yaml.load(fp, Loader=yaml.FullLoader)

    def format(self, address, country=None):
        search_key = country.upper() if country is not None else "default"
        fmt = self.model.get(search_key, None)
        if fmt is None:
            fmt = self.model.get("default", None)
        if fmt is None:
            raise RuntimeError(
                "Configuration file for address formatter has no default value!"
            )

        # Some country configurations redirect to other countries but
        # change the country name in the process:
        use_country = fmt.get("use_country")
        if use_country is not None:
            country = fmt.get("change_country")
            if country is not None:
                address["country"] = country
            return self.format(address, country=use_country)

        cleaned_address = {}
        for key, value in address.items():
            if value is not None:
                cleaned_address[key] = value

        cleaned_address["first"] = first(cleaned_address)
        return pystache.render(fmt["address_template"], cleaned_address).strip()

    def one_line(self, address, country=None):
        return ", ".join(self.format(address, country=country).split("\n"))
