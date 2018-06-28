"""Write a function that takes in a dictionary of titles and authors, and store it into
a dictionary of authors and their titles.

	>>> make_library({'Learn Java' : 'John', 'Learn C#': 'Reba', 'Learn Python' : 'JOHN', 'Learn PHP' : 'john'})
	{'John': ['Learn Python', 'Learn PHP', 'Learn Java'], 'Reba': ['Learn C#']}


"""

def make_library(books):

	library = {}

	for title, author in books.items():
		cap_author = author.capitalize()
		if cap_author in library:
			library[cap_author] += [title]
		elif cap_author not in library:
			library[cap_author] = [title]
	return library



if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. HOORAY!\n"