list_test1 = ['apple', 'potato', 'Capitalized Words']
list_test2 = [123, 8897, 42, 1168, 8675309]
list_test3 = ['hello', 'world', 123, 'orange']
# We want to COMPLETELY reverse a list by flipping the order of the entries AND flipping the order of characters in each element.

# a) Define a 'reverse_characters' function. Give it one parameter, which will be the string to reverse.
def reverse_characters(s):
# b) Within the function, use the 'list' function to split a string into a list of individual characters
    char_list = list(s)
# c) 'reverse' your new list.
    char_list.reverse()
# d) Use 'join' to create the reversed string and return that string from the function.
    reversed_string = ''.join(char_list)
# e) Create a variable of type string to test your new function.
    return reversed_string
# f) Use 'print(reverse_characters(my_variable_name))'; to call the function and verify that it correctly reverses the characters in the string.
print(reverse_characters("Launchcode")) 


# g) Use method chaining to reduce the lines of code within the function.
# def reverse_characters(s):
#     return ''.join(list(s)[::-1])
# my_variable_name = "Launchcode"
# print(reverse_characters(my_variable_name)) 

# 2) The 'split' method does not work on numbers, but we want the function to return a number with all the digits reversed (e.g. 1234 converts to 4321 and NOT the string "4321")
# a) Add an if statement to your reverse_characters function to check the typeof the parameter.
def reverse_characters(input_char):
    if type(input_char) == str:
        return ''.join(list(input_char)[::-1])
    elif type(input_char) == int:
        reversed_str = ''.join(list(str(input_char))[::-1])  
        return int(reversed_str)
    else:
        return "not an int or str"
# b - d) If type is ‘string’, return the reversed string as before. If type is ‘number’, convert the parameter to a string, reverse the characters, then convert it back into a number. Return the reversed number.
def reversed_list(list_reverse):
    for i in range(len(list_reverse)):
        list_reverse[i] = reverse_characters(list_reverse[i])
    list_reverse.reverse()
    return list_reverse
# e) Be sure to print the result returned by the function to verify that your code works for both strings and numbers. Do this before moving on to the next steps.
print(reversed_list(list_test2))


# 3) Create a new function with one parameter, which is the list we want to change. The function should:
# a) Define and initialize an empty list.
def new_list(input_list):
    result_list = []
# b) Loop through the old list.
    for item in range(len(input_list)):
        list_item=reverse_characters(input_list[item])
# d) Add the reversed string (or number) to the list defined in part ‘a’.
        result_list.append(list_item)
# e) Return the final, reversed list..
    return result_list
# c) For each element in the old list, call reverse_characters to flip the characters or digits.
def reverse_characters(s):
    if type(s) == str:
        return s[::-1]
    elif type(s) == int:
        reversed_str = str(s)[::-1]
        return int(reversed_str)
       
# f) Be sure to print the results from each test case in order to verify your code.
print(new_list(list_test1))
print(new_list(list_test2))
print(new_list(list_test3))



    

