def permute(input_list):
    output_list = []
    new_input_list = []
    for item in input_list:
        new_input_list.append(str(item))
    if len(input_list) == 1:
        output_list = [new_input_list]
    else:
        for index,element in enumerate(new_input_list):
            element = str(element)
            #print (element)
            for permutation in permute(new_input_list[:index] + new_input_list[index + 1:]):
                new_permutation = ''.join(permutation)
                output_list += [(element) + (new_permutation)]
    return output_list
print(permute([1,2,3]))