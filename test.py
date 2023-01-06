# first, put CNF into dictionary
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


def find_rule(exp):
    global grammar
    if exp == []:
        return []

    tmp = []
    for item in exp:
        for key in grammar:
            if item in grammar.get(key):
                tmp.append(key)

    return tmp


def concat(s1, s2):
    if s1 == [] or s2 == []:
        return []

    tmp = []
    for i in s1:
        for j in s2:
            tmp.append(i + ' ' + j)

    return tmp


def cyk(s):
    s = s.split(" ")  # pecah string menjadi list berdasarkan kata
    n = len(s)  # jumlah kata
    table = [[[] for i in range(n)] for j in range(n)]  # buat tabel

    # loop untuk row 1
    for i in range(n):
        table[i][i] = find_rule([s[i]])

    # rumus cyk: V(i,j) = V(i-k[-(x)],j) * V(i, j+k[x-1])
    # where k = range(1,loop)
    # where x = range(loop)

    # n = 5
    for loop in range(2, n + 1):  # 2, 3, 4, 5
        k = range(1, loop)  # [1]
        for i in range(loop - 1, n):  # 1, 2, 3, 4
            for j in range(n - loop + 1):  # 0, 1, 2, 3
                for x in range(1, loop):
                    table[i][j] += find_rule(concat(table[i - k[-x]][j], table[i][j + k[x - 1]]))
                    # cetak tabel masing-masing sel
                    print(table)

        # cetak tabel per row
    print('\n')
    # cetak tabel setelah selesai
    for row in table:
        print(row)



    return table


grammar = init_grammar('cnf.txt')
cyk('Kratos datang dari Yunani')