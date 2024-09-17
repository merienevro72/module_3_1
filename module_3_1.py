calls = 0
def count_calls():
    global calls
    calls +=1
def string_info(string):
    string_ = str (string)
    tuple_ = len(string_), string_.upper(), string_.lower()
    count_calls()
    return tuple_
def is_contains (string, list_to_search):
    string_ = string.lower()
    list_to_search_ = str(list_to_search)
    list_to_search_ = list_to_search_.lower()
    count_calls()
    if string_ in list_to_search_:
        return (True)
    else:
        return (False)

print (string_info('capybara'))
print (string_info('armageddon'))
print (is_contains('urban', ['ban', 'ur', 'URban']))
print (is_contains('big', ['bug', 'bag', 'fig']))
print(calls)
