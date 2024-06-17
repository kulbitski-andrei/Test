# Создайте класс "Банковский счет" с методами для внесения и снятия денег,
# а также для проверки баланса. Учтите возможность возникновения ошибок при операциях со счетом.

class BankAccount:
    """BankAccount class exemplar represent
    particular account of a particular person
    with possibility to make deposit, withdrawal
    and to check the balance and account status"""

    def __init__(self, person, amount):

        self.person = person
        self.amount = amount
        self.blocked = False

    def deposit(self, money_dep):

        if not self.blocked:
            try:
                self.amount += money_dep
                print("Транзакция завершена успешно!")
            except Exception:
                print("Транзакция прервана, обратитесь к оператору!")
        else:
            print("Невозможно выполнить транзакцию - счет заблокирован")

    def withdraw(self, money_with):

        if not self.blocked:
            try:
                self.amount -= money_with
                print("Транзакция завершена успешно!")
            except Exception:
                print("Транзакция прервана, карта будет заблокирована!")
                self.blocked = True
        else:
            print("Невозможно выполнить транзакцию - счет заблокирован")

    def account_status(self):

        text = (f"Пользователь {self.person}. "
                f"На счету: ${self.amount}. "
                f"Статус счета: {"Активен" if not self.blocked else "Заблокирован"}")
        print(text)
        return text


account_musk = BankAccount("Илон Маск", 500)
assert account_musk.account_status() == ("Пользователь Илон Маск. "
                                         "На счету: $500. Статус счета: Активен")
account_musk.deposit(300)  # + $300
assert account_musk.account_status() == ("Пользователь Илон Маск. "
                                         "На счету: $800. Статус счета: Активен")
account_musk.withdraw(700)  # - $700
assert account_musk.account_status() == ("Пользователь Илон Маск. "
                                         "На счету: $100. Статус счета: Активен")

account_musk.withdraw("Hello world")  # - Невалидный ввод, блокировка счета
assert account_musk.account_status() == ("Пользователь Илон Маск. "
                                         "На счету: $100. Статус счета: Заблокирован")
