def fizz_buzz(input):
    divs_by_3 = input % 3 == 0
    divs_by_5 = input % 5 == 0
    if divs_by_3 and not divs_by_5:
        return "fizz"
    elif not divs_by_3 and divs_by_5:
        return "buzz"
    elif divs_by_5 and divs_by_3:
        return "fizzbuzz"
    return input


print(fizz_buzz(7))
