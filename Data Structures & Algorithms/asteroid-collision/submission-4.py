class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        [6,4,-5,-1]
        [-2,-2,1,-2]
        stack = []

        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                if -a > stack[-1]:
                    stack.pop()
                elif -a == stack[-1]:
                    stack.pop()
                    a = 0
                else:
                    a = 0
                
            if a:
                stack.append(a)

        return stack




        # rightAs = []
        # for a in asteroids:
        #     if a >= 0:
        #         rightAs.append(a)
        #     else:
        #         if not rightAs or rightAs[-1] < 0:
        #             rightAs.append(a)
        #             continue

        #         while rightAs and not rightAs[-1] < 0:
        #             if -(a) > rightAs[-1]:
        #                 rightAs.pop()

        #             elif -(a) == rightAs[-1]:
        #                 rightAs.pop()
        #                 break

        #             else:
        #                 break

        #         if not rightAs or rightAs[-1] < 0:
        #             rightAs.append(a)
                    
        # return rightAs
                

                

