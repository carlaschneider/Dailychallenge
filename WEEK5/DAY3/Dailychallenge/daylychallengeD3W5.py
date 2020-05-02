car = {
        "à": "a",
        "ä": "a",
        "â": "a",
        "ç": "c",
        "é": "e",
        "è": "e",
        "ë": "e",
        "ï": "i",
        "ô": "o",
        "ù": "u",
        "ü": "u",
        "û": "u",
        " ": "",
        "-": "",
        ",": "",
        "'": "",
        "?": "",
        "!": "",
        ".": ""
    }


class palindrome:
    def __init__(self, chain):
        self.chain = chain

    def checking_chain(self):
        a = self.chain.lower()
        for key, value in car.items():
            a = a.replace(key, value)
        return str(a)

    def check(self):
        pal = True
        a = palindrome(self.chain).checking_chain()

        for i in range(len(a)//2):
            if a[i] != a[-i-1]:
                pal = False
                break

        if pal == True:
            print("It's a  palindrome !")
        else:
            print("It's not a palindrome...")

palindrome(input("Enter a string to check if it's or not a palindrome: ")).check()