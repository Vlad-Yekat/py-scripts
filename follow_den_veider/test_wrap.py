def second_wrap(func):
    def wrapper(*args, **kwargs):
        print('.'+func.__name__)
        new_func = func(*args, **kwargs)
        return new_func

    return wrapper


def first_wrap(func):
    def fwrapper(*args, **kwargs):
        print('..'+func.__name__)
        new_func = func(*args, **kwargs)
        return new_func

    return fwrapper


@second_wrap
@first_wrap
def some(*args):
    text1 = ''.join([z for z in args])
    print(text1)


some('...')

