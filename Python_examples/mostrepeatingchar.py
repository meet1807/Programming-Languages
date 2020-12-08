# Find the most reapeating character in the given string
# input = "This is a common interview question"


# Time complexity : O(N)
# Space complexity : O(N)

def findMostReapeatedChar(input):

    # check if the string is empty or not
    if not input:
        return -1
    # use hashmap key = charcter and value = how many times it repeated
    input_dict = dict()
    for i in input:  # time O(N)  space O(N)
        if i in input_dict:
            input_dict[i] += 1
        elif i != ' ':
            input_dict[i] = 1

    # sort the hashmap in descending order :
    # covert the dict key,value pairs to tuples and save them in list to sort
    # return the key of highest reapeated value
    ans = sorted(input_dict.items(),  # time O(N)   sapce O(1)
                 key=lambda item: item[1], reverse=True)[0][0]
    return ans


    # ans = sorted(key=lambda item: item[1], input_dict.items())
input = "This is a common interview question"
print(findMostReapeatedChar(input))
