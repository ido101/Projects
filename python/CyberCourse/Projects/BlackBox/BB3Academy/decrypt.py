import base64

def xor_text(text, key):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(text, key)])

key = "this_is_my_cool_nice_key"
secret_data = "IABaLAxaEC1eDQAgXwtf"
dec_64 = base64.b64decode(secret_data).decode()
print(xor_text(dec_64, key)) # Secret Code


#Just a test
for i in xor_text(dec_64, key).encode():
    print(i)
l = [84, 104, 51,95,83,51,99,114,51,116,95,67,48,100,51]
l = "".join([chr(i) for i in l])
print(l)