import pandas as pd
import numpy as np

pair = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 24]
rss = []

for i in pair:

    pairnum = i

    if i % 2 == 0:
        num = 1
    else:
        num = 0

    num = pd.Series([num])

    filename = "data_feature/pair" + str(pairnum) + "_fea.csv"
    df = pd.read_csv(filename)
    nose_to_nose = df["nose_to_nose"]
    samples_per_split = 139
    no_splits = int(df.shape[0] / samples_per_split)

    for t in range(0, no_splits):
        frame = df["nose_to_nose"].loc[
            (t) * samples_per_split : (t + 1) * samples_per_split
        ]

        frame = pd.concat([num, frame])
        rss.append(frame)

rss = np.array(rss)
np.savetxt('test.out', rss, delimiter=',')
