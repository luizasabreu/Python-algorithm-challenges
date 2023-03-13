"""Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. 
Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
"""
from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        city_dictionary = {}
        destinations = []
        for city in paths:
            origin = city[0]
            destination = city[1]
            if origin in city_dictionary.keys():
                city_dictionary[origin].append(destination)
            else:
                city_dictionary[origin] = destination
            destinations.append(destination)
        
        for destination in destinations: 
            if destination not in city_dictionary.keys():
                return destination

        
    



solution = Solution()
input = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(solution.destCity(input))