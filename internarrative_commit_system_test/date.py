import math
import datetime
import sys

def get_g_month_length(g_month, g_year):
    if g_month != 2:
        return [None, 31, None, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][g_month]
    else:
        return 28 + (g_year % 4 == 0 and (
        g_year % 100 != 0 or g_year % 400 == 0))

def get_ts_total_seasons(ts_season, ts_year):
    return (ts_season - 1) + 4 * (ts_year - 1)

def get_ts_equinox_length(ts_total_seasons):
    c1 = ts_total_seasons % 3 == 0
    c2 = ts_total_seasons % 44 == 0
    return 1 + c1 - c2

def get_ts_lunar_equinox_length(ts_total_seasons):
    c1 = ts_total_seasons % 3 == 0
    c2 = ts_total_seasons % int(math.log(2, 10) * 1024) == 0
    return 1 - c1 + c2

def next_day(g_day, g_month, g_year, ts_day, ts_month, ts_equinox, ts_season,
ts_year, ts_lun_day, ts_lun_count, ts_lun_year):
    # simple
    if g_day != get_g_month_length(g_month, g_year):
        r_g_day = g_day + 1
        r_g_month = g_month
        r_g_year = g_year
    elif g_month != 12:
        r_g_day = 1
        r_g_month = g_month + 1
        r_g_year = g_year
    else:
        r_g_day = 1
        r_g_month = 1
        r_g_year = g_year + 1
    # complicated
    if ts_equinox:
        lun_day_jump = get_ts_lunar_equinox_length(get_ts_total_seasons(
        ts_season, ts_year)) / 2
        if ts_day != get_ts_equinox_length(get_ts_total_seasons(
        ts_season, ts_year)):
            r_ts_day = ts_day + 1
            r_ts_month = ts_month
            r_ts_equinox = ts_equinox
            r_ts_season = ts_season
            r_ts_year = ts_year
        else:
            r_ts_day = 1
            r_ts_month = 1
            r_ts_equinox = False
            r_ts_season = ts_season
            r_ts_year = ts_year
    else:
        if ts_day != 30:
            lun_day_jump = 1
            r_ts_day = ts_day + 1
            r_ts_month = ts_month
            r_ts_equinox = ts_equinox
            r_ts_season = ts_season
            r_ts_year = ts_year
        elif ts_month != 3:
            lun_day_jump = 1
            r_ts_day = 1
            r_ts_month = ts_month + 1
            r_ts_equinox = ts_equinox
            r_ts_season = ts_season
            r_ts_year = ts_year
        else:
            skip_equinox = get_ts_equinox_length(get_ts_total_seasons(
            ts_season + 1, ts_year)) == 0
            new_year = ts_season == 4
            lun_day_jump = get_ts_lunar_equinox_length(get_ts_total_seasons(
            ts_season + 1, ts_year)) / (1 if skip_equinox else 2)
            r_ts_day = 1
            r_ts_month = 1 if skip_equinox else None
            r_ts_equinox = not skip_equinox
            r_ts_season = 1 if new_year else ts_season + 1
            r_ts_year = ts_year + 1 if new_year else ts_year
    r_ts_lun_day = (ts_lun_day + lun_day_jump) % 29
    if r_ts_lun_day < ts_lun_day:
        if r_ts_year == ts_lun_year:
            r_ts_lun_count = ts_lun_count + 1
            r_ts_lun_year = ts_lun_year
        else:
            r_ts_lun_count = 1
            r_ts_lun_year = r_ts_year
    else:
        r_ts_lun_count = ts_lun_count
        r_ts_lun_year = ts_lun_year
    return r_g_day, r_g_month, r_g_year, r_ts_day, r_ts_month, \
    r_ts_equinox, r_ts_season, r_ts_year, r_ts_lun_day, r_ts_lun_count, \
    r_ts_lun_year

def main(x):
    now = tuple(int(i) for i in x.split('/'))
    # d = 13, 12, 2012, 23, 3, False, 4, 0, 0.0, 13, 0
    # the below is equivalent to the above
    d = 26, 12, 2011, 4, 1, False, 1, 0, 0.0, 1, 0
    desc = ('day', 'month', 'year', 'day', 'month', 'equinox?',
    'season', 'year', 'lunar day', 'lunar month', 'lunar year')
    while True:
        '''
        if (d[3], d[4], d[6]) == (30, 3, 4) and d[-4] % 77 == 0 and d[-4] % 3 != 0 and d[-3] == 28:
            for i, j in zip(desc, d):
                print(f'{i}: {j}')
            print('\n')
        if (d[3], d[4], d[6]) == (1, 1, 1) and d[-4] % 77 == 1 and d[-4] % 3 != 1 and d[-3] == 1:
            for i, j in zip(desc, d):
                print(f'{i}: {j}')
            print('\n')
        if d[-3] in (28.5, 0.5) and 840 > d[-4] > 630:
            for i, j in zip(desc, d):
                print(f'{i}: {j}')
            print('\n')
        '''
        if d[:3] == now:
            for i, j in zip(desc, d):
                print(f'{i}: {j}')
            break
        d = next_day(*d)

if __name__ == '__main__':
    main(sys.argv[1])
