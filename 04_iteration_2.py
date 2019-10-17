def my_loop(n):
    for i in range(1,n):
        print(i)

def my_reverse_loop(n):
    num_list = []
    for i in range(1,n): 
        num_list.append(i)
    num_list.reverse()
    for i in num_list: 
        print(i) 

print('my loop')
my_loop(10)
print("my reverse loop")
my_reverse_loop(10)





