# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    list_to_remove_elements= list(list_to_remove_elements)
    if len(list_to_remove_elements) > 5:
        list_to_remove_elements.pop(5)
        list_to_remove_elements.pop(4)
        list_to_remove_elements.pop(0)
    elif len(list_to_remove_elements) >= 5:
        list_to_remove_elements.pop(4)
        list_to_remove_elements.pop(0)
    elif len(list_to_remove_elements) > 0:
        list_to_remove_elements.pop(0)
    else:
        return list_to_remove_elements
    return list_to_remove_elements

def add_elements(list_to_add_elements):
    list_to_add_elements = list(list_to_add_elements)
    list_to_add_elements.insert(0, 'Pink')
    list_to_add_elements.append('Yellow')
    return list_to_add_elements

def is_empty(list_to_check):
    list_to_check=list(list_to_check)
    if len(list_to_check) == 0:
        return True
    else:
        return False

def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1)<3 and len(list_to_compare2)<3:
        return True
    elif len(list_to_compare1)>=3 and len(list_to_compare2)>=3:
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
        else:
            return False
    else:
        return False

def list_of_lists(list_of_lists_to_modify):
    row1= list_of_lists_to_modify[0]
    row2= list_of_lists_to_modify[1]
    row3= list_of_lists_to_modify[2]
    if len(row1)>1:
        row1= row1[:2] 
    elif len(row1)==1:
        row1= [row1[0]]
    else:
        row1= []

    if len(row2)>=4:
        row2= row2[1:4]
    elif len(row2)==3:
        row2= row2[1:3]
    elif len(row2)==2:
        row2= row2[2]
    else:
        row2= []

    if len(row3)>=2:
        row3= [row3[-2],row3[-1]]
    elif len(row3)==1:
        row3= [row3[-1]]
    else:
        row3=[]

    final_table= [row1,row2,row3]
    return final_table
