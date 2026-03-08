←
←
# Dictionaries Practice

# Problem 1: 
# Write a function that takes as input a dictionary and returns a new dictionary,
# where 5 is added to each value of the original dictionary, assuming all values are integers.
# e.g
# {"item1": 2, "item2": 7, "item3": 20} returns {"item1": 7, "item2": 12, "item3": 25}
#def new_dict(input_dict):
#    for k,v in input_dict.items():
#        input_dict[k] = v + 5
#    else:
#        return input_dict
# 
#input_dict = {"item1": 2, "item2": 7, "item3": 20}
#print(new_dict({"item1": 2, "item2": 7, "item3": 20})) # expect {"item1": 7, "item2": 12, "item3": 25}



# Problem 2:
# Write a function to check all values are same in a dictionary. 
# Return True if they are all the same, False otherwise
# e.g 
# {'item1': 'apple', 'item2': 'apple', 'item3': 'apple'} returns True, 
# {'item1': 'apple', 'item2': 'apple', 'item3': 'orange'} return False


#def check_same_values(input_dict):
#    v = list(input_dict.values())
#    for i in v:
#        if i == v[0]:
#            continue
#        else:
#            return False
#    else:
#        return True
#
#
#
## testing
#input_dict = {'item1': 'apple', 'item2': 'apple', 'item3': 'apple'}
#print(check_same_values(input_dict))  # expect True
#input_dict = {'item1': 'apple', 'item2': 'apple', 'item3': 'orange'}
#print(check_same_values(input_dict))  # expect False




# Problem 3: 
# Convert a dictionary to a list of lists where each sublist is in the 
# form [key, value]. Return a sorted version of this list where we sort 
# by decreasing values. 
# Example input: {'a': 1, 'b': 5, 'c': 10, 'd': 3, 'e': 2} 
# Example output: [['c', 10], ['b', 5], ['d', 3], ['e', 2], ['a', 1]]
#def dict_to_sorted_list(input_dict):
#    l = []
#    data = list(input_dict.values())
#    for i in range(len(list(input_dict.items()))):
#        for k,v in list(input_dict.items()):
#            for j in data:
#                if v >= i:
#                  continue
#                else:
#                    break
#            else:
#                l.append([k, v])
#                data.remove(v)
#                del input_dict[k]
#                break
#    return l
#            
#
## testing
#input_dict = {'a': 1, 'b': 5, 'c': 10, 'd': 3, 'e': 2}  
#print(dict_to_sorted_list(input_dict))  # expect: [['c', 10], ['b', 5], ['d', 3], ['e', 2], ['a', 1]]



# Problem 4:
# Given a list of dictionaries with item names and amounts in the form {'item': 'my_item_name', 'amount': 'my_amount'}
# write function to combine these items into a single dictionary. See example below. 
# Example input: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: {'item1': 1150, 'item2': 300}

def combine_dicts(input_dicts):
    v_dicts = {}
    for d in input_dicts:
            data = list(d.values())
            if not data[0] in v_dicts.keys():
                v_dicts[data[0]] = data[1]
            else:
                v_dicts[data[0]] = v_dicts[data[0]] + data[1] 

    return v_dicts

    

# testing
input_dicts = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
print(combine_dicts(input_dicts))  # expect {'item1': 1150, 'item2': 300}

