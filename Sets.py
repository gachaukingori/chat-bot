#SETS unordered collection without duplicate element
#use {} or set() to create

vowels = {'a','e','i','o','u'}
empty = set()
print(empty)

alphabets = {'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'}
consonants = alphabets - vowels
print(consonants)

#MEMBERSHIP
print('a' in consonants) #false
print('a' in alphabets)  #true

#in vowels or in consonants or both (UNION)
print(vowels | consonants) #alphabets randomly

# in vowels or alphabets but not in both
print(vowels ^ alphabets) #consonants
print(vowels^consonants) #prints alphabets
print(alphabets^consonants) #prints vowels
# IN BOTH A AND B (INTERSECTION)
print(vowels & consonants) #empty set
print(vowels & alphabets) #vowels
print(alphabets & consonants)  #consonants
