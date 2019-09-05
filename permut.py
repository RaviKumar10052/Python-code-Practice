from itertools import permutations
import pronouncing
def allPermutations(str):
    permList = permutations(str,5)
    count=1
    for perm in list(permList):
        print(''.join(perm))
        count=count+1
        if(count==5000):
            print(count)
            break

str = 'bcdfghjklmnpqrstvwxyz'
allPermutations(str)