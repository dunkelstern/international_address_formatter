# International Address formatter

This is a address formatter that can format addresses in multiple formats that are common
in different countries.

For formatting the addresses the `worldwide.yml` from [OpenCageData address-formatting repository](https://github.com/OpenCageData/address-formatting) is used to format the address according to customs in the country that is been encoded.

See `README.md` in the [repository](https://github.com/dunkelstern/international_address_formatter) for more information.

## Changelog

### v1.0.2

- Update `worldwide.yml` data file (thanks @kimryan)

### v1.0.1

- Bugfix: Package did not find its data-file because of wrong path calculation

### v1.0

- Initial release, split out of the osmgeocoder project

## API documentation

The complete project contains actually only one class:

### `AddressFormatter`

Publicly accessible method prototypes are:

```python
def __init__(self, config=None):
    pass

def format(self, address, country=None):
    pass

def one_line(self, address, country=None):
    pass
```

#### `__init__`

Initialize the address formatter
- `config`: (optional) override default config file to use for the address formatter, defaults to config file included in this package

#### `format`

Format an address in the default layout used in the specified country. Return value may contain line breaks.
- `address`: Dictionary that contains the address parts, see below for recognized keys
- `country`: Country code of the formatting template to use

Recognized keys in `address`:
- `attention`
- `house`
- `road`
- `house_number`
- `postcode`
- `city`
- `town`
- `village`
- `county`
- `state`
- `country`
- `suburb`
- `city_district`
- `state_district`
- `state_code`
- `neighbourhood`

#### `one_line`

Works the same as `format` but returns a single line of text.
