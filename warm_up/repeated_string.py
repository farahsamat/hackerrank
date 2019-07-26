# s = 'kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm'
# n = 736778906400 #answer = 51574523448

# s = 'afcfffaged'
# n = 962645758455 #answer = 192529151691

s = 'aedbdaeaddadddcedcbbabdccbecaecaccdbebeeadadcaabbaabbaeeeecaddbcdecbbdccdebaaebecdaaabbcdeccbabaabce'
n = 731869010806  # answer = 168329872486


def repeatedString(s, n):
    if 'a' in s:
        if len(s) == 1:
            return n
        else:
            sum_a = s.count('a') * int(n / len(s))
            if n % len(s) == 0:
                return sum_a
            else:
                remainder = int(n % len(s))
                s_new = s[0:remainder]
                return sum_a + s_new.count('a')
    else:
        return 0


print(repeatedString(s, n))
