class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        bothof = zip(position, speed)
        times = []
        max_ti = 0
        fleets = 0
        for pos, sp in bothof:
            time = (target - pos)/sp
            times.append(time)
        cars = sorted(zip(position, times) , reverse = True)   
        for po , ti in cars:
            if ti > max_ti:
                fleets += 1
                max_ti = ti
        return fleets        

        