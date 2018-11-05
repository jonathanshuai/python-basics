dictionary = {
    'apple',
    'pie',
    'cake',
    'p'
}


# Create a memo which tells us the solution for any call w/ substring
memo = dict()


def result_recorder(f):
    def g(arg):
        result = f(arg)
        memo[arg] = result
        return result

    return g

# @result_recorder
def break_word(word):
    # If word is already in the dictionary, just return it
    if word in dictionary:
        return word

    # If we've done this subproblem before, return the solution
    if word in memo:
        return memo[word]

    n_chars = len(word)
    
    # Iterate through the characters of word
    for i in range(n_chars):
        # If word[:i] in the dictionary, we should check if we can 
        # split word[i:] into dictionary words...
        if word[:i] in dictionary:
          
            # Check the case that word[i:] is dictionary word. If it is,
            # we already win!!
            if word[i:] in dictionary:
                solution = [word[:i], word[i:]]
                # memo[word] = solution
                return solution
            else:
                # Otherwise, we try to break up the rest of the string
                # into dictionary words. 
                subwords_list = break_word(word[i:])
                if len(subwords_list) > 0:
                    solution = [word[:i]] + subwords_list
                    # memo[word] = solution
                    return solution

    # if we get to the end and we never find an i s.t. 
    # word[:i] is a dictionary word and word[:i] is in dictionary
    # return an empty list
    # memo[word] = []
    return []

print(break_word('applepie'))
print(break_word('applepiecake'))
print(break_word('apple'))


