input_string = input("Digite uma palavra: ")

inverted_string = ""

for i in range(len(input_string) - 1, -1, -1):
    inverted_string += input_string[i]

print("String original:", input_string)
print("String invertida:", inverted_string)
