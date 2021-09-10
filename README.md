# RandomTT
Short script to randomly generate complex propositional statements with "and," "or," "not," "implication," "bi-implication," and "exclusive or" logical operators.
Uses PrettyTables and a slightly modified version of truths package (https://github.com/tr3buchet/truths)

USAGE:
=======================================================
from RandomTT import PropositionalStatement as ps
table = ps.make_table(*number of atomic variables between 2 and 4 variables*)
print
=======================================================
returns PrettyTable object with atomic propositions and statements as headers with intermediate columns.
