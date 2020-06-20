

def string_compression(string):

    final_length = get_final_length(string)
    if final_length > len(string):
        return string

    new_string = ""
    count = 0
    for index, char in enumerate(string):
        count += 1

        if index + 1 >= len(string) or string[index] != string[1 + index]:
            new_string += char + str(count)

    return new_string




def get_final_length(string):

    count_length = 0
    count = 0
    for index, char in enumerate(string):
        count += 1

        if index + 1 >= len(string) or string[index] != string[1 + index]:
            count_length += 1  + len(str(count_length))
            count = 0
    return count_length


print(string_compression("aaabbbbcddddd"))
