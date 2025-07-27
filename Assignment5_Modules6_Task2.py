list = [1,2,3,4,5,6,7,8,9,10]
print(f"Original list: {list}")
list_extracts = list[:5]
print(f"Extracted first five elements: {list_extracts}")
list.reverse()
print(f"Reversed extracted elements: {list[-5:]}")

