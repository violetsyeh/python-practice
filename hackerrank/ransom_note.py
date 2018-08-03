"""Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

For example, the note is "Attack at dawn". The magazine contains only "attack at dawn". The magazine has all the right words, but there's a case mismatch. The answer is 'No'.


"""
def checkMagazine(magazine, note):
    
    if len(magazine) < len(note):
        print 'No'
        exit

    magazine_dict = {}
    for word in magazine:
        if word in magazine_dict:
            magazine_dict[word] += 1
        elif word not in magazine_dict:
            magazine_dict[word] = 1
    
    note_list = list(note)
    check_flag = 'Yes'
    for word in note_list:
        if word not in magazine_dict.keys():
            check_flag = 'No'
        elif word in magazine_dict.keys() and magazine_dict[word] > 0:
            magazine_dict[word] -= 1
        else:
            check_flag = 'No'
            
            
                
    print check_flag

if __name__ == '__main__':
    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = raw_input().rstrip().split()

    note = raw_input().rstrip().split()

    checkMagazine(magazine, note)