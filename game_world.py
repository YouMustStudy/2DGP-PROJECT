# layer 0: MAP INDEX
# layer 1: BackGround
objects = [[],[],[]]

def add_object(o, layer):
    objects[layer].append(o)


def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o
            break;


def clear():
    for o in all_objects():
        del o
    objects.clear()
    objects.append([])
    objects.append([])
    objects.append([])


def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o

