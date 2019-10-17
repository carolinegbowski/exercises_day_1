
this_list = [1, 2, ['jeff', 'tom'], [42, ['billy', 'jason']]]

def crack_this_list(any_list):
    for i in any_list: 
        if type(i) is list: 
            for j in i: 
                if type(j) is list: 
                    for k in j:
                        if type(k) is list: 
                            for l in k: 
                                print(l)
                        else:
                            print(k)
                else:
                    print(j)
        else:
            print(i)

crack_this_list(this_list)

# while True: ???????
#     if i in any_list is list: 
#         for j in i: 
#             print(j)
#     else:
#         print(i)
# can't you do a while loop to see while NOT list, print i, but if list, print each item of list?

# can do recursively or with a stack 
# recursive -- function that calls itslef (breaks into smaller units and calls on itself)

def unspool_list(item): 
    if type(item) != list: 
        return str(item)
    return "\n".join(unspool_list(element) for element in item)
        # call join here 

