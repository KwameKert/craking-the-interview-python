#urlify string

#count number of spaces
def count_spaces(string, length):
    spaces = 0
    for i in range(0, length):
        if string[i] == ' ':
            spaces += 1
    return spaces



def urlify(string, truelength):
    spaces = count_spaces(string, truelength)
    indexCount = truelength + (spaces*2)

    count = truelength -1
    string = list(string)
    while count >= 0:
        if string[indexCount -1] == ' ':
            string[indexCount -1] = '0'
            string[indexCount -2] = '2'
            string[indexCount -3] = '%'
            count -= 1
            indexCount -=1
            print(string)
        else:
            string[indexCount -1] =  string[count]
            indexCount -= 1
            count -=1
    return "".join(string)

print(urlify('Mr John Smith    ',13))
