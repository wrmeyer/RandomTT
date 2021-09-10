# RandomTT
Short script to randomly generate complex propositional statements with "and," "or," "not," "implication," "bi-implication," and "exclusive or" logical operators.
Uses PrettyTables and a slightly modified version of truths package (https://github.com/tr3buchet/truths) to build statements into a truth table

## _Usage:_
```sh
from RandomTT import PropositionalStatement as ps
table = ps.make_table(*number of atomic variables between 2 and 4 variables*)
```
returns PrettyTable object with atomic propositions and statements as headers with intermediate columns.

```sh
statement_list = ps.rand_statement(*number of atomic variables between 2 and 4 variables*)
```
returns 3 lists of strings:
1) list of randomly generated, complex propositional satements
2) list of logically equivalent statements using only "and," "not," and "or" operators
3) list of atomic propositions used in the statements
