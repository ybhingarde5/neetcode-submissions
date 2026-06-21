class Solution:
    def validPalindrome(self, s: str) -> bool:
        sen = s.replace(" ","").lower()
        i, j = 0, len(sen) -1

        while i < j:
            if sen[i] == sen[j]:
                i+=1
                j-=1
            else:
                return self.isPalindrome(i, j-1, sen) or self.isPalindrome(i+1, j, sen)
        
        return True
    
    def isPalindrome(self,i,j, sen):
        while i < j:
            if sen[i] == sen[j]:
                i+=1
                j-=1
            else:
                return False
        
        return True

        
    
