import unittest
import hello
import ps1


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")
        self.assertNotEqual(hello.hello(), "bye world")

    # def test_sin(self):
    #     self.assertEqual(hello.sin(0), 0)
    #     self.assertEqual(hello.sin(1), 0.8414709848078965)

    # def test_cos(self):
    #     self.assertEqual(hello.cos(0), 1)
    #     self.assertEqual(hello.cos(1), 0.5403023058681398)

    # def test_tan(self):
    #     self.assertEqual(hello.tan(0), 0)
    #     self.assertEqual(hello.tan(1), 1.5574077246549023)

    # def test_cot(self):
    #     self.assertEqual(hello.cot(0), float("inf"))
    #     self.assertEqual(hello.cot(1), 0.6420926159343306)


class TestProblem1(unittest.TestCase):
    def test_withdraw(self):
        account = ps1.BankAccount(100, "alicia", "123456789")
        account.withdraw(40)  # withdraw 50 and check if the new balance is 50
        self.assertEqual(account.balance, 60)

        account.withdraw(200)  # withdraw 200 and check if the balance remains the same
        self.assertEqual(account.balance, 60)

        account.withdraw(-10)  # withdraw -10 and check if the balance remains the same
        self.assertEqual(account.balance, 60)

        account.withdraw("a")  # withdraw a and check if the balance remains the same
        self.assertEqual(account.balance, 60)

    def test_deposit(self):
        account = ps1.BankAccount(1000, "alicia", "123456789")
        account.deposit(500)
        self.assertEqual(account.balance, 1500)

        account.deposit(-100)
        self.assertEqual(account.balance, 1500)

        account.deposit("a")
        self.assertEqual(account.balance, 1500)

        account.deposit(200)
        self.assertEqual(account.balance, 1700)

    def test_balance(self):
        account = ps1.BankAccount(100, "alicia", "123456789")
        self.assertEqual(account.get_balance(), 100)

        account.deposit(50)
        self.assertEqual(account.get_balance(), 150)

        account.withdraw(30)
        self.assertEqual(account.get_balance(), 120)

        account.withdraw(500)
        self.assertEqual(account.get_balance(), 120)


if __name__ == "__main__":
    unittest.main()
