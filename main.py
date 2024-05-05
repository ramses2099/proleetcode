from typing import List
from datastructure import *

def findduplicate(nums: List) -> None:
    for i in range(len(nums)):
        for j in range((i + 1), len(nums)):
            if nums[i] == nums[j]:
                print(f"{nums[i]} is a duplicate")
                break


def main():
    # linkedlist = Linked_List()
    # linkedlist.insert_at_begining(5)
    # linkedlist.insert_at_begining(15)
    # linkedlist.print()
    # linkedlist.insert_at_end(10)
    # linkedlist.print()
    ll = Linked_List()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    print(f'length of the linkedlist {ll.get_length()}')



if __name__ == "__main__":
    main()
