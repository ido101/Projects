encrypted = "myyux?44=755zsn{jwxny~3ht3nq4hyk2hmfqqjslj292<8:74"
decrypted = ""
for letter in encrypted:
    decrypted += chr(ord(letter) -5)
print(decrypted)