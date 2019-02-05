# -*- coding: utf-8 -*-
import sys 


def eval_constraint(my_constraint):
    constraint = my_constraint[1:-1]
    op = ''
    left = ''
    right = ''
    writing_left = False
    writing_right = False
    writing_op = True
    num_open_parens = 0 
    for c in constraint:
        if c == '(': 
            num_open_parens += 1
        if c == ' ' and num_open_parens == 0:   
            if writing_op: 
                writing_op = False
                writing_left = True
            elif writing_left: 
                writing_left = False
                writing_right = True
            continue
        if writing_op: 
            op += c
        elif writing_left: 
            left += c
        elif writing_right: 
            right += c
        if c == ')': 
            num_open_parens -= 1
    if "(" in left: 
        left = eval_constraint(left) 
    elif "(" in right: 
        right = eval_constraint(right) 
    return [op, left, right] 
        
def pretty_print(eval_list):
    op = eval_list[0] 
    left = eval_list[1]
    right = eval_list[2]

    final_string = ""
    
    if isinstance(left, list):
        left = pretty_print(left)
    if isinstance(right, list):
        right = pretty_print(right)

    if op == "Eq":
        final_string = left + " = " + right
    elif op == "Ne":
        final_string = left + " != " + right
    elif op == "Ule" or op == "Sle": 
        final_string = left + " != " + right
    elif op == "Ugt" or op == "Sgt": 
        final_string = left + " != " + right
    elif op == "Uge" or op == "Sge": 
        final_string = left + " != " + right
    elif op == "Slt" or op == "Ult": 
        final_string = left + " < " + right
    elif op == "ReadLSB": 
        final_string = right
    elif op == "Add": 
        final_string = left + " + " + right 
    elif op == "Sub": 
        final_string = left + " - " + right 
    elif op == "UDiv" or op == "SDiv": 
        final_string = left + " / " + right 
    elif op == "URem" or op == "SRem": 
        final_string = left + " / " + right 
    elif op == "Mul": 
        final_string = left + " * " + right 
    elif op == "Not": 
        final_string = " - " + left
    elif op == "And": 
        final_string = left + " && " + right 
    elif op == "Or": 
        final_string = left + " || " + right 
    elif op == "Xor": 
        final_string = left + " ^ " + right 
    elif op == "Shl": 
        final_string = left + " << " + right 
    elif op == "LShr": 
        final_string = left + " >> " + right 
    elif op == "AShr": 
        final_string = left + " >> " + right 
    else: 
        print "OPCODE NOT FOUND!!"
        sys.exit()
    return "(" + final_string + ")"



constraintsfile = open(sys.argv[1], 'r')
lines = ''.join(constraintsfile.readlines())
lines = ' '.join(lines.split())
constraints = []
for elt in lines.split(":"): 
    if "(" in elt:
        constraints.append(elt.replace("\n", " ").\
        replace("PRINTING------------------------", '').strip())

simplified_constraints = []
for constraint in constraints:
    curr_constraint = constraint
    simplified_constraint = ''
    # valid constraints will always be wrapped in parens
    
    parsed = pretty_print(eval_constraint(curr_constraint))
    print parsed 

