def remove_fourth_character(word: str) -> str:
    firstWord = word[:3]
    secondWord = word[4:]
    return firstWord + secondWord


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
