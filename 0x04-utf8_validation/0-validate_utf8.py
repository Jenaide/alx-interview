#!/usr/bin/python3
"""
UTF-8 method
"""



def validUTF8(data):
    """
    method that determines of a given data set represents 
    a valid UTF-8 encoding.
    """
    bytes_to_follow = 0 # Number of bytes required to complete a character

    for byte in data:
        # converts the bytes to binary string and remove '0b' prefix
        bins = format(byte, '08b')

        if bytes_to_follow == 0:
            if bins.startswith('0'):
                continue
            elif bins.startswith('110'):
                bytes_to_follow = 1
            elif bins.startswith('1110'):
                bytes_to_follow = 2
            elif bins.startswith('11110'):
                bytes_to_follow = 3
            else:
                return False
        else:
            if not bins.startswith('10'):
                return False
            bytes_to_follow -= 1

    return bytes_to_follow == 0
