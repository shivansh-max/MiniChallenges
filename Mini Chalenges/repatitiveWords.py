sentence = input("Enter the system WITH punctuation")

sentence_word_list = list(sentence)

sentence_word_list.pop(len(sentence_word_list) - 1)

sentence = ""

for j in range(len(sentence_word_list)):
	sentence += sentence_word_list[j]

# print(sentence)

sentence_word_list = sentence.split()

def Repeat(x): 
    _size = len(x) 
    repeated = [] 
    global repeated_places
    repeated_places = []
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j] and x[i] not in repeated: 
                # repeated_places.append(j)
                repeated.append(x[i])
                repeated_places.append(j) 
    return repeated 
  
print (f"{Repeat(sentence_word_list)} is repeated.")