the_matrix = [
    ["7", "i", "3"],
    ["T", "s", "i"],
    ["h", "%", "x"],
    ["i", " ", "#"],
    ["s", "M", " "],
    ["$", "a", " "],
    ["#", "t", "%"],
    [" ", "r", "!"],
]
def crypt(matrix):
    message_decrypted = ""
    matrix_as_list = []
    counter = 0
    while counter < 3:
        for row in matrix:
            matrix_as_list.append(row[counter])
        counter += 1
    print(matrix_as_list)
    for i in matrix_as_list:
        element = i
        if element.isalpha():
            message_decrypted += element
        elif element == " ":
            message_decrypted += element
    print(message_decrypted)
crypt(the_matrix)

