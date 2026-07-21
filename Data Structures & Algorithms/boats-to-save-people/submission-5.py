class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat = 0
        left = 0
        right = len(people) - 1
        while left <= right:
            weight = people[left] + people[right]
            if weight <= limit:
                left += 1
        
            right -= 1
            boat += 1
          
        return boat


            


            
            
  





