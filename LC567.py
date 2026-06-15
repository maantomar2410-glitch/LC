def permutation(s1,s2):
        if len(s1) > len(s2):
            return False
        check = {}
        for i in s1:
            if i in check:
                check[i] = check[i] + 1
            else:
                check[i] = 1
        check_s2 = {}
        for i in range(len(s1)):
            if s2[i] in check_s2:
                check_s2[s2[i]] = check_s2[s2[i]] + 1
            else:
                check_s2[s2[i]] = 1

        for i in range(len(s2) - len(s1) + 1):
            if check == check_s2:
                return True
            else:
                if i == len(s2) - len(s1):
                    break

                if s2[i + len(s1)] in check_s2:
                    check_s2[s2[i + len(s1)]] = check_s2[s2[i + len(s1)]] + 1
                else:
                    check_s2[s2[i + len(s1)]] = 1
                
                check_s2[s2[i]] = check_s2[s2[i]] - 1
                if check_s2[s2[i]] == 0:
                    del check_s2[s2[i]]
                    
        return False