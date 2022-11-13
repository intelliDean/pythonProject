import string
"""The function encodes a message by taking input for key, use the key
    to encode the message"""


def encryption_message(message1, key1):
    alphabet = string.ascii_lowercase
    inverse = alphabet[key1:] + alphabet[:key1]
    encode = message1.translate(str.maketrans(alphabet, inverse))
    print(f"{encode.swapcase()}")


def decryption_message(message2, key2):
    alphabet = string.ascii_lowercase
    inverse = alphabet[key2:] + alphabet[:key2]
    decode = message2.translate(str.maketrans(inverse, alphabet))
    print(f"{decode.swapcase()}")


if __name__ == '__main__':
    key = int(input("Enter secret key to encode\n"))
    message = input("Enter message\n")
    encryption_message(message, key)

    key = int(input("\nEnter secret key to encode\n"))
    message = input("\nEnter message\n")
    decryption_message(message, key)


    #print("This is the {} that has the {}".format(message, key))
