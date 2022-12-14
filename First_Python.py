x = 25
y = 40
char = "hello"
z = 3*x +y**2
a_tuple = ("hi", 2.0, 10, True)
print(a_tuple[0])
print(z)

######

a_list = [i for i in range(0,30)]

b_list = a_list.copy()
id(a_list) # 2206363921088
id(b_list) # 2206363303296
    # a_list and b_list occupy their own unique space in RAM
b_list = [i for i in range(1,31)]
    # changes b_list and NOT a_list, which makes sense given above

b_list = a_list.copy()
id(a_list[0]) # 2206174439696
id(b_list[0]) # 2206174439696
    # a_list[0] and b_list[0] occupy their same space in RAM
b_list[0] = 20
    # according to lecture, with this setup, this command simultaneously creates 20 and a unique space in RAM for b_list[0]
id(a_list[0]) # 2206174439696
id(b_list[0]) # 2206174440336

# At the end, it is super technical, and it is just always important to copy() with list type

######

c_list = [1.0, "bye", a_list, False]

d_list = c_list.copy()
id(c_list) # 2206363942848
id(d_list) # 2206363920960
    # c_list and d_list occupy their own unique space in RAM
d_list = ["hi", "my", "name", "is"]
    # changes d_list and NOT c_list, which makes sense given above
    
d_list = c_list.copy()
id(c_list[1]) # 2206230911280
id(d_list[1]) # 2206230911280
    # c_list[1] and d_list[1] occupy their same space in RAM
d_list[1] = 45
    # according to lecture, with this setup, this command simultaneously creates 45 and a unique space in RAM for d_list[1]
id(c_list[1]) # 2206230911280
id(d_list[1]) # 2206174441136

d_list = c_list.copy()
id(c_list[2]) # 2206363921088
id(d_list[2]) # 2206363921088
    # c_list[2] and d_list[2] occupy their same space in RAM
d_list[2][4] = "new"
    # changes d_list[2][4], c_list[2][4], and a_list[4]
    
a_list[4] = 4
    # # changes d_list[2][4], c_list[2][4], and a_list[4]
    
######

e_list = [1.0, "bye", a_list.copy(), False]
id(e_list[2]) # 2206363794304
id(d_list[2]) # 2206363921088
id(c_list[2]) # 2206363921088
    # e_list[2] occupy their own unique space in RAM
e_list[2][4] = "new"
    # changes only e_list[2][4]
    
# At the end, be careful when copying a list with another list in it (the other list is not copied)

######

abc = [5,3,1]

efg = abc
id(efg)
id(abc)

efg = ["hi", 1, 2]
id(efg)
id(abc)
    # efg ONLY changes, probably because we are changing efg as a whole and reassigning something entirely different

efg = abc
id(efg[1])
id(abc[1])

efg[1] = False
id(efg[1])
id(abc[1])
    # efg[1] and abc[1] changes 

######

add_list = [1,2,3] + [4,5,6]
    # Created [1,2,3,4,5,6]
    
import numpy as np
vector_1 = np.array([1,2,3])
vector_2 = np.array([4,5,6])
vector_add = vector_1 + vector_2
