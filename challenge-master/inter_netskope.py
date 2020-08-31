"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: ["music","muse","mule"]
Output: “mu”


Example 2:
Input: ["dog","","car"]
Output: ""


Explanation: There is no common prefix among the input strings.
Input: ["miss", "mission","mistake", "misunderstand"]
Output: "mis"
"""

def common_prefix(list1):
    common = ''
    fcommon =''
    index0 = 0
    index_next = 1
    word1 =list1[index0]
    llen = len(min(list1))
    wlen = len(list1)
    first_word = list1[0]
    for w in range (1,wlen):
        common = ''
        for l in range(llen):
            if list1[w][l] == first_word[l]:
                common=common+str(list1[0][l])
            fcommon = common
    return (common)
list1 = ["music","muse","mul","mut"]
#list1 = ["miss", "mission","mistake", "misunderstand"]
#list1 = ["dog","","car"]
result = common_prefix(list1)
if not result :
    print('\'\'')
else:
    print('\'',result,'\'')