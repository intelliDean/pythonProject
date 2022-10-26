def enter_password():
    for n in range(3):
        password = input("Password\n")
        if password == "I<3Bieber":
            print("Correct! Access granted")
            break
        print("Password is incorrect. Access Denied\n")
    else:
        print("Suspicious activity. The authorities have been alerted.")


if __name__ == '__main__':
    enter_password()
