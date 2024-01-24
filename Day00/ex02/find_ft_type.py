def all_thing_is_obj(object: any) -> int:
    t = object.__class__
    if (str(t).find("list") > 0):
        print("List :", t)
    if (str(t).find("tuple") > 0):
        print("Tuple :", t)
    if (str(t).find("set") > 0):
        print("Set :", t)
    if (str(t).find("dict") > 0):
        print("Dict :", t)
    if (str(t).find("str") > 0):
        if (object == "Brian"):
            print("Brian is in the kitchen :", t)
        if (object == "Toto"):
            print("Toto is in the kitchen :", t)
    if (str(t).find("int") > 0):
        print("Type not found")
    return (42)
