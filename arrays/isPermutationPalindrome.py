

def isPermutationOfPalindrome(string):
    string = string.lower()
    table = frequencyCounter(string)
    return checkTable(table)



def checkTable(table):
    found = 0
    for item in table:
        if table.get(item)%2 == 1:
            if found  >  1:
                return False
            else:
                found += 1;
    return True




def frequencyCounter(string):
    holder = {}
    for i in string:
        holder[i] = holder.get(i, 0)+1

    return holder



print(isPermutationOfPalindrome("Tct Coa"))
