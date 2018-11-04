# simple examle how decorator work

def new_func(old_func):
    def inside():
        # old_func()
        print('new')
    return inside


@new_func
def old_func():
    print('old')

old_func()
