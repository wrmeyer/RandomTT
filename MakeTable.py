import PropositionalStatement as ps
from truths import Truths

def make_table(var_num):
    columns = ps.rand_statement(var_num)
    table = Truths(columns[2], columns[1], columns[0], ints=False).just_table()
    return(table)