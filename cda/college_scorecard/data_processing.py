def list_average(lists):
    n_lists = len(lists)
    list_length = len(lists[0])
    avg_list = [0.0 for i in range(list_length)]
    for i in range(list_length):
        for j in range(n_lists):
            avg_list[i] += lists[j][i]
        avg_list[i] /= n_lists
    return avg_list


def ownership_types(keys):
    ownership_type = {
        '1': 'public',
        '2': 'private',
        '3': 'private',
    }
    return [ownership_type[key] for key in keys]
