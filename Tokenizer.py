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
Sentence 1 : Shalane Flanagan's first-place finish in the NYC Marathon's women's division was an incredible achievement on several levels:
Sentence 2 :  Not only was it the Marblehead-raised long-distance runner's first major marathon victory in what she suggested might be the final race of her career, but it was also the first time an American woman had won the race since 1977.
Sentence 3 :  After the race, Flanagan - who withdrew from the Boston Marathon earlier this year due to injury - choked up talking about her Nov.
Sentence 4 :  5 victory.
Sentence 5 :
<BLANKLINE>
About nine months ago, I was heartbroken over not getting the opportunity to race the Boston Marathon, she said.
Sentence 6 :  I just kept telling myself that there's going to be delayed gratification and a moment down the road that would make up for it.
Sentence 7 :
<BLANKLINE>
Iâ€™ve dreamed of a moment like this since I was a little girl, said the 36-year-old.
Sentence 8 :  It took me seven years to do this;
Sentence 9 :  a lot of work just went into this one moment.
Sentence 10 :
<BLANKLINE>
Flanagan also said that as she finished the 26.
Sentence 11 : 2 mile race she thought about fellow American runner M.
Sentence 12 :  Keflezighi, who finished his final career race Sunday, and how she wanted to make him proud.
Sentence 13 :
<BLANKLINE>
And I think I did!
Sentence 14 :  Flanagan said.
Sentence 15 :  Her finish time was 2:
Sentence 16 : 26:
Sentence 17 : 53.
Sentence 18 :  The prize for 1st place was $100,000.
Sentence 19 : 00.

## The errors happen with punctuation used in different locations than sentence boundaries. Places such as dates, decimals, money, time, abbreviation in name cause errors. 

# testing the better_tokenizer function
>>> print_sentences(better_tokenizer(open("tokenizertest.txt", "r").read()))
Sentence 1 :  Shalane Flanagan's first-place finish in the NYC Marathon's women's division was an incredible achievement on several levels: Not only was it the Marblehead-raised long-distance runner's first major marathon victory in what she suggested might be the final race of her career, but it was also the first time an American woman had won the race since 1977.
Sentence 2 :  After the race, Flanagan - who withdrew from the Boston Marathon earlier this year due to injury - choked up talking about her Nov. 5 victory.
Sentence 3 :  About nine months ago, I was heartbroken over not getting the opportunity to race the Boston Marathon, she said.
Sentence 4 :  I just kept telling myself that there's going to be delayed gratification and a moment down the road that would make up for it.
Sentence 5 :  Iâ€™ve dreamed of a moment like this since I was a little girl, said the 36-year-old.
Sentence 6 :  It took me seven years to do this; a lot of work just went into this one moment.
Sentence 7 :  Flanagan also said that as she finished the 26.2 mile race she thought about fellow American runner M. Keflezighi, who finished his final career race Sunday, and how she wanted to make him proud.
Sentence 8 :  And I think I did!
Sentence 9 :  Flanagan said.
Sentence 10 :  Her finish time was 2:26:53.
Sentence 11 :  The prize for 1st place was $100,000.00.

###
The number of sentences goes down and there are no more glaring errors. In sentence punctuation, like ";" and ":" do not count as the sentence is still going, despite them being two completely separate but related thoughts. Otherwise, the number of sentences would increase by two. 
###


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
	end_punctuation = ['.','!','?']
	sentence = ''
	text_list = text.split()
	sentences = []
	
	for word in text_list:
		if any(subtring in word for subtring in end_punctuation):
			# check if date
			if word.lower()[:-1] in ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]:
				sentence += " " + word
			# check if decimal in a number
			elif word[-1] not in "".join(end_punctuation):
				sentence += " " + word
			# check if word is an abbreviation of someone's name
			elif len(word) == 2 and word[0].isupper():
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


