def balance_check(name: str, balance: float) -> None:
    # name is defined as str, balance is defined as float while the function returns None
    print(f"Hello {name}, your balance is {balance}")


if __name__ == '__main__':
    balance_check(name="Dean", balance=230009.03)
