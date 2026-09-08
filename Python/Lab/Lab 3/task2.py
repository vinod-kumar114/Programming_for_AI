""" Two strings are called anagrams if they contain the same characters with the same frequencies, but the characters may appear in a different order. 
Write a program to determine whether two given strings are anagrams. 
• Create a function named is_anagram(s, t).  
• Compare the frequency of each character in both strings.  
• Return True if the strings are anagrams; otherwise return False."""


def is_anagram(s,t):

    l1 = []
    l2 = []
    for i in s.lower():
        l1.append(i)
    for i in t.lower():
        l2.append(i)

    s1= set(l1)
    s2= set(l2)
    
    if s1==s2:
        return 1
    else:
        return 0

print(is_anagram("vinko","dVoin"))
print(is_anagram("Ali","lia"))