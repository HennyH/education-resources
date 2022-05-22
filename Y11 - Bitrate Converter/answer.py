PREFIXES = {
    "": 1,
    "K": 10 ** 3,
    "M": 10 ** 6,
    "G": 10 ** 9
}

BLOBS = {
    "b": 1,
    "B": 8
}

UNITS_TO_DECIMAL = {}
for prefix, decimal in PREFIXES.items():
    for blob, byte_count in BLOBS.items():
        UNITS_TO_DECIMAL[f"{prefix}{blob}/s"] = decimal * byte_count

def bitrate_convert(value: float, from_units: str, to_units: str) -> float:
    from_multiple = UNITS_TO_DECIMAL.get(from_units, 1)
    to_multiple = UNITS_TO_DECIMAL.get(to_units, 1)
    return value * from_multiple / to_multiple

def get_si_prefix(unit: str) -> int:
    if unit.startswith("G"):
        return 10 ** 9
    elif unit.startswith("M"):
        return 10 ** 6
    elif unit.startswith("K"):
        return 10 ** 3
    return 1

def get_bits_in_unit(unit: str) -> int:
    """
    Returns the number of bits (8 or 1) based upon wether the unit is expressed in b/s or B/s.
    """
    if unit.endswith("B/s"):
        return 8
    return 1

def bitrate_convert(value: float, from_units: str, to_units: str) -> float:
    from_multiple = get_si_prefix(from_units) * get_bits_in_unit(from_units)
    to_multiple = get_si_prefix(to_units) * get_bits_in_unit(to_units)
    return value * (from_multiple / to_multiple)
