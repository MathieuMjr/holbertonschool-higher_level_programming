def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
# ou : return None if idx < 0 or idx >= len(my_list) else my_list[idx]
