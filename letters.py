letters = ['a','b','c','d','e','f','g','h','i','j', \
    'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print(letters)
f = open("letters.txt", "w")
 
for letters_1 in letters:
    for letters_2 in letters:
        for letters_3 in letters:
            print(letters_1 + letters_2 + letters_3)
            f.write(letters_1 + letters_2 + letters_3 + '\n')
f.close()




        


