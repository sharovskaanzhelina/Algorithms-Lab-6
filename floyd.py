INF = 9999999

def floyd(W):
    n = len(W)
    D = [row[:] for row in W]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
    return D

W = [
    [0,   6,   2,   4,   INF, INF, INF, INF],
    [6,   0,   INF, 6,   INF, 6,   INF, INF],
    [2,   INF, 0,   INF, INF, INF, INF, 4  ],
    [4,   6,   INF, 0,   1,   INF, INF, INF],
    [INF, INF, INF, 1,   0,   4,   7,   INF],
    [INF, 6,   INF, INF, 4,   0,   5,   3  ],
    [INF, INF, INF, INF, 7,   5,   0,   5  ],
    [INF, INF, 4,   INF, INF, 3,   5,   0  ]
]

D = floyd(W)

print("Матриця найкоротших відстаней D (алгоритм Флойда):")
header = "    " + "".join(f"{i+1:>4}" for i in range(len(D)))
print(header)
for i, row in enumerate(D):
    print(f"{i+1:>2}: " + "".join(f"{val:>4}" for val in row))