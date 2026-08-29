class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i = 0 
        j = len(people) - 1
        people.sort()
        ans = 0
        while i <= j:
            diff = limit - people[j]
            if people[i] <= diff:
                i+=1
                j-=1
            else:
                j-=1

            ans += 1
            
        return ans
            
            
