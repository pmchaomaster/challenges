input_string = 'abc'
length = len(input_string)
for i in range (length):
  for j in range (i,length):
    print ("=================")
    print (i, j)
    print (input_string[i:j+1])
