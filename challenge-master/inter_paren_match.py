def balance_check(s):

    if len(s)%2 !=0:
        return 'No Match'

    opening = set('([{')

    #matches = set([('(',')'),('[',']'),('{','}')] )
    matches = set([('(',
                    ')'),
                   ('[',
                    ']'),
                   ('{',
                    '}')])

    stack =[]
    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return '2 No Match'
            last_open = stack.pop()

            if (last_open,paren) not in matches:
                return '1No Match'

    return len(stack) == 0,'YES'

#res=balance_check('[]]')
#res=balance_check('[{]')
res=balance_check('{[}]}')


print "concluded!",res
