first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(elm) for elm in first_strings if len(elm) > 5]
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
third_result = {elm: len(elm) for list_ in (first_strings, second_strings) for elm in list_ if not (len(elm) % 2)}
print(first_result)
print(second_result)
print(third_result)
