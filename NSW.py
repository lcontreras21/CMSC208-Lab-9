
# CMSC/LING 208 Lab 9 Part 3
# Name: Luis Contreras-Orendain

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
	snippet = wordlist[start_pos-scan_range:start_pos+scan_range] 
	return "PIN" in snippet
	
# Returns true iff string w is of the form XXX-XXXX, XXX-XXX-XXXX, (XXX) XXX-XXXX
def is_phone(w):
	if len(w) == 8:
		return is_string_of_digits(w[:3] + w[4:])
	elif len(w) == 12:
		return is_string_of_digits(w[:3] + w[4:7] + w[8:])
	elif len(w) == 14:
		return is_string_of_digits(w[1:4] + w[6:9] + w[10:])
	elif w[0] == "(" and w[4] == ")":
		return is_phone(w[5:])
	else:
		return False
  
# Takes a text t as a list of words with sentence-final punctuation removed and returns that text with markup for the following NSW categories: zip codes, phone numbers, years, and PINs.
def NSW_markup(t):
	markedup = []
	i = 0
	while i < len(t):
		# check if the word is a zip code
		if is_zip(t[i]):
			markedup.append("<zip>" + t[i] + "</zip>")
		# check if word is 4 numbers and then decide whether it is a pin or  a year
		elif is_string_of_digits(t[i]):
			if i < len(t) - 2 and i > 2:
				if scan(t, "PIN", i, 2):
					markedup.append("<pin>" + t[i] + "</pin>")
				else:
					markedup.append("<year>" + t[i] + "</year>")
		# check if word is a phone number
		elif is_phone(t[i]):
			markedup.append("<phone>" + t[i] + "</phone>")
		else:
			markedup.append(t[i])
		i+=1
      
	return markedup

def demo():
   print(NSW_markup(remove_punctuation(mytext.split())))
   
if __name__ == '__main__':
   demo()
