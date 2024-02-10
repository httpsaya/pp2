def unique(input_list):
    unique_elements = []
    for item in input_list:
        if item not in unique_elements:
            unique_elements.append(item)
    return unique_elements

input_list = [1,1,2,2,3,3,4,4,4,5,5,6,6,6]
print(unique(input_list))