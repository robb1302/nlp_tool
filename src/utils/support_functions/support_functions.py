def flatten_list(more_dim_list):
    """
    more_dim_list -   a list with lists

    The Function unlists a more dimensional list

    flat_list - list with one dimenesion

    """
    flat_list = []
    # Iterate through the outer list
    for element in more_dim_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list