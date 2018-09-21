units_high = ['', 'un', 'duo', 'tre$', 'quattuor', 'quinqua', 'se$', 'septe^', 'octo', 'nove^']

tens_high = ['', 'n deci', 'ms viginti', 'ns triginta', 'ns quadraginta', 'ns quinquaginta', 'n sexaginta', 'n septuaginta', 'mx octoginta', '* nonaginta']

hundreds_high = ['', 'nx centi', 'n ducenti', 'ns trecenti', 'ns quadringenti', 'ns quingenti', 'n sescenti', 'n septingenti', 'mx octingenti', '* nongenti']

special_units = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion']

very_small = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def thousand_to(x):
    if x < 11:
        return special_units[x]
    elif x < 1001:
        y = x - 1
        return concat(units_high[y % 10], tens_high[(y // 10) % 10], hundreds_high[(y // 100) % 10])
    else:
        raise Exception('Too large!')

special = {'$': 'sx', '^': 'mn'}

def concat(*l):
    ls = []
    for ind, i in enumerate(l):
        if i and (i[-1] in special):
            common = set(l[ind + 1].split(' ')[0]) & set(special[i[-1]])
            assert len(common) < 2
            ls.append(i.split(' ')[-1][:-1] + (list(common)[0] if common else ''))
        else:
            ls.append(i.split(' ')[-1])
    return ''.join(ls)[:-1] + 'illion'

def less_than_thousand(x):
    if x < 100:
        return less_than_hundred(x)
    elif x % 100 == 0:
        return very_small[x // 100] + ' hundred'
    else:
        return very_small[x // 100] + ' hundred and ' + less_than_hundred(x % 100)

def less_than_hundred(x):
    if x < 10:
        return very_small[x]
    elif x < 20:
        return teens[x - 10]
    elif x % 10 == 0:
        return tens[x // 10]
    else:
        return tens[x // 10] + '-' + very_small[x % 10]

def overall(x):
    l = []
    while True:
        if x < 1000:
            l.append(less_than_thousand(x))
            break
        p = 0
        q = 1
        while q < x:
            p += 1
            q *= 1000
        p -= 1
        q //= 1000
        l.append(less_than_thousand(x // q) + ' ' + thousand_to(p))
        x %= q
    return ' '.join(l)

import time
for i in range(0, 11):
    print()
    print(overall(2 ** 2 ** i))
    time.sleep(1)
