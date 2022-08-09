# https://leetcode.com/problems/move-pieces-to-obtain-a-string/

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.ranking = defaultdict(lambda: [])
        self.actualRankings = {}
        self.types = {}
        
        for (i, food) in enumerate(foods):
            cuisine = cuisines[i]
            rating = -ratings[i]
            
            heappush(self.ranking[cuisine], (rating, food))
            
            self.actualRankings[food] = rating
            self.types[food] = cuisine
            
    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.types[food]
        self.actualRankings[food] = -newRating
        heappush(self.ranking[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while self.ranking[cuisine] and self.actualRankings[self.ranking[cuisine][0][1]] != self.ranking[cuisine][0][0]:
            heappop(self.ranking[cuisine])
            
        return self.ranking[cuisine][0][1]
        
# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
