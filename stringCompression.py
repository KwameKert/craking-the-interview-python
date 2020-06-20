
def string_compression(string):

    #define hashmap
    holder = {}
    #define new string
    new_string = ""

    #create a  frequency counter
    for item in string:
        holder[item] = holder.get(item, 0)+1


    #loop through map
    for item in holder:
        new_string += item+ str(holder.get(item))

    return new_string if len(new_string) < len(string) else string

print(string_compression("aabbccd"))
