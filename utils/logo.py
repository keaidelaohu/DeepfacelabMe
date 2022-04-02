def print_info():
    print ('')
    print_logo_info()
    print('')

def print_logo_info():
    print ('')
    tree_count=1
    width = 24
    for i in range(10):
        print(("*"*tree_count).center(width))
        tree_count +=2
    print("|@~@|".center(width))
    print ('-> Deeplacelab Me 2022sp1 Ver 2.41 - This RG version was edited by kingboy!(2022.3.28)')
