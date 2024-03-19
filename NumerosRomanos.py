def DecimalARomano(decimal):
    NumeroRomanos = { 1: "I", 5: "V", 10: "x", 50:"L", 100: "C", 500:"D", 1000:"M"}
    Romano = ""

    for value, numeral in sorted(NumeroRomanos.items(), reverse=True):
        while decimal >= value:
            Romano += numeral
            decimal -= value

    return Romano