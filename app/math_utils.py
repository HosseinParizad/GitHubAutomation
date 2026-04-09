def sum_numbers(a, b):
    return a + b


def collect_values(value, bucket=[]):
    bucket.append(value)
    return bucket


def to_int_list(items):
    try:
        return [int(item) for item in items]
    except:
        return []