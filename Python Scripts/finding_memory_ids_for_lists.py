sentence = "I desperately want a 1982 Winnebago."
sentence2 = sentence

values = [1,2,3,4,5]

sentence_hex = hex(id(sentence))
sentence2_hex = hex(id(sentence2))

values_elements_hex = [hex(id(_)) for _ in values]
values_hex = hex(id(values))

print(sentence_hex, sentence2_hex)
print(values_elements_hex)
print(values_hex)
