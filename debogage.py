
# def check_alive(health):
#     if health <= 0 : 
#         return False
#     else:
#         return True

# print(check_alive(0))

# def greet(name):
#     if name == "Johnny" :
#         return "Hello, my love!"
#     else:
#         return "Hello,{name}!".format(name=name)

# print(greet("Marie"))

def create_array(n):
    res=[]
    i=1
    while i<=n: 
        res+=[i]
        i+=1
    return res

print(create_array(1))
