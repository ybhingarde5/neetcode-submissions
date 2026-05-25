class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        kvp = {}

        for s in strs:
            key = tuple(list(sorted(s)))
            if key in kvp:
                kvp[key].append(s)
            else:
                kvp[key] = [s]
            
        return list(kvp.values())


























        # ans = []
        # visited = set()

        # for i in range(len(strs)):
            
        #     if i in visited:
        #         continue
                
        #     anagram = [strs[i]]


        #     for j in range(i+1, len(strs)):

        #         if sorted(strs[i]) == sorted(strs[j]):
                    
        #             anagram.append(strs[j])
        #             visited.add(j)

        #     ans.append(anagram)
        
        # return ans

                




