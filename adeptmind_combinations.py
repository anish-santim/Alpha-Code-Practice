import itertools 

'''
Given a list of tuples [('E', 'B'), ('C', 'D'), ('A', 'D')] and a target 'ABC'. 
return True if you can use the tuples to assemble the target.
By assemble means, each tuple can be used exactly once, and we need to choose one value from each tuple.
'''

list_of_tuples = [('E', 'B'), ('C', 'D'), ('A', 'D')]
target_string  = 'ABC'

'''
assemble_target_string function checks for target_string possible by assembling the list_of_tuples
'''

def assemble_target_string(list_of_tuples, target_string):
    target_string = "".join(sorted(target_string))
    for word in list(itertools.product(*list_of_tuples)):
        word = "".join(sorted(word))
        if word==target_string: return True 
    return False 

print(assemble_target_string(list_of_tuples, target_string))
        