#Find the largest word in a given string
#Examples
#Input: "fun&!! time"
#Output: time

#The simplest and easiest solution that comes to mind is :
#We check for every character if it is an alphanumeric character or not
#If it is, we increase a counter and update a variable which stores the maximum value of counter
#If we encounter a non-alphanumeric character, we reset the counter to zero and start again when the next alpha-numeric character arrives

def easy_longest_word(string):
    count = 0
    maximum = 0
    for char in string:
        if char.isalnum():
            count += 1
        else:
            maximum = max(maximum, count)
            count = 0
    maximum = max(maximum, count)
    return maximum

string = 'longest word'
print(easy_longest_word(string))


