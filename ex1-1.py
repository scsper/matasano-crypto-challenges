# Convert hex to base64
import binascii

given_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

binary = binascii.unhexlify(given_string)
base64 = binascii.b2a_base64(binary)

print base64
