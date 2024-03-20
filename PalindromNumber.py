 word = str(x)
        l = 0
        r = len(word) - 1
        while(l < len(word)):
            if not word[l] == word[r]:
                return False
            else:
                l+=1
                r-=1
        return True  
