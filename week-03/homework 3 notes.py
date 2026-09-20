# TO DO: WRITE YOUR CODE/SOLUTION BELOW
def letter_score(letter):
    scrabble = {
        "1": ['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u'],
        "2": ['d', 'g'], 
        "3": ['b', 'c', 'm', 'p'],
        "4": ['f', 'h', 'v', 'w', 'y'],
        "5": ['k'],
        "8": ['j', 'x'],
        "10": ['q', 'z']
    }
    
    for key, value in scrabble.items():
        if letter in value:
            return int(key)

    return 'Not an eligible Scrabble score.'