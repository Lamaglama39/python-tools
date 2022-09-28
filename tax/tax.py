import decimal

price = int(input("price: "))
tax_late = decimal.Decimal(input("tax_late: "))

def tax(price, tax_late=1.08):
    print("print:",price,"tac_late:",tax_late)
    tax_price = decimal.Decimal(price * tax_late)
    print("tax_price:", "{:,}".format(tax_price))

tax(price, tax_late)