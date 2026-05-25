class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        ans = []
        visited = set()

        for i in range(len(strs)):
            
            if i in visited:
                continue
                
            anagram = [strs[i]]


            for j in range(i+1, len(strs)):

                if sorted(strs[i]) == sorted(strs[j]):
                    
                    anagram.append(strs[j])
                    visited.add(j)

            ans.append(anagram)
        
        return ans

                




