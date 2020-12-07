"""
input = "aaabbccccd"
output = a3b2c3d1

"""
output=""
input = "aaabbccccd"
len_input = len(input)-1
for n in range(len_input):
#    print(n)
    print(input[n])
    if (input[n]!= input[n+1]) or n+1 == len_input:
    #if (input[n]!= input[n+1]) :
       output =output+input[n]+str(n)
    print(output)
print ("Conclud")