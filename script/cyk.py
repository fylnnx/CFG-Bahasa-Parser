# first, put CNF into dictionary
import streamlit as st
from script import init

grammar = init.init_grammar(r'cnf.txt')


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
    word_notfound = []
    for i in range(n):
        if find_rule([s[i]]) == []:
            word_notfound.append(s[i])
        table[i][i] = find_rule([s[i]])

    if word_notfound !=[]:
        str_notfound = ''
        for i in word_notfound:
            str_notfound += i
            if i != word_notfound[-1] and len(word_notfound) !=1:
                str_notfound += ', '
        st.write("Kata", str_notfound, "tidak ada dalam CFG")

    elif word_notfound == []:
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
                    table[i][j] = list(set(table[i][j]))
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
        # check output in terminal
        print(table2)
        # show CYK in web
        st.dataframe(table2)

        print('\n\n')
        if table[n - 1][0] == []:
            st.error("Kalimat tidak valid!")
        else:
            st.success("Kalimat valid")

        return table
