def numbers(Students):                                                                                                  # def created

    list1 = []

    for i in range(len(Students)) :                                                                                     # Multidimentional list concept

        for j in range(len(Students[i])) : 

            list1.append(Students[i][j])

    

    num = {}

    for elements in list1:

        num[elements] = list1.count(elements)

    

    # num = {elements:list1.count(elements) for elements in list1}                      # Dictionary Compression form

    return num                                                                                                           # num returned

def popular(num):

    popular_course = max(num,key=num.get)

    # popular_course = max(num,key=num.get)                                                                                 # printing the key having max value

    return popular_course

Students = [['math', 'phy', 'chem', 'cs'], ['math', 'phy'], ['math', 'chem'], ['history', 'eco']]

x = numbers(Students)

print(x)

y = popular(x)

print("i course is: ",y)
