import math


def converter(dd):
    letter = "W" if dd < 0 else "E"
    dd = abs(dd)
    frac, whole = math.modf(dd)
    minutes = abs(frac * 60)
    if minutes == 0:
        minutes = int(minutes)
    else:
        minutes = round(minutes, 3)
    return f'{int(whole)}^{minutes}{letter}'
