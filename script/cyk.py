# first, put CNF into dictionary
import streamlit as st
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
    s = s.split(" ") # pecah string menjadi list berdasarkan kata
    n = len(s) # jumlah kata
    table = [[[] for i in range(n)] for j in range(n)] # buat tabel

    # loop untuk row 1
    for i in range(n):
        table[i][i] = find_rule([s[i]])

    # rumus cyk: V(i,j) = V(i-k[-(x)],j) * V(i, j+k[x-1])
    # where k = range(1,loop)
    # where x = range(loop)

    # n = 5
    for loop in range(2, n+1): # 2, 3, 4, 5
        k = range(1, loop) # [1]
        for i in range(loop-1, n): # 1, 2, 3, 4
            for j in range(n - loop+1): # 0, 1, 2, 3
                for x in range(1, loop):
                    table[i][j] += find_rule(concat(table[i-k[-x]][j], table[i][j+k[x-1]]))
                    # cetak tabel masing-masing sel

        # cetak tabel per row
        # check output in terminal
        print(table)
        # show CYK in web
        st.dataframe(table)

    st.write("Hasil Parsing CYK Table Filling: ")
    # cetak tabel setelah selesai
    print('\n\n')
    table2 = []
    for row in table:
        table2.append(row)
    #check output in terminal
    print(table2)
    #show CYK in web
    st.dataframe(table2)

    print('\n\n')
    if table[n-1][0] == []:
        st.error("Kalimat tidak valid!")
    else:
        st.success("Kalimat valid")

    return table



grammar = init_grammar(r'cnf.txt')
