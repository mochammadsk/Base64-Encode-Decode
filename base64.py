import time
import base64

# Procedure header


def header():
    print(43*'=')
    print("|          Base64 Encode-Decode           |")
    print(43*'=')

# Procedure footer


def footer():
    print(43*'=')
    print("|             @mochammadsk_               |")
    print(43*'=')

# Procedure encoding base64


def encode():
    print("+           Type Plaintext Here           +")
    print(43*'-')
    sample_string = input("")
    sample_string_bytes = sample_string.encode("ascii")

    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")

    print(43*'-')

    start_time = time.time()
    print(f"Ciphertext : {base64_string}")
    end_time = time.time()

    time_lapsed = end_time - start_time
    time_convert(time_lapsed)

# Procedure decoding base64


def decode():
    print("+          Type Ciphertext Here           +")
    print(43*'-')
    base64_string = input("")
    base64_bytes = base64_string.encode("ascii")

    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")

    print(43*'-')

    start_time = time.time()
    print(f"Plaintext  : {sample_string}")
    end_time = time.time()

    time_lapsed = end_time - start_time
    time_convert(time_lapsed)

# Procedure perhitungan waktu


def time_convert(sec):
    sec = sec % 60
    print("Time (s)   : {0}".format(round(sec, 6)))

# Procedur menampilkan pilihan menu


def menu():
    print('''
1. Encode
2. Decode
    ''')


def nope():
    print("            No Options Here!!         ")


header()
print("+                  MENU                   +")
print(43*'-')
menu()

# Input pilihan menu
print(43*'=')
choice = int(input("Choose Menu : "))
print(43*'=')

# Switchcase dari input menu
menus = [encode, decode, nope, nope, nope, nope, nope, nope, nope]
operation = menus[choice-1]()
print(operation)

footer()
