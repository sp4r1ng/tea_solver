import sys
from ctypes import *

def encipher(v, k):
    y = c_uint32(v[0])
    z = c_uint32(v[1])
    sum = c_uint32(0)
    delta = 0x9e3779b9
    n = 32
    w = [0, 0]

    while n > 0:
        sum.value += delta
        y.value += (z.value << 4) + k[0] ^ z.value + sum.value ^ (z.value >> 5) + k[1]
        z.value += (y.value << 4) + k[2] ^ y.value + sum.value ^ (y.value >> 5) + k[3]
        n -= 1

    w[0] = y.value
    w[1] = z.value
    return w

def decipher(v, k):
    y = c_uint32(v[0])
    z = c_uint32(v[1])
    sum = c_uint32(0xc6ef3720)
    delta = 0x9e3779b9
    n = 32
    w = [0, 0]

    while n > 0:
        z.value -= (y.value << 4) + k[2] ^ y.value + sum.value ^ (y.value >> 5) + k[3]
        y.value -= (z.value << 4) + k[0] ^ z.value + sum.value ^ (z.value >> 5) + k[1]
        sum.value -= delta
        n -= 1

    w[0] = y.value
    w[1] = z.value
    return w

def main():
    print("TEA Encryption/Decryption Tool")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Choose an option (1/2): ")

    if choice not in ['1', '2']:
        print("Invalid choice. Exiting.")
        return

    try:
        key = list(map(int, input("Enter 4 integer keys separated by spaces: ").split()))
        if len(key) != 4:
            print("Key must contain exactly 4 integers.")
            return

        v = list(map(int, input("Enter 2 integer values separated by spaces: ").split()))
        if len(v) != 2:
            print("Input must contain exactly 2 integers.")
            return

        if choice == '1':
            result = encipher(v, key)
            print(f"Encrypted values: {result}")
        else:
            result = decipher(v, key)
            print(f"Decrypted values: {result}")

    except ValueError:
        print("Invalid input. Please enter integers only.")

if __name__ == "__main__":
    main()