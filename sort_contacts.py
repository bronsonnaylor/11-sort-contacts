def sort_contacts(contacts):
    list = []
    [list.append((names, details[0], details[1])) for names, details in sorted(contacts.items())]
    #can't use append  with list comprehension.. Ex: list = [list.append(**)] for...
    #must enclose in [] on line 3??
    return list
