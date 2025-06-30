from app.calculations import add, subtract, multiply, divide, BankAccount, InsufficientFunds
import pytest

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)


@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 5),
    (7,1, 8),
    (12, 4, 16)
])


def test_add(num1, num2, expected):
    print("Testing add function")    
    assert add(num1, num2) == expected
    assert add(num1, num2) == expected
    assert add(num1, num2) == expected

def test_subtract():
    print("Testing subtract function")    
    assert subtract(5, 3) == 2
    assert subtract(1, 0) == 1
    assert subtract(1, 2) == -1

def test_multiply():
    print("Testing multiply function")    
    assert multiply(5, 3) == 15
    assert multiply(1, 0) == 0
    assert multiply(1, 2) == 2

def test_divide():
    print("Testing divide function")    
    assert divide(15, 3) == 5
    assert divide(2, 1) == 2
    assert divide(1, 2) == 0.5


def test_bank_set_initial_amount():
    bank_account  = BankAccount(50)
    assert bank_account.balance == 50

def test_bank_set_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0

def test_withdraw(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 30

def test_deposit(bank_account):
    bank_account.deposit(80)
    assert bank_account.balance == 130

def test_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance, 4) == 55

@pytest.mark.parametrize("deposited, withdraw, expected", [
    (500, 200, 300),
    (700, 200, 500),
    (1200, 400, 800),
])


def test_bank_transaction(zero_bank_account, deposited, withdraw, expected): 
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdraw)
    assert zero_bank_account.balance == expected


def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(200)
        assert bank_account.balance