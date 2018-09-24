def letter_frequency(sentence):
    frequency={}
    for letter in sentence:
        val=frequency.setdefault(letter,0)
        frequency[letter]=val+1
    return frequency

freq=letter_frequency("Helllo How are you")
print(freq)