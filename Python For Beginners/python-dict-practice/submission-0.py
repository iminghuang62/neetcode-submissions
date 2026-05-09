from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    count_dic = {}

    for c in word:
        if c not in count_dic:
            count_dic[c] = 1
            # print(count_dic)
        else:
            count_dic[c] = count_dic[c] + 1
            # print(count_dic)
    return count_dic




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
