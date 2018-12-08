# CMSC_Lab_9

Lab 9 of my CMSC 208 Speech Synthesis and Recognition course. 

Instructions:

Part 1: Reflection

In class on Monday, December 3, we did a group activity in which each student had the opportunity to communicate using a speech generating device (or SGD). Write a brief (2-3 paragraph) reflection on that activity. You can comment on the SGD itself (the Predictable iPad app) but be sure to also comment on the experience of relying on a device to speak for you, especially when everyone else could use their own voices.

Part 2: Sentence Tokenization

The starter file Tokenizer.py includes a (very naive) tokenizer function that takes a text and parses it into sentences based only on the presence of punctuation.

First, fill in the function demo() as indicated in the comment above it. (If needed see here for python file input/output methods.) Run that function to see what the tokenizer currently does with the test file and identify its errors.

Now, modify the tokenizer function so that it does a better job. Have it factor in more information (i.e., rules) to reduce the number of errors. You can limit your focus to the kinds of errors present in this particular test text, meaning you don't have to go so far to address any possible tokenization error (indeed, this is the very problem with rule-based approaches!). But your modifications should be general enough that your function will succeed on a different text that presents the same kind of errors.

Part 3: NSW Classification


Now write a function that takes a text and labels various categories of non-standard words (NSWs). The file NSW.py includes some preliminary code to get you started.

At the top of the file is a sample text that contains various categories of NSWs, including zip codes, phone numbers, years, and PINs (personal identification numbers). The task is to complete the function NSW_markup, which takes this text and returns it with the NSWs identified and labeled with tags, like this:

```xml
['NSWs', 'must', 'be', 'classified', 'for', 'phonetic', 'analysis', 'This', 'is', 'especially', 'important', 'in', 'the', 'case', 'of', 'numbers,', 'which', 'differ', 'in', 'their', 'pronunciation', 'depending', 'on', 'their', 'category', 'For', 'example,', 'it', 'is', 'necessary', 'to', 'distinguish', 'a', 'year', 'like', '<year>1849</year>', 'from', 'a', 'PIN', 'like', '<pin>3269</pin>', 'Phone', 'numbers', 'come', 'in', 'variable', 'forms', 'like', '<phone>234-6529</phone>', 'or', '<phone>492-499-1349</phone>', 'or', '<phone>(203)893-5938</phone>', 'Zip', 'codes', 'can', 'also', 'vary', 'between', '<zip>29481</zip>', 'or', '<zip>49381-2395</zip>']
```

The NSW_markup function is partially filled in: it currently identifies some (but not all) zip codes. But it doesn't label the zip codes it finds; it only prints a message indicating it has found one. Modify and complete this function so that it 1) finds all of the instances of NSW, and 2) labels each one according to its category instead of printing the message.

Suggested approach:

1. Extend the provided is_zip function to find all of the zip codes.
2. Write an additional boolean function is_phone to identify phone numbers.
3. Distinguish four-digit sequences that are years from four-digit sequences that are PINs by scanning some window of words to the left and right. If the word 'PIN' appears in that window, classify the number as a PIN. Otherwise, classify it as a year. (Obviously, this is a naive method, but it will succeed in many cases!)

