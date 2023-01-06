def init_grammar(filename):
    grammar = {}
    with open(filename, 'r') as file:
        for line in file:
            # line lebih besar dari 0 berarti bukan spasi kosong pada txtfile
            if len(line) > 0:
                line = line.replace("\n", "")
                lhs = line.split(" -> ")[0]
                rhs = line.split(" -> ")[1]

                # create empty list for each key
                if line.split(" -> ")[0] not in grammar.keys():
                    grammar[lhs] = []

                # cari rhs dan pisahkan "|"
                rhs = rhs.split("|")
                grammar[lhs] = rhs

    return grammar


def find_rule(exp, grammar=init_grammar('cnf.txt')):

    #global grammar
    if exp == []:
        return []

    tmp = []
    for item in exp:
        for key in grammar:
            if item in grammar.get(key):
                tmp.append(key)

    return tmp
