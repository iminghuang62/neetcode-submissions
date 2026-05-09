from typing import Dict, List

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    return list(age_dict.values())

# or this
# def remove_keys(my_dict: Dict[str, int], keys: List[str]) -> Dict[str, int]:
#     for key in keys:
#         if key in my_dict:
#             del my_dict[key]
#     return my_dict

# do not modify below this line
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35}))
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}))
