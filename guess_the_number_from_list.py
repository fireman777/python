
def guess_the_number():
    '''This code finds a number in a list.

       Then prints it's position'''

    #variables
    nums=[5,4,1,777,9,6,16,37,12434,13]
    a=int(input('input value: '))

    if (a in nums):
        c=(nums.index(a))
        print('{} exists in the list on the {} position'.format(a,c+1))
        i=0
        while i<10:
            i+=1
            print(i,'\t', end='')
        print()
        i=0
        while i<10:
            if (i==c):
                print('[',nums[i],']', '\t', sep='', end='')
            else:
                print(nums[i], '\t', end='')
            i+=1
    else:
        print('{} not in the list.'.format(a))

guess_the_number()
print()
print(guess_the_number.__doc__)
