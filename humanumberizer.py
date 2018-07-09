import sys


def split_into_parts(number):
    parts = []
    while number > 9:
        number, part = divmod(number, 10)
        parts.append(part)

    parts.append(number)
    return list(reversed(parts))


digits = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

edge_cases = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13:	'thirteen',
    14:	'fourteen',
    15:	'fifteen',
    16:	'sixteen',
    17:	'seventeen',
    18:	'eighteen',
    19:	'nineteen'
}

decimals = {
    20:	'twenty',
    30:	'thirty',
    40:	'forty',
    50:	'fifty',
    60:	'sixty',
    70:	'seventy',
    80:	'eighty',
    90:	'ninety'
}

def humanize(number):
    parts = split_into_parts(number)
    powers = [10 ** i for i in range(len(parts)-1, -1, -1)]
    # print(parts, powers)
    aside = 0
    needs_hyphen = False

    out = []
    for i, p in zip(powers, parts):
        if i == 100:
            out.extend([digits[p], 'hundred'])

            if parts[-1] == 0 and parts[-2] == 0:
                break
            out.append('and')
        elif i == 10:
            if parts[-1] == 0:
                out.append(decimals[p*i])
                break
            elif p == 0:
                continue
            elif p > 1:
                out.append(decimals[p*i])
                needs_hyphen = True
            elif p == 1:
                aside = 10
        else:
            out.append(edge_cases.get(p+aside, digits[p]))
    str_out = ' '.join(map(str, out))
    if needs_hyphen:
        str_out = '-'.join(str_out.rsplit(' ', 1))
    print(str_out)




if __name__ == '__main__':
    humanize(int(sys.argv[1]))
