"""
# CMSC/LING 208 Lab 9 Part 3
# Name: Luis Contreras-Orendain
>>> mytext = 'NSWs must be classified for phonetic analysis. This is especially important in the case of numbers, which differ in their pronunciation depending on their category. For example, it is necessary to distinguish a year like 1849 from a PIN like 3269. Phone numbers come in variable forms like 234-6529 or 492-499-1349 or (203)893-5938. Zip codes can also vary between 29481 or 49381-2395.'
>>> demo()

"""
# Example text as a string
mytext = 'NSWs must be classified for phonetic analysis. This is especially important in the case of numbers, which differ in their pronunciation depending on their category. For example, it is necessary to distinguish a year like 1849 from a PIN like 3269. Phone numbers come in variable forms like 234-6529 or 492-499-1349 or (203)893-5938. Zip codes can also vary between 29481 or 49381-2395.'

# Strips periods from sentence-final words 
def remove_punctuation(text):
	return [w[:-1] if w[-1] == '.' else w for w in text]

# Returns true iff string c is a single digit
def is_digit(c):
	return c in '0123456789'

# Returns true iff string w consists of all digits   
def is_string_of_digits(w):
	for c in w:
		if not is_digit(c):
			return False
	return True

# Returns true iff string w is of the form XXXXX or XXXXX-XXXX where X is a digit (incomplete)
def is_zip(w):
	if len(w) == 5:
		return is_string_of_digits(w)
	elif len(w) == 10 and w[5] == "-":
		return is_string_of_digits(w[:5]+w[6:])
	return False

# Suggested approach to distinguishing years from PINs
# Returns true iff string word is found in list wordlist within scan_range positions (left or right) of start_pos 
def scan(wordlist, word, start_pos, scan_range):
   
	return False  # placeholder
  
# Takes a text t as a list of words with sentence-final punctuation removed and returns that text with markup for the following NSW categories: zip codes, phone numbers, years, and PINs.
def NSW_markup(t):
	markedup = []
	i = 0
	while i < len(t):
		if is_zip(t[i]):
			print(t[i],'is a zip code!')      
		i+=1
      
	return markedup









def demo():
   print(NSW_markup(remove_punctuation(mytext.split())))

def _test():
	import doctest
	result = doctest.testmod()
	print("Result of doctest for Tokenizer.py is:", result[0])
	if result[0] == 0:
		print("Wahoo! Passed all", result[1], "tests!")
	else:
		print("Rats!")   
   
if __name__ == '__main__':
   _test()
   #demo()




