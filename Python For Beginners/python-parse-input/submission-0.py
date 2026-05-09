from typing import List

def read_integers() -> List[int]:
    stringList = input().split(",")
    # print(stringList)
    intList = []
    for s in stringList:
        intList.append(int(s))
    
    return intList

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
