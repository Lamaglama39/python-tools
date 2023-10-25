import decimal
def tax_calculation():
    price = int(input("price: "))
    tax_late = decimal.Decimal(input("tax_late: "))

    def tax(price, tax_late=1.08):
        print("print:",price,"tac_late:",tax_late)
        tax_price = decimal.Decimal(price * tax_late)
        print("tax_price:", "{:,}".format(tax_price))
    tax(price, tax_late)
# tax_calculation()

from currency_converter import CurrencyConverter
from datetime import date
import math

def currency_exchange():
    c = CurrencyConverter()

    before  = input("為替元の国を入力してください(Default:JPY): ")
    money = input("金額を入力してください(Default:1): ")
    after = input("為替先の国を入力してください(Default:USD): ")

    if  money.isdecimal():
        pass
    else :
        money = 1

    if  before.isupper():
        pass
    else :
        before = "JPY"

    if  after.isupper():
        pass
    else :
        after = "USD"

    choice_date = date(2022, 8, 26)

    def exchange(money, before, after, choice_date):
        answer = (c.convert(money, before, after,choice_date))
        answer3 = math.floor(answer * 10 ** 2) / (10 ** 2)
        print("tax_price:", ("{:,}".format(answer3)))
    exchange(money, before, after, choice_date)

# currency_exchange()