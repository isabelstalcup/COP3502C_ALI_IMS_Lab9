## Isabel Stalcup, Alessandro Inverardi

# encode
def encode(password):
    encoded = ""
    for digit in password:
        digit = (int(digit) + 3) % 10
        encoded += str(digit)
    return encoded

#decode


def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        op = int(input("Please enter an option: "))

        if op == 1:
            password = input("Please enter a password: ")
            encoded = encode(password)
            print("Your password has been encoded and stored!\n")

        elif op == 2:
            if encoded != "":
                # decoded = decode(encoded)
                print(f"The encoded pass is {encoded}, and the original password is {decoded}.")
            else:
                print("There is no password to be decoded.")

        elif op == 3:
            break

        else:
            continue

if __name__ == "__main__":
    main()