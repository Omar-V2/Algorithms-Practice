def oneEdit(s1, s2):
    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    elif len(s1) == len(s2) + 1:
        return one_edit_insert(s1, s2)
    elif len(s2) == len(s1) + 1:
        return one_edit_insert(s2, s1)
    return False


def one_edit_replace(s1, s2):
    differences = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            differences += 1
            if differences > 1:
                return False
    return True

def one_edit_insert(s1, s2):
    edited = False
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            i += 1
        else:
            i += 1
            j += 1
    return True
            
print(oneEdit("pale", "paless"))
