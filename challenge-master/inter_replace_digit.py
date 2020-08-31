str = "California Sunday 01-07-1924, barak Monday00-04-2011"
outstr=""
for c in str:
    if c.isdigit():
        c = 'x'
    outstr +=  c
print (outstr)
