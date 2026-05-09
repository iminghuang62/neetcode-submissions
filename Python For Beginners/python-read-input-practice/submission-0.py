def add_two_numbers() -> int:
    stringList = input().split(",")
    # intList = []

    # for s in stringList:
    #     intList.append(int(s))
    
    # return sum(intList)

    num1 = int(stringList[0])
    num2 = int(stringList[1])

    return num1 + num2



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
