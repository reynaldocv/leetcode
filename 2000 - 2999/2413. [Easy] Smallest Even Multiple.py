class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [0, 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        
        for i in range(2, 13):
            days[i] += days[i - 1]

        arriveAlice = days[int(arriveAlice[: 2])] + int(arriveAlice[3:])
        leaveAlice = days[int(leaveAlice[: 2])] + int(leaveAlice[3:])
        
        arriveBob = days[int(arriveBob[: 2])] + int(arriveBob[3:])
        leaveBob = days[int(leaveBob[: 2])] + int(leaveBob[3:])
        
        arrive = max(arriveAlice, arriveBob)
        leave = min(leaveAlice, leaveBob)
        
        if leave < arrive: 
            return 0 
        else: 
            return leave - arrive + 1
