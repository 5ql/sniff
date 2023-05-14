import string

expected_ic = {'English': 0.0667, 'French': 0.0778, 'German': 0.0762, 'Spanish': 0.0727}

text = input("Enter a string to calculate the index of coincidence: ").translate(str.maketrans('', '', string.punctuation)).replace(" ", "").upper()

freq = {char: text.count(char) for char in text}
ic = sum([freq[char]*(freq[char]-1) for char in freq])/float(len(text)*(len(text)-1))

language = next((lang for lang, expected_ic in expected_ic.items() if abs(ic - expected_ic) < 0.01), None)

print("The index of coincidence for the input string is: {:.3f}".format(ic))
print("The input string is likely in {}.".format(language) if language else "The language of the input string could not be determined.")
