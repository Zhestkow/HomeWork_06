# a=[i for i in range(1,9)]
# print (a)


# a = [1, 4, 5, 6, 7, 8, 9, 45]
# for idx, value in enumerate(a):
#     print(idx, value)


# num = [1, 2, 3, 4, 5, 6]
# months = ["июнь5", "июнь4", "июнь3", "июнь2", "июнь1"]
# a = list(zip(num, months))
# print (a) 


# sum = lambda a,b: a-b if a>5 else 0
# print (sum(6,5))


# a = [i for i in range (8)]
# print(a)
# a = list(map (lambda x:x+10 if x<4 else x+20,a))
# print(a)


# a = [i for i in range (8)]
# print(a)
# a = list(filter(lambda x:True if x%2!=0 else False,a)) #  -----> 1 вариант
# a = list(filter(lambda x: not x%2,a))  # ----> 2 вариант
# print(a)


i=16
t=15
print(i%t)