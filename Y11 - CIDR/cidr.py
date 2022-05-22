def integer_to_binary_string(integer, length=None):
    """
    Formats a non-negative integer (e.g. 6, 200, 321,
    0) as a binary string of the given length. The returned
    string when passed to int(..., base=2) should give
    you back the same number.
    
    >>> integer_to_binary_string(16, length=5)
    '10000'
    >>> integer_to_binary_string(132, length=8)
    '10000100'
    >>> integer_to_binary_string(14, length=8)
    '00001110'
    >>> integer_to_binary_string(14)
    '1110'

    hint: lookup string formatting f"{number:b}"
    """
    pass

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
    pass

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
    pass

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
    pass

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
    pass

def get_readable_form_of_binary_ip_address(binary_ip_address):
    """
    Takes a binary IP address such as 00001100000001000000000000000000
    and converts it into a human readable form such as 12.4.0.0

    >>> get_readable_form_of_binary_ip_address("00001100000001000000000000000000")
    '12.4.0.0'
    """
    pass

def get_net_id(ip_address, netmask):
    """
    Takes a human readable IP address, and a human readble
    netmask and returns the human readable network id.
    
    >>> get_net_id("12.4.0.5", "255.254.0.0")
    '12.4.0.0'
    >>> get_net_id("192.168.1.111", "255.255.255.0")
    '192.168.1.0'
    """
    pass

def is_ip_adress_within_network(net_id, ip_address, netmask):
    """
    Checks whether the given IP address is contained within the network
    given by the network id and netmask.

    >>> is_ip_adress_within_network("192.168.1.0", "192.168.1.111", "255.255.255.0")
    True
    >>> is_ip_adress_within_network("12.4.0.5", "12.5.0.0", "255.254.0.0")
    False
    """
    pass

def get_host_id_range(ip_address, netmask):
    """
    Takes a human readable IP address, and a human readble
    netmask and returns the first and last host ids of the network.

    Remember that the network id is used by the network itself -
    not a host! Therefore it should be excluded as part of the range. This
    also applies to the last address which is used as a broadcast id.

    HARD!!!!!

    >>> get_host_id_range("192.168.4.0", "255.255.255.192")
    ['192.168.4.1', '192.168.4.62']
    >>> get_host_id_range("192.168.4.0", "255.255.255.0")
    ['192.168.4.1', '192.168.4.254']
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
  