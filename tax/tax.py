def tax(price , *,tac_late=1.08):
    print("print:",price,"tac_late:",tac_late)
    tax_price = price * tac_late
    print("tax_price:", tax_price)

tax(100, tac_late=1)