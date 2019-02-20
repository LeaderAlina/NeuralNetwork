import numpy as np

w = np.array([[0, 0, 0]])

examples = np.array([[1, 1, 0.3], [1, 0.4, 0.5], [1, 0.7, 0.8]])

def target(ex):
    if ex[1] == 1 and ex[2] == 0.3:
        return 1
    elif ex[1] == 0.4 and ex[2] == 0.5:
        return 1
    elif ex[1] == 0.7 and ex[2] == 0.8:
        return 0

def predict(example):
    sum = example[0] * w[0][0] + example[1] * w[0][1] + example[2]*w[0][2]
    if sum > 0:
        return 1
    else:
        return 0

i = 10
perfect = False
while not perfect:
    # print(i)
    j = 1
    i += 10
    perfect = True
    for e in examples:
        if predict(e) != target(e):
            # print(j)
            # print("e", e)
            perfect = False
            if predict(e) == 0:
                w = w + e
                # print("w", w)
            else:
                w = w - e
                # print("w ", w)
        j += 1
print("final answer", w)