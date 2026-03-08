←
←
#numbers = [1, 2, 3, 4, 5]
#square_dict = {numbers[i]: numbers[i] for i in range(len(numbers))}
#print(square_dict)

#e = enumerate("abc")
#print(e)
#print(e, "__next__")


#def ccount(sentence):
#    char_count = {}
#    for c in sentence:
#        if c != ' ':  # 忽略空格
#            if not c in char_count.keys():
#                char_count[c] = 1
#            else:
#                char_count[c] = char_count[c] + 1
#        else:
#            continue
#    return char_count
#
#sentence = "hello world"
#print(ccount(sentence))

#book = "apple"
#text = "pop"
#
#
#def encode(book, text):
#    code_dict = {}
#    for c in text:
#        pos = book.find(c)
#        code_dict[c] = pos
#        print(f"当前字典: {code_dict}")
#    return code_dict
#
#
#result = encode(book, text)
#print(f"最终结果: {result}")

#def filter_dict(d, min_value):
#    new_dict= {k: v for k, v in d.items() if v > min_value}
#    return new_dict
#    
#d = {'x': 12, 'y': 5, 'z': 18, 'w': 7, 'v': 10} 
#min_value = 9
#print(filter_dict(d, min_value))

book = "python programming"
text = "pop"


def encode(book, text):
    code_dict = {}
    for c in text:
        pos = book.find(c)
        code_dict[c] = str(pos)
        print(f"当前字典: {code_dict}")
    return code_dict


result = encode(book, text)
print(f"最终结果: {result}")