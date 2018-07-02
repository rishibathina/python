def mode(my_list):
    unique_list = sorted(list(set(my_list)))
    appearance = {a:my_list.count(a) for a in unique_list}
    max_app = max(appearance.values())
    list_of_tuples = []
    for key, value in appearance.items():
        list_of_tuples.append((key,value))
    list_of_tuples.sort(key=lambda  x: x[1])
    list_of_tuples = list_of_tuples[::-1]
    chosen_tuple = list_of_tuples[0]
    chosen_number = chosen_tuple[0]
    return chosen_number