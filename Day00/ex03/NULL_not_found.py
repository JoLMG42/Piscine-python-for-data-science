def NULL_not_found(object: any) -> int:
    t = object.__class__
    if (object is None):
        print("Nothing:", object, t)
    elif (t == float and str(object) == "nan"):
        print("Cheese:", object, t)
    elif (t == int and object == 0):
        print("Zero:", object, t)
    elif (object == '' and t == str):
        print("Empty:", t)
    elif (object is False):
        print("Fake:", object, t)
    elif (t == str and object != ''):
        print("Type not Found")
        return (1)
    return (0)
