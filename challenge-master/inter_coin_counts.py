def rec_coin(target,coins):
    '''
    INPUT: Target change amount and list of coin values
    OutPut: Minimum coin needed to make change

    Note This solution is not optimized

    '''

    # Default to target value
    min_coins = target

    # Check base case
    if target in coins:
        return 1

    else:

        # for every coin value that is <= than target
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + rec_coin(target-i,coins)

            # Reset Minium if we have a new minium
            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins

result = rec_coin(40,[25,50])
print (result)





