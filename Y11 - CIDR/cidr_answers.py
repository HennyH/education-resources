def integer_to_binary_string(integer, length=None):
    """
    Formats a non-negative integer (e.g. 6, 200, 321,
    0) as a binary string of the padded up to the given length with 0s.
    The returned string when passed to int(..., base=2) should give
    you back the same number.
    
    >>> integer_to_binary_string(16, length=5)
    '10000'
    >>> integer_to_binary_string(132, length=8)
    '10000100'
    >>> integer_to_binary_string(14, length=8)
    '00001110'
    >>> integer_to_binary_string(14)
    '1110'
    """
    if length is None:
        return f"{integer:b}"
    return f"{integer:0={length}b}"

def split_readable_ip_address(readable_ip_address):
    """
    Takes a human readable IP such as 10.15.100.2 and
    splits it up by the period into an array of 4 numbers.

    >>> split_readable_ip_address("10.15.100.2")
    [10, 15, 100, 2]
    >>> split_readable_ip_address("0.0.50.0")
    [0, 0, 50, 0]
    >>> split_readable_ip_address("192.168.0.1")
    [192, 168, 0, 1]
    """
    return list(map(int, readable_ip_address.split(".")))


def get_binary_form_of_readable_ip_address(readable_ip_address):
    """
    Takes a human readable IP address such as 10.15.100.2
    converts it into a binary string.

    Hint: if you've completed the split_readable_ip_address
    and integer_to_binary_string functions then you should use
    them here! A for loop, some function calls and a string con-
    catenation and you'll be done!
    
    >>> get_binary_form_of_readable_ip_address("12.4.0.0")
    '00001100000001000000000000000000'
    >>> get_binary_form_of_readable_ip_address("255.254.0.0")
    '11111111111111100000000000000000'
    """
    binary_ip_address = ""
    for segment in split_readable_ip_address(readable_ip_address):
        binary_ip_address += integer_to_binary_string(segment, length=8)
    return binary_ip_address

def split_binary_ip_address(binary_ip_address):
    """
    Takes a binary IP address such as 00001100000001000000000000000000
    and splits it up into 8 bit long strings, returning all the 8 bit
    long strings in a list.
    
    >>> split_binary_ip_address("00001100000001000000000000000000")
    ['00001100', '00000100', '00000000', '00000000']
    >>> split_binary_ip_address("11111111111111100000000000000000")
    ['11111111', '11111110', '00000000', '00000000']
    """
    return [binary_ip_address[i:i+8] for i in range(0, len(binary_ip_address), 8)]

def parse_binary_string_as_integer(binary_string):
    """
    Takes a binary string such as 0010 or 111 or 101, etc...
    and parses it as an integer.
    
    Hint hint: int(x, base=b)

    >>> parse_binary_string_as_integer("111")
    7
    >>> parse_binary_string_as_integer("0")
    0
    >>> parse_binary_string_as_integer("1")
    1
    >>> parse_binary_string_as_integer("001101")
    13
    """
    return int(binary_string, base=2)

def get_readable_form_of_binary_ip_address(binary_ip_address):
    """
    Takes a binary IP address such as 00001100000001000000000000000000
    and converts it into a human readable form such as 12.4.0.0

    >>> get_readable_form_of_binary_ip_address("00001100000001000000000000000000")
    '12.4.0.0'
    """
    binary_ip_addr_segments = split_binary_ip_address(binary_ip_address)
    decimal_ip_addr_segments = [str(parse_binary_string_as_integer(bs)) for bs in binary_ip_addr_segments]
    return ".".join(decimal_ip_addr_segments)

def get_net_id(ip_address, netmask):
    """
    Takes a human readable IP address, and a human readble
    netmask and returns the human readable network prefix.
    
    >>> get_net_id("12.4.0.5", "255.254.0.0")
    '12.4.0.0'
    >>> get_net_id("192.168.1.111", "255.255.255.0")
    '192.168.1.0'
    """
    binary_ip_address = get_binary_form_of_readable_ip_address(ip_address)
    ip_address_number = parse_binary_string_as_integer(binary_ip_address)
    binary_netmask = get_binary_form_of_readable_ip_address(netmask)
    netmask_number = parse_binary_string_as_integer(binary_netmask)
    net_id_number = ip_address_number & netmask_number
    binary_net_id = integer_to_binary_string(net_id_number, length=32)
    return get_readable_form_of_binary_ip_address(binary_net_id)

def is_ip_adress_within_network(net_id, ip_address, netmask):
    """
    Checks whether the given IP address is contained within the network
    given by the network prefix and netmask.

    >>> is_ip_adress_within_network("192.168.1.0", "192.168.1.111", "255.255.255.0")
    True
    >>> is_ip_adress_within_network("12.4.0.5", "12.5.0.0", "255.254.0.0")
    False
    """
    binary_net_id = get_binary_form_of_readable_ip_address(net_id).rstrip("0")
    binary_ip_address = get_binary_form_of_readable_ip_address(ip_address)
    return binary_ip_address.startswith(binary_net_id)

def get_host_id_range(ip_address, netmask):
    """
    Takes a human readable IP address, and a human readble
    netmask and returns the first and last host ids of the network.

    Remember that the network prefix/id is used by the network itself -
    not a host! Therefore it should be excluded as part of the range. This
    also applies to the last address which is used as a broadcast id.

    HARD!!!!!

    >>> get_host_id_range("192.168.4.0", "255.255.255.192")
    ['192.168.4.1', '192.168.4.62']
    >>> get_host_id_range("192.168.4.0", "255.255.255.0")
    ['192.168.4.1', '192.168.4.254']
    """
    net_id = get_net_id(ip_address, netmask)
    binary_netmask_len = len(get_binary_form_of_readable_ip_address(netmask).rstrip("0"))
    lower_binary_ip = get_binary_form_of_readable_ip_address(net_id)
    # this could be simplified to: ip_address | (~ netmask) but python doesn't support unsigned integer bitwise operations
    upper_binary_ip = lower_binary_ip[:binary_netmask_len] + ((32 - binary_netmask_len) * "1")
    lower_ip_number = parse_binary_string_as_integer(lower_binary_ip)
    upper_ip_number = parse_binary_string_as_integer(upper_binary_ip)
    lower_ip = get_readable_form_of_binary_ip_address(integer_to_binary_string(lower_ip_number + 1, length=32))
    upper_ip = get_readable_form_of_binary_ip_address(integer_to_binary_string(upper_ip_number - 1, length=32))
    return [lower_ip, upper_ip]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
  