class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.replace(" ", "").lower()
        print(string)
        i , j = 0, len(string) - 1

        while i < j:
            if not string[i].isalpha() and not string[i].isdigit():
                i+=1
            elif not string[j].isalpha() and not string[j].isdigit():
                j-=1
            elif string[i] != string[j]:
                return False
            else:
                i+=1
                j-=1
        return True
