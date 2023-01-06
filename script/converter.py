import init

NEW_VAR = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
grammar = init.init_grammar('cfg.txt')
new_prod = {} # for new production rules
terminals = ['Noun', 'Pronoun', 'PropNoun', 'Adv', 'Adj', 'Num', 'Verb', 'Prep']
index = 0
lhs = grammar.keys()


def remove_duplicate_rhs():
    for key in grammar:
        grammar[key] = list(set(grammar.get(key)))


def remove_unit_prod():
    for key in grammar:
        rhs = grammar.get(key)
        for rule in rhs:
            if rule in lhs:
                grammar[key].remove(rule)
                grammar[key].extend(grammar[rule])


def find_newrule(exp):
    if exp == '':
        return []

    for key in new_prod:
        if exp in new_prod.get(key):
            return [key]
    return []


def remove_long_rhs():
    for key in grammar:
        if key not in terminals:
            rhs = grammar.get(key)
            for rule in rhs:
                if len(rule.split(" ")) > 2:
                    grammar[key].remove(rule)
                    grammar[key].extend([breakdown(rule)])

    for key in new_prod:
        grammar[key] = new_prod.get(key)


def breakdown(s): # 'S P Pel'
    global index
    while len(s.split(" ")) > 2:
        exp = s.split(" ")
        tmp = exp[0] + ' ' + exp[1] # S P
        if find_newrule(tmp) == []:
            new_prod[NEW_VAR[index]] = [tmp]
            index += 1

        exp = find_newrule(tmp) + exp[2::]
        s = ''
        for i in exp:
            s += i
            if i != exp[-1]:
                s += ' '

    return s


def convert():
    remove_duplicate_rhs()

    remove_long_rhs()
    remove_long_rhs()
    remove_long_rhs()

    remove_unit_prod()
    remove_unit_prod()
    remove_unit_prod()

    cfg_file = 'cnf.txt'
    with open(cfg_file, 'w') as newfile:
        for k in grammar:
            newfile.write(f"{k} -> ")
            for obj in grammar.get(k):
                newfile.write(f"{obj}")
                if obj != grammar.get(k)[-1]:
                    newfile.write("|")
            newfile.write("\n")
