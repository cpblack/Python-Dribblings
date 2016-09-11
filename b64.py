import base64
def encode(stringIn,layers):
    t = 0
    m = stringIn
    while len(m) % 4 > 0:
        m = m+"="
    while t < layers:
        m = base64.b64encode(m)
        t = t + 1
    return m
def decode(stringIn,layers):
    t = 0
    m = stringIn
    while t < layers:
        m = base64.b64decode(m)
        t = t + 1
    while m[-1:] == "=":
        m = m[:-1]
    return m
