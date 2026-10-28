text = "Ido Cohen"
key = 5
print(text)
text = [ord(char) for char in text]
print(text)
text = [str(char ^ key) for char in text]
print(text)
text = ' '.join(text)
print(text)
result = []
tmp = ""
for char in text:
    if char not in [" "]:
        tmp += char
    else:
        result.append(tmp)
        tmp = ""
result.append(tmp)
text = result.copy()
text = [int(char) ^ key for char in text]
print(text)
text = [chr(char) for char in text]
print(text)
text = ''.join(text)
print(text)