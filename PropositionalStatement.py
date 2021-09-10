import random
import PropositionalStatement as ps
from truths import Truths

def rand_statement(num_variables):
    possible_variables = ['p','q','r','s','t']
    variables = []
    operators = ["and","not","or","imp","bimp","xor"]
    operators_without_not = ["and","or","imp","bimp","xor"]
    for x in range (0,num_variables):
        variables.append(possible_variables[x])
        
    #determining the number of operators to use in first pass
    statement_len = random.randint(num_variables, num_variables+1)
    
    #creating an ordered list of operators to be used but not having an operator appear more than twice
    operator_list = []
    for segment in range(statement_len):
        operator_list.append(random.choice(operators))
        for i in range(len(operator_list)):
            while True:
                if operator_list.count(operator_list[i]) > 2:
                    operator_list[i] = random.choice(operators)
                else:
                    break
#=================================
                
    #taking new list of operators and slapping some variables on either end of them
    while True:
        used_variables = []
        statements = []
        for operator in operator_list:
            if operator == "not":
                var = random.choice(variables)
                used_variables.append(var)
                statement = ("not(" + str(var) + ")")
                statements.append(statement)
            else:
                var1 = random.choice(variables)
                used_variables.append(var1)
                var2 = random.choice(variables)
                used_variables.append(var2)
                #Making sure different variables are on either side of the operator
                while True:
                    if var1 == var2:
                        var2 = random.choice(variables)
                    else:
                        break
                statement = (str(var1) + " " + operator + " " + str(var2))
                statements.append(statement)
        #making sure all variables are used
        res = []
        for var in used_variables:
            if var not in res:
                res.append(var)
        if variables == sorted(res):
            break
#====================
    #Pairing those statements with a and/or/not form for easy logic parsing
    abn_statements=[]
    for item in statements:
        abn_statements.append(break_down(item))

#================
    #taking the list of statements and makes one large statements for intermediate columns of truth table
    #building two lists: one that allows complex operators i.e. bi-implication, implication, exclusive-or; and one that builds logically equivalent statements but only uses 'and', 'or', and 'not'
    #uses cloned list of existing statements to account for redundency
    statements_clone = []
    for item in statements:
        statements_clone.append(item)
    abn_statements_clone = []
    for item in abn_statements:
        abn_statements_clone.append(item)
    new_statements = []
    new_abn_statements = []
    not_count = 0
    while True:
        if len(statements_clone) == 0:
            break
        if len(statements_clone) %2 == 1:
            if len(statements_clone) == 1:
                break
            else:
                if not_count == 1:
                    choice = random.choice(operators)
                else:
                    choice = random.choice(operators_without_not)
                if choice != "not":
                    statement = ("("+statements_clone[0] + ") " + choice + " (" + statements_clone[1]+")")
                    abn_statement = ("("+abn_statements_clone[0] + ") " + choice + " (" + abn_statements_clone[1]+")")
                    
                    #break_down function takes complex operator propositions and converts them to logically equivalent statements using simple operators
                    statements.append(statement)
                    abn_statements.append(break_down(abn_statement))
                    new_statements.append(statement)
                    new_abn_statements.append(break_down(abn_statement))
                    
                    #remove first and second statement from statements clone in order to signify that the statements have been processed
                    statements_clone.remove(statements_clone[0])
                    statements_clone.remove(statements_clone[0])
                    abn_statements_clone.remove(abn_statements_clone[0])
                    abn_statements_clone.remove(abn_statements_clone[0])
                else:
                    statement = ("(not("+ statements_clone[0] + "))")
                    abn_statement = ("(not("+ abn_statements_clone[0] + "))")
                    
                    statements.append(statement)
                    abn_statements.append(break_down(abn_statement))
                    new_statements.append(statement)
                    new_abn_statements.append(break_down(abn_statement))
                    
                    #remove first and second statement from statements clone
                    statements_clone.remove(abn_statements_clone[0])
                    abn_statements_clone.remove(abn_statements_clone[0])
                    not_count += 1
        else:
            choice = random.choice(operators_without_not)
            statement = ("("+statements_clone[0] + ") " + choice + " (" + statements_clone[1]+")")
            abn_statement = ("("+abn_statements_clone[0] + ") " + choice + " (" + abn_statements_clone[1]+")")
            
            statements.append(statement)
            abn_statements.append(break_down(abn_statement))
            new_statements.append(statement)
            new_abn_statements.append(break_down(abn_statement))
            
            #remove first and second statement from statements clone
            statements_clone.remove(statements_clone[0])
            statements_clone.remove(statements_clone[0])
            abn_statements_clone.remove(abn_statements_clone[0])
            abn_statements_clone.remove(abn_statements_clone[0])

      
    #final column making
    #same process as above but makes assumption that fewer statements remain in need of processing
    leftovers = statements_clone + new_statements
    abn_leftovers = abn_statements_clone + new_abn_statements
    while True:
        if (len(leftovers)) >= 2:
            choice = random.choice(operators_without_not)
            final_statement = ("("+leftovers[0] + ") " + choice + " (" + leftovers[1]+")")
            abn_final_statement = ("("+abn_leftovers[0] + ") " + choice + " (" + abn_leftovers[1]+")")
            
            statements.append(final_statement)
            abn_statements.append(break_down(abn_final_statement))
            
            abn_leftovers.remove(abn_leftovers[0])
            abn_leftovers.remove(abn_leftovers[0])
            leftovers.remove(leftovers[0])
            leftovers.remove(leftovers[0])
            
            leftovers.append(final_statement)
            abn_leftovers.append(break_down(final_statement))
        else:
            if len(leftovers) == 2:
                statement = ("("+ final_statement + ") " + random.choice(operators_without_not) + " (" + leftovers[0]+")")
                
                statements.append(statement)
                abn_statements.append(break_down(statement))
                
                leftovers.remove(leftovers[0])
                abn_leftovers.remove(abn_leftovers[0])
                
            else:
                break
    #returns complex statements, logically equivalent simple statements, and atomic variables all in lists of strings
    return (statements, abn_statements, variables)

#breaks down propositional statements into "and", "not", and "or" operator statements
def break_down(statement):
    while True:
        if " xor " in statement:
            x = statement.split(" xor ")[0]
            y = statement.split(" xor ")[1]
            statement = "(" + x + " or "+  y +") and not(" + x + " and " + y + ")"
        elif " imp " in statement:
            x = statement.split(" imp ")[0]
            y = statement.split(" imp ")[1]
            statement = "(not " + x + ") or " + y
        elif " bimp " in statement:
            x = statement.split(" bimp ")[0]
            y = statement.split(" bimp ")[1]
            statement = "(" + x + " and " + y + ") or (not (" + x + ") and not (" + y + "))"
        else:
            break
    return(statement)

def make_table(var_num):
    columns = rand_statement(var_num)
    table = Truths(columns[2], columns[1], columns[0], ints=False).just_table()
    return(table)