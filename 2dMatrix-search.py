class solution:
    def searchMatrix(self, Matrix: list[list[int]], target: int):
        ROWS, COLS = len(Matrix), len(Matrix[0])
        top, bot = 0 , ROWS -1

        while top <= bot:
            middle = (top + bot)//2
            if target > Matrix[middle][-1]:
                top = middle + 1
            elif target < Matrix[middle][0]:
                bot = middle - 1
            else:
                break

            if top > bot:
                return False
            
        cnrow = (top + bot)//2
        l , r = 0, COLS-1
        while l<=r:
            mid = (l + r)//2
            if target > Matrix[cnrow][mid]:
                l = mid + 1
            elif target < Matrix[cnrow][mid]:
                r = mid -1
            else:
                return True
        return False
