def read_input_as_int(filename):
    with open(filename, 'r') as f:
        return list(map(lambda x: int(x.strip()), f.readlines()))


def read_input_as_one_line_ints(filenamn):
    with open(filenamn, 'r') as f:
        return list(map(int, f.readline().split(',')))


def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(lambda x: x.strip(), f.readlines()))


def read_input_as_doc(filename):
    with open(filename, 'r') as f:
        return f.read()


def flatten(ls):
    return [item for sublist in ls for item in sublist]
