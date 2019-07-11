def levenshtein_dist_rec(s, t):

    len_s = len(s)
    len_t = len(t)

    def lev(source_len, target_len, source_str, target_str):

        if source_len == 0: return target_len
        if target_len == 0: return source_len

        if source_str[source_len- 1] == target_str[target_len- 1]:
            ind = 0
        else:
            ind = 1
        return min( lev(source_len-1, target_len, source_str, target_str)+1,
                    lev(source_len, target_len-1, source_str, target_str) + 1,
                    lev(source_len-1, target_len - 1, source_str, target_str) + ind)

    return lev(len_s, len_t, s, t)

def levenshtein_dist_dp(source, target):

    len_source = len(source)
    len_target = len(target)
    matrix = [[None for j in range(len_target+1)] for i in range(len_source+1)]

    for i in range(len_source + 1):
        for j in range(len_target+1):
            if i == 0:
                matrix[i][j] = j
            elif j == 0:
                matrix[i][j] = i
            else:
                if source[i-1] == target[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    matrix[i][j] = 1 + min(matrix[i][j-1],
                                           matrix[i-1][j],
                                           matrix[i-1][j-1])

    return matrix[len_source][len_target]

def main():
    strings = [("hello", "hello"), ("hello", "hell"), ("hello", "antidisetablishmentarianism"), ("poop", "pooppy")]

    for x in strings:
        print(str(x) + ": " + str(levenshtein_dist_rec(*x)))
    for x in strings:
        print(str(x) + ": " + str(levenshtein_dist_dp(*x)))


if __name__ == "__main__":
    main()
