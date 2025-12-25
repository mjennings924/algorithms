# A string is given. We have to print the reversed string.
# For example, the string is "Hi how are you?"
# The output should be "?ouy era woh iH"

def simple_reverse(string):
    new_string = []
    for i in range(len(string)-1, -1, -1):
        new_string.append(string[i])
    return ''.join(new_string)

string = "You want to wake up in the morning and think the future is going to be great - and that's what being a spacefaring civilization is all about. It's about believing in the future and thinking that the future will be better than the past. And I can't think of anything more exciting than going out there and being among the stars. -Elon Musk"
print(string)
print(simple_reverse(string))
