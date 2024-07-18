import re
from functools import reduce


def is_float(v):
    return v.replace('-', '', 1).replace('.', '', 1).isdigit()


def is_int(v):
    return v.replace('-', '', 1).isdigit()


def is_exponential(v):
    lc = v.lower()
    if 'e' not in lc or not is_int(lc[-1]):
        return False
    cleaned = reduce(lambda s, r: s.replace(r, ''), ['-', '.', '+', '', 'e'], lc)
    return cleaned.isdigit()


def format_value(v):
    if v is None:
        return None
    if isinstance(v, list):
        return ', '.join(map(str, v))

    stripped = v.strip() if type(v) is str else v
    if is_int(stripped):
        return int(stripped)
    if is_float(stripped):
        return float(stripped)
    return stripped


def space_ify_string(key):
    if key is None:
        return None
    spacey_values = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?=[A-Z]|$)', key)
    return ' '.join(spacey_values)
