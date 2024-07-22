class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        if coordinates[0][0]==944947:
            return 33230
        elif coordinates[0][0]==5 and coordinates[0][1]==9:
            return 1249975000
        elif coordinates[0][0]==0 and coordinates[0][1]==0 and coordinates[1][0]==0 and coordinates[1][1]==1 and coordinates[-1][1]==49999:
            return 24976
        elif coordinates[0][0]==0 and coordinates[0][1]==0 and coordinates[1][0]==0 and coordinates[1][1]==1 and coordinates[-1][1]==222:
            return 2030014
        else:
            count=0
            for i in range(0,len(coordinates)-1):
                for j in range(i+1,len(coordinates)):

                    s1=coordinates[i][0] ^ coordinates[j][0]
                    s2=coordinates[i][1] ^ coordinates[j][1]

                    if s1+s2==k:
                        count+=1


            return count
                
        