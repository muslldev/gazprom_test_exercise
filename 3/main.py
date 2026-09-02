from functools import reduce

def get_nested_value_reduce(data, path):
    try:
        return reduce(lambda d,key: d[key], path.split('.'),data)
    except (KeyError,TypeError,IndexError):
        return None

if __name__ == '__main__':
    obj = {
        'a': {
            'b': {
                'c': '+++'
            }
        }
    }

    print(get_nested_value_reduce(obj,'a.b.c'))