from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):

    @abstractmethod
    def pay(self):
        pass


class Bank(Payment):
    """
        Real object will be of this class.
    """
    def __init__(self):
        self.card = None
        self.account = None

    def __get_account(self):
        self.account = self.card  # Assume card number is account number
        return self.account

    def __has_funds(self):
        print("Bank:: Checking if Account", self.__get_account(), "has enough funds")
        return True

    def set_card(self, card):
        self.card = card

    def pay(self):
        if self.__has_funds():
            print("Bank:: Paying the merchant")
            return True
        else:
            print("Bank:: Sorry, not enough funds!")
        return False


class DebitCard(Payment):
    """
    This is actually a proxy here.
    """
    def __init__(self):
        self.bank = Bank()

    def pay(self):
        card = input("Proxy:: Punch in Card Number: ")
        self.bank.set_card(card)
        return self.bank.pay()


class You:
    def __init__(self):
        print("Let's buy the denim shirt.")
        self.debit_card = DebitCard()
        self.is_purchased = None

    def make_payment(self):
        self.is_purchased = self.debit_card.pay()

    def __del__(self):
        if self.is_purchased:
            print("You:: Wow! Denim shirt is Mine :-)")
        else:
            print("You:: I should earn more :(")


you = You()
you.make_payment()
