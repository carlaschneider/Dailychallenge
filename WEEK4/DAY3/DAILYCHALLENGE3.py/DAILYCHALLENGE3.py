message = input("enter your message")
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
c = input("Do you want to crypt or decrypts your message ? (crypt or decrypts)")
messageC = ''
if c == "crypt":
    for i in message:
        for j in alphabet:
            if i == j:
                k = (alphabet.index(j) - 3)
                messageC += alphabet[k]


elif c == "decrypts":
    for i in message:
        for j in alphabet:
            if i == j:
                k = (alphabet.index(j) + 3)%26
                messageC += alphabet[k]


else:
    print("i don't understand")

print(messageC)