input_tuple = input().split(',')
N, M = int(input_tuple[0]), int(input_tuple[1])

len_N = len(str(N))
len_sqr_N = len(str(N ** 2))
col = (M + 3) // (2 * len_N + len_sqr_N + 9)

num = 1
N += 1
sep = '=' * M

print(sep)
while num < N:
    for j in range(1, N):
        edge = min(num + col, N)
        for i in range(num, edge):
            print(f'{str(i).rjust(len_N)} * {str(j).ljust(len_N)} = {str(i * j).ljust(len_sqr_N)}', end='')
            if i != edge - 1:
                print(" | ", end='')
        print()
    print(sep)
    num += col
