
units = (('year', 3600*24*365), ('day', 3600*24), ('hour', 3600), ('minute', 60), ('second', 1))


def format_duration(seconds):

    if seconds == 0:
        return 'now'

    result = []

    for unit, value in units:
        amount = seconds // value
        if amount > 0:
            result.append('{} {}'.format(amount, unit) if amount == 1 else '{} {}s'.format(amount, unit))
            seconds = seconds % value

    if len(result) == 1:
        return result[0]
    return ' and '.join([', '.join(result[:-1]), result[-1]])
