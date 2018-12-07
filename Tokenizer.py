'''
# CMSC/LING 208 Lab 9 Part 2
# Name: Luis Contreras-Orendain

## Test Cases

>>> tokenizer_output = tokenizer("Hello, World. My name is John; I speak english. What is your name. Wow!")
>>> tokenizer_output
['Hello, World.', ' My name is John;', ' I speak english.', ' What is your name.', ' Wow!']

>>> print_sentences(tokenizer_output)
Sentence 1 : Hello, World.
Sentence 2 :  My name is John;
Sentence 3 :  I speak english.
Sentence 4 :  What is your name.
Sentence 5 :  Wow!

# calling the demo function to see what it does to the tokenizertest.txt file
>>> naive_demo()

## The errors happen with punctuation used in different locations than sentence boundaries. Places such as dates, decimals, money, time, abbreviation in name cause errors. 

# testing the better_tokenizer function
>>> print_sentences(better_tokenizer(open("tokenizertest.txt", "r").read()))

'''
# tokenizer takes a string and returns a list of the sentences contained in that string.
def tokenizer(text):
	end_punctuation = ['.','!','?',':',';']
	sentence = ''
	sentences = []
	for c in text:
		if c in end_punctuation:
			sentence += c
			sentences.append(sentence)
			sentence = ''
		else:
			sentence+=c
	return sentences
	
def better_tokenizer(text):
	end_punctuation = ['.','!','?',':',';']
	sentence = ''
	text_list = text.split()
	sentences = []
	
	for word in text_list:
		if any(subtring in word for subtring in end_punctuation):
			# check if date
			if word.lower()[:-1] in ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]:
				sentence += " " + word
			# check if decimal in a number
			elif word[0] in "1234567890" or word[0] in "124567890":
				sentence += " " + word
			# check if abbreviation
			elif word[:2] == "mr" or word[:2] == "ms" or word[0].isupper() and len(word) == 2:
				sentence += " " + word
			else:
				sentence += " " + word
				sentences.append(sentence)
				sentence = ""
		else:
			sentence += " " + word
		
	return sentences 
	#print(text_list)

# print_sentences takes a list of strings and prints them one at a time   
def print_sentences(sentence_list):
	i = 1
	for s in sentence_list:
		print('Sentence',i,':',s)
		i+=1

# Demonstration: rewrite demo() so that it 1) opens the file tokenizertest.txt and reads it into a string, 2) sends that string to tokenizer, 3) sends the result of tokenizer to print_sentences, and 4) closes the file tokenizertest.txt
def naive_demo():
	# read in text from file as string
	file_string = open("tokenizertest.txt", "r").read()
	
	# call tokenizer() witht that string
	tokenizer_output = tokenizer(file_string)

	# call print_sentences with the list from tokenizer
	print_sentences(tokenizer_output)





def _test():
	import doctest
	result = doctest.testmod()
	print("Result of doctest for Tokenizer.py is:", result[0])
	if result[0] == 0:
		print("Wahoo! Passed all", result[1], "tests!")
	else:
		print("Rats!")

if __name__=='__main__':
	_test()
    #demo()


