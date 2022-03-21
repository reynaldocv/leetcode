# https://leetcode.com/problems/longest-substring-of-one-repeating-character/

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
    
        ans = []
        d = defaultdict(list)
        f = defaultdict(int)
        ii = 0
        n = len(s)
        s = list(s)
        maxl=1
        while ii<n:

            l = 1
            while ii+l<n and s[ii+l]==s[ii]: l+=1
            d[s[ii]].append([ii, ii+l-1])
            f[l] += 1
            maxl = max(l, maxl)
            ii += l

        for c, ind in zip(queryCharacters[:], queryIndices[:]):


            if c!=s[ind]:
                #print(d[c], [ind, n])
                ip = bisect_right(d[c], [ind, n])
                if ip>0: l1= d[c][ip-1][1]-d[c][ip-1][0]+1
                if ip<len(d[c]): l2=d[c][ip][1]-d[c][ip][0]+1
                if ip>0 and ind==d[c][ip-1][1]+1 and (ip<len(d[c]) and ind==d[c][ip][0]-1):

                    d[c] = d[c][:ip-1] + [[d[c][ip-1][0], d[c][ip][1]]]+d[c][ip+1:]
                    f[l1]-=1
                    f[l2]-=1
                    f[l1+l2+1]+=1
                    maxl = max(maxl, l1+l2+1)
                elif ip>0 and ind==d[c][ip-1][1]+1:
                    d[c][ip-1][1] += 1
                    maxl = max(maxl, l1 +1)
                    f[l1]-=1
                    f[l1+1]+= 1
                elif ip<len(d[c]) and ind==d[c][ip][0]-1:
                    maxl = max(maxl, l2+1)
                    f[l2]-=1
                    f[l2+1]+=1
                    d[c][ip][0]-=1
                else:
                    bisect.insort(d[c],[ind, ind])
                    f[1]+=1
                r = s[ind]
                ip = bisect_right(d[r], [ind, n])

                l =  d[r][ip-1][1]-d[r][ip-1][0]+1
                f[l]-=1
                if d[r][ip-1]==[ind,ind]:
                    d[r].pop(ip-1)

                elif d[r][ip-1][0]==ind: 
                    d[r][ip-1][0]+= 1    

                    f[l-1]+=1
                elif d[r][ip-1][1]==ind: 

                    f[l-1]+=1
                    d[r][ip-1][1]-=1
                else:
                    l1, l2 = ind-d[r][ip-1][0], d[r][ip-1][1]-ind
                    rep = d[r][ip-1][1] 
                    d[r][ip-1][1] = ind-1
                    bisect.insort(d[r], [ind+1, rep])
                    f[l1]+=1
                    f[l2]+=1

                if l == maxl and f[maxl]==0 and maxl>1:
                    maxl -=1
                    while f[maxl]==0 and maxl>1: maxl -=1


            ans.append(maxl)
            s[ind]=c

        return ans
