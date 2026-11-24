import numpy as np

def make_hours():
    return np.arange(0,22,3).tolist()


def vector_report(a):
    s = np.asarray(a)
    return {
        'third': float(s[2]),
        'last':  float(s[-1]),
        'middle': s[2:6].tolist(),
        'every_second': s[::2].tolist(),
        'reversed': s[::-1].tolist(),
    }

def cap_above(s,lim):
    a = np.asarray(s).copy()
    a[a > lim] = lim
    return a.tolist()

def change_vector(s):
    a = np.asarray(s).copy()
    a[2:5]= 99
    a[::2]= -1
    return a.tolist()

def celsius_to_fahrenheit(s):
    a = np.asarray(s)
    fahrenheit = a * 9/ 5 + 32
    return fahrenheit.tolist()

print(vector_report(make_hours()))
print(make_hours())
print(cap_above(make_hours(), 10))
print(change_vector(make_hours()))
print(celsius_to_fahrenheit(make_hours()))


