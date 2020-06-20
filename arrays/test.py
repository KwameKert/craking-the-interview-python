


def frequencyCount(string):

    holder = {}

    for i in string:
        if holder.get(i) is not None:
            holder[i] = holder.get(i)  + 1
        else:
            holder[i]  = 1

    return holder



print(frequencyCount("hello world"))
