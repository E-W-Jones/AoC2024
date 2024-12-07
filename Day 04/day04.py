XMAS = ['X', 'M', 'A', 'S']
SAMX = ['S', 'A', 'M', 'X']

def read_wordsearch(filename):
    with open(filename) as filein:
        return [list(line.strip('\n')) for line in filein.readlines()]

def log(*args, verbose):
    if verbose:
        print(*args)

def word_count(wordsearch, word, i, j, m, verbose=False):
    count = 0
    if j < N-3:
        if [wordsearch[i][j+n] for n in range(m)] == word:
            log(i, j, 'right', verbose=verbose)
            count += 1
    if j > 2:
        if [wordsearch[i][j-n] for n in range(m)] == word:
            log(i, j, 'left', verbose=verbose)
            count += 1
    if i < N-3:
        if word == [wordsearch[i+n][j] for n in range(m)]:
            log(i, j, 'down', verbose=verbose)
            count += 1
    if i > 2:
        if word == [wordsearch[i-n][j] for n in range(m)]:
            log(i, j, 'up', verbose=verbose)
            count += 1
    if i < N-3 and j < N-3:
        if word == [wordsearch[i+n][j+n] for n in range(m)]:
            log(i, j, 'down and right', verbose=verbose)
            count += 1
    if i < N-3 and j >= 3:
        if word == [wordsearch[i+n][j-n] for n in range(m)]:
            count += 1
            log(i, j, 'down and left', verbose=verbose)
    if i >= 3 and j < N-3:
        if word == [wordsearch[i-n][j+n] for n in range(m)]:
            count += 1
            log(i, j, 'up and right', verbose=verbose)
    if i >= 3 and j >= 3:
        if word == [wordsearch[i-n][j-n] for n in range(m)]:
            count += 1
            log(i, j, 'up and left', verbose=verbose)
    return count

def MAS_count(wordsearch, i, j, m=3, verbose=False, word=['M', 'A', 'S'], offset=-1):
    count = 0
    M = []
    if [wordsearch[i][j+n] for n in range(offset, m+offset)] == word:
        log(i, j, 'right', verbose=verbose)
        count += 1
        M.append((0, -1))
    if [wordsearch[i][j-n] for n in range(offset, m+offset)] == word:
        log(i, j, 'left', verbose=verbose)
        count += 1
        M.append((0, 1))
    if word == [wordsearch[i+n][j] for n in range(offset, m+offset)]:
        log(i, j, 'down', verbose=verbose)
        count += 1
        M.append((-1, 0))
    if word == [wordsearch[i-n][j] for n in range(offset, m+offset)]:
        log(i, j, 'up', verbose=verbose)
        count += 1
        M.append((1, 0))
    if word == [wordsearch[i+n][j+n] for n in range(offset, m+offset)]:
        log(i, j, 'down and right', verbose=verbose)
        count += 1
        M.append((-1, -1))
    if word == [wordsearch[i+n][j-n] for n in range(offset, m+offset)]:
        count += 1
        log(i, j, 'down and left', verbose=verbose)
        M.append((-1, 1))
    if word == [wordsearch[i-n][j+n] for n in range(offset, m+offset)]:
        count += 1
        log(i, j, 'up and right', verbose=verbose)
        M.append((1, -1))
    if word == [wordsearch[i-n][j-n] for n in range(offset, m+offset)]:
        count += 1
        log(i, j, 'up and left', verbose=verbose)
        M.append((1, 1))
    return count, M

def is_reflection(x1, y1, x2, y2):
    # #   2
    # # 1 . 1
    # #   2
    # if x1 == 0 and y1 != 0 and x2 != 0 and y2 == 0:
    #     return True
    # 1 . 2
    # . . .
    # 2 . 1
    if x1 == y1 and x2 == -y2:
        return True

def search_xmas(wordsearch, N):
    count = 0
    for i in range(N):
        for j in range(N):
            count += word_count(wordsearch, XMAS, i, j, len(XMAS))
    return count

def search_mas(wordsearch, N):
    count = 0
    for i in range(1, N-1):
        for j in range(1, N-1):
            _, Ms = MAS_count(wordsearch, i, j)
            for M1 in Ms:
                for M2 in Ms:
                    if M1 == M2:
                        continue
                    if is_reflection(*M1, *M2):
                        # print(i, j, M1, M2)
                        count += 1
            
            # if count > 0:
            #     print(Ms)
            #     print(wordsearch[i-1][j-1], wordsearch[i-1][j], wordsearch[i-1][j+1], '\n',
            #           wordsearch[i][j-1], wordsearch[i][j], wordsearch[i][j+1], '\n',
            #           wordsearch[i+1][j-1], wordsearch[i+1][j], wordsearch[i+1][j+1], '\n', sep='')
    return count

wordsearch = read_wordsearch('input.txt')
N = len(wordsearch)

print(search_xmas(wordsearch, N))
print(search_mas(wordsearch, N))