from typing import List

from string import ascii_lowercase

# Take the block of text provided and strip off the whitespace at both ends.
# Split the text by newline (\n).
# Loop through the lines, for each line:
# strip off any leading spaces,
# check if the first character is lowercase,
# if so, split the line into words and get the last word,
# strip off BOTH the trailing dot (.) and exclamation mark (!) from this last word,
# and finally add it to the results list.
# Return the results list.

another_text = """
Take the block of text provided and strip() off the whitespace at the ends.
Split the whole block up by newline (\n).
 if the first character is lowercase, split it into words and add the last word
of that line to the results list.
Strip the trailing dot (.) and exclamation mark (!) from the word first.
  finally return the results list!
"""

TEXT = """
One really nice feature of Python is polymorphism: using the same operation
on different types of objects.
Let's talk about an elegant feature: slicing.
You can use this on a string as well as a list for example
'pybites'[0:2] gives 'py'.
 The first value is inclusive and the last one is exclusive so
here we grab indexes 0 and 1, the letter p and y.
  When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
but here is the kicker: you can use this on a list too!
['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
and now you know about slicing from the end as well :)
keep enjoying our bites!
"""


def slice_and_dice(text: str = TEXT) -> List[str]:
    """
    Get a list of words from the passed in text.
    See the Bite description for step by step instructions
    """
    results = []
    
    lines = TEXT.strip().split("\n") # Removes all kinds of spaces and splits lines in Win environment (.split() in UNIX)
        
    for line in lines:
        
        line = line.lstrip() # Remove leading spaces
        
        if line[0] in ascii_lowercase:
            
            words = line.split()
            
            last_word = words[-1]
            
            last_word_stripped = last_word.rstrip(".!") # Remove from the end of the words
            
            results.append(last_word_stripped)
            
    return print(results)

slice_and_dice(another_text)

