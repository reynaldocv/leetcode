# https://leetcode.com/problems/minimum-sideway-jumps/

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        sidejump = 0
        cur_lane = 2
        backup_lane = None
        ob_last = 0
        for ob in obstacles[1:]:
            if backup_lane != None and ob == backup_lane:
                backup_lane = None
            if ob == cur_lane:
                if backup_lane != None:
                    cur_lane = backup_lane
                    backup_lane = None
                elif ob_last == 0:
                    sidejump += 1
                    cur_lane = cur_lane + 1 if cur_lane < 3 else 1
                    backup_lane = cur_lane + 1 if cur_lane < 3 else 1
                else:
                    sidejump += 1
                    cur_lane = cur_lane + 1 if cur_lane < 3 else 1
                    cur_lane = cur_lane + 1 if cur_lane == ob_last else cur_lane
                    cur_lane = 1 if cur_lane > 3 else cur_lane
            ob_last = ob
                
        return sidejump
