def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'
    """

    split_phrase = phrase.split(' ')
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_word = ''
    new_word_list = []


    for word in split_phrase:
    	if word[0] in vowels:
    		new_word = word + 'yay'
    		# print new_word
    		new_word_list.append(new_word)
    		
    	else:
    		new_word = word[1::] + word[0] + 'ay'
    		# print new_word
    		new_word_list.append(new_word)
    return ' '.join(new_word_list)

print pig_latin('hello kitty')