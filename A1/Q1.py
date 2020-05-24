c, g, w, m = "C", "G", "W", "M"

l_side = [c, g, w, m]
r_side = []


def issafe():
    # cabbage and goat together
    if c in l_side and g in l_side and m not in l_side:
        return False
    if c in r_side and g in r_side and m not in r_side:
        return False

    # goat and wolf together
    if g in l_side and w in l_side and m not in l_side:
        return False
    if g in r_side and w in r_side and m not in r_side:
        return False

    return True


def print_items():
    for i in l_side:
        print(i, end=" ")

    print("  " * (4 - len(l_side)), end="")

    print("~" * 10, end=" ")

    for i in r_side:
        print(i, end=" ")

    print()


print_items()
while True:
    l_side.remove(m)
    r_side.append(m)

    # as we are otherwise altering the list in the for loop
    # use a copy of it as the interator
    for i in l_side.copy():
        # try to move with an item
        l_side.remove(i)
        r_side.append(i)

        # check if other items safe
        if issafe():
            break

        # undo previous action
        l_side.append(i)
        r_side.remove(i)

    print_items()
    if len(r_side) == 4:
        break

    r_side.remove(m)
    l_side.append(m)

    for i in r_side.copy():
        # don't unnecessarily bring things back if all is safe
        if issafe():
            break

        # try to move with an item
        r_side.remove(i)
        l_side.append(i)

        # check if other items safe
        if issafe():
            break

        # undo previous action
        r_side.append(i)
        l_side.remove(i)

    print_items()
