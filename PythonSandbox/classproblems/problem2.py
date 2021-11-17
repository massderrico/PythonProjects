
spam = ["apple", "dog", "chicken", "pig", "cat"]


def pass_list(lists):
    list_len = len(lists)
    last_item = list_len -1
    num = 0
    while num < (last_item): #prints all the items from index [0:-2] with commma between each item
        print (lists[num] + ", ", end="")
        num += 1

    print ("and " + lists[-1]) #prints "and" as well as the last item

pass_list(spam)

