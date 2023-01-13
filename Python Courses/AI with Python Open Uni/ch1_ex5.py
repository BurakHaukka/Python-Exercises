# def my_split(sentence, x):
#     sent_list = list(sentence)
#     sent_index = len(sent_list)
#     splitted_sent = []
#     for i in range(sent_index):
#         if sent_list[i] in small or capital:
#             splitted_sent.insert(i, sent_list[i])
#             splitted_sent.insert(i + 1, x)
#         return splitted_sent

def my_split(sentence, x):
    splitted_sentence = []
    pos = -1
    last_pos = -1
    while ' ' in sentence[pos + 1:]:
        pos = sentence.index(x, pos + 1)
        splitted_sentence.append(sentence[last_pos + 1:pos])
        last_pos = pos
    splitted_sentence.append(sentence[last_pos + 1:])
    return splitted_sentence

# def my_join(splitted_sentence, y):
#     separated_index = len(splitted_sentence)
#     joined_sentence = ''
#     for i in range(0, separated_index):
#         if joined_sentence[i] not in small and capital:
#             joined_sentence[i] = y
#     for i in joined_sentence:
#         print(i)

def my_join(splitted_sentence, y):
    joined = ''
    for i in splitted_sentence:
        joined += y + i
    return joined[1:]

sentence = str(input("Please enter a sentence:"))
print(my_join(my_split(sentence, ' '), ','))
print(my_join(my_split(sentence, ' '), '\n'))

#print(my_split(sentence, ' '))
#print(my_join(sentence, '\n'))
