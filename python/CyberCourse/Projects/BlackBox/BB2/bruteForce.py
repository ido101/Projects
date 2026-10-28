import hashlib

hashed_number = "6688795677c1c8f2d3cd14b710f60153"
hashlib.md5()
number = "052538"
charset = "0123456789"

for i in charset:
    for j in charset:
        for a in charset:
            for b in charset:
                number = "052538"
                number += i + j + a + b
                hashed_test = hashlib.md5(number.encode()).hexdigest()
                if(hashed_test == hashed_number):
                    print(f"Phone number found: {number}")