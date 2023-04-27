words = [
    'kajak',
    'pająk',
    'ala ma kota',
    'abccba'
]
palindromes = []
def is_palindrome(items) :
    # prints which of given words are a palindrome
    for item in items:
        if item == item[::-1]:
            palindromes.append(item)
    return
is_palindrome(words)
print(palindromes)