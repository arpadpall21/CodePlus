def dailyTemperatures(temperatures:list):
    nextWarmDay = [0 for _ in temperatures]
    
    for i in range(len(temperatures)):
        if i >= len(temperatures)-1:
            nextWarmDay[i] = 0
        
        if i < len(temperatures)-1:
            iRest = i+1
            nextWarmDayCount = 1
            while iRest < len(temperatures):
                if temperatures[iRest] > temperatures[i]:
                    nextWarmDay[i] = nextWarmDayCount
                    break
                
                nextWarmDayCount += 1
                iRest += 1

    return nextWarmDay





# print( dailyTemperatures([73,74,75,71,69,72,76,73]) )
# print( dailyTemperatures([30,40,50,60]) )
# print( dailyTemperatures([30,60,100,90]) )

temp = [34,34,47,47,34,34,34,47,34,47,47,47,34,34,34,47,47,34,47,47,34,34,34,34,47,34,34,47,34,34,34,47,47,47,47,47,47,34,34,34,47,34,34,47,34,47,47,47,34,47,47,34,47,34,47,47,34,47,47,34,34,47,47,47,34,34,47,47,47,34,34,47,34,34,34,47,47,34,34,47,47,47,47,47,34,34,34,47,47,34,47,34,47,34,34,47,34,47,47,47,47,47,47,34,34,34,47,34,47,34,47,34,34,34,34,47,34,34,34,34,34,34,34,47,34,34,47,47,34,47,47,47,47,47,47,47,34,34,47,34,47,34,47,34,34,34,47,34,34,47,34,47,47,34,47,47,47,47,34,34,34,34,47,47,34,34,34,47,34,34,47,34,34,47,34,34,34,34,47,34,34,34,47,34,34,47,47,34,47,47,34,34,34,34,34,34,47,47,34,47,34,47,34,47,47,47,34,47,34,34,34,34,34,47,47,47,47,47,47,34,47,34,47,34,34,34,47,47,47,34,47,47,34,47,47,47,34,47,47,34,47,47,34,47,34,34,47,47,34,34,34,34,47,34,34,47,47,34,47,47,34,34,34,34,47,47,34,34,47,47,34,47,34,47,34,47,47,47,47,34,34,47,47,34,34,34,47,34,47,47,47,34,47,47,34,34,34,34,34,47,47,34,47,47,34,34,47,34,47,47,34,47,47,47,47,47,47,47,34,34,34,34,47,47,34,47,34,47,47,34,47,47,34,34,34,47,47,47,34,47,34,47,47,47,34,34,34,34,34,34,34,47,34,34,34,34,47,47,34,34,47,34,47,47,34,47,34,34,47,47,47,47,47,47,34,34,47,34,34,47,34,47,47,47,47,47,34,34,34,47,47,34,47,34,34,47,47,47,34,34,47,47,47,34,34,47,47,34,34,47,47,47,47,34,34,34,47,34,34,47,47,34,34,34,47,34,34,47,34,34,34,34,47,34,47,34,47,47,47,34,34,47,47,47,47,47,34,47,34,34,34,34,34,47,47,34,34,47,47,34,34,47,34,47,34,47,34,47,47,47,47,47,47,47,47,47,34,47,47,47,34,47,47,34,34,47,34,47,34,34,47,47,47,47,34,47,34,34,34,47,47,47,34,34,47,47,34,34,34,34,47,47,34,47,34,34,47,47,34,47,34,47,34,47,34,34,47,34,47,34,47,34,47,47,47,47,47,34,34,47,47,34,34,34,47,34,34,34,34,34,47,47,47,34,47,47,47,47,47,47,47,47,34,34,34,34,47,34,47,34,47,47,47,34,34,34,34,47,34,47,34,47,34,47,34,34,34,47,34,47,34,34,47,34,34,47,34,34,47,47,47,34,47,47,47,34,34,34,34,34,34,34,47,34,34,47,34,47,34,47,34,34,34,34,47,47,47,47,34,47,34,34,34,47,34,47,47,47,34,34,47,34,47,47,34,47,34,34,34,47,34,34,34,47,34,34,34,34,34,34,47,47,47,47,34,47,47,34,47,34,47,34,47,34,47,34,34,47,34,47,34,47,34,34,34,34,34,47,47,47,47,47,47,47,47,47,34,47,47,34,34,34,47,34,34,47,47,34,47,47,47,47,47,47,47,34,47,34,47,47,47,47,47,47,34,47,47,34,34,34,47,47,47,47,34,34,47,47,34,34,34,34,34,47,34,34,34,34,47,47,34,47,47,47,47,47,47,47,34,34,47,34,47,34,47,47,47,47,34,47,47,47,34,34,34,34,34,34,47,47,47,34,34,34,47,47,34,47,34,47,47,47,34,47,47,47,47,47,47,47,34,47,47,47,34,34,47,47,34,47,47,34,34,34,47,34,47,34,34,47,34,47,34,34,34,34,47,47,47,34,47,34,47,47,34,47,34,47,34,47,34,47,47,47,34,34,47,34,47,34,47,47,47,47,47,34,47,34,47,34,47,34,34,47,47,47,47,47,34,47,34,47,47,47,47,47,47,47,34,47,47,47,34,34,34,47,34,47,47,47,47,34,47,47,34,47,34,34,47,47,34,34,47,34,47,47,47,47,34,47,47,34,34,34,47,47,34,34,47,34,47,34,47,34,47,47,47,47,34,47,47,34,34,34,47,34,47,34,47,34,34,34,47,34,34,34,34,34,34,47,47,47,34,47,47,47,34,34,34,34,47,34,34,47,34,34,47,47,34,34,47,34,34,47,34,34,47,34,47,47,34,47,47,34,34,47,47,34,34,47,34,34,47,47,34,47,34,34,47,47,47,34,34,47,47,34,34,34,47,47,34,47,34,47,47,34,34,34,47,47,47,47,34,47,47,34,47,47,34,47,34,47,34,47,47,34,34,47,47,47,34,47,47,47,34,34,34,47,47,47,47,34,47,47,34,34,34,34,34,34,34,34,47,34,47,47,34,47,47,34,47,47,47,47,47,34,47,34,34,34,34,47,47,47,47,34,34,34,47,34,34,34,47,47,34,47,47,34,47,34,34,34,47,34,47,47,47,34,34,34,34,47,47,47,34,47,47,47,34,47,34,47,34,34,47,47,47,47,34,47,34,47,34,47,34,34,34,47,34,34,34,47,34,34,47,34,47,34,47,47,34,34,47,34,47,47,47,34,47,34,47,34,47,47,47,47,34,34,34,34,34,34,34,47,47,47,47,34,47,34,34,47,34,47,34,34,34,47,47,34,34,34,47,34,47,47,47,34,34,47,47,47,47,34,34,34,47,47,34,47,34,34,34,34,34,47,47,47,47,47,34,34,34,34,47,47,34,47,47,47,34,34,47,34,34,34,34,34,34,34,47,47,34,47,34,47,47,34,47,47,47,34,34,47,47,34,34,34,47,47,47,34,34,34,34,47,34,47,34,34,47,47,47,47,34,47,34,47,47,47,47,34,34,47,47,47,34,47,34,47,34,34,47,34,47,47,47,34,34,34,34,47,47,47,34,34,47,47,47,34,34,47,34,47,34,47,34,47,34,34,47,47,47,34,47,34,47,47,47,34,34,34,34,34,47,34,47,47,47,47,34,47,47,47,47,34,34,47,47,47,34,34,34,34,34,47,34,47,47,34,47,47,47,34,47,34,47,47,34,47,34,47,34,34,47,34,34,47,34,34,34,34,34,47,34,47,34,47,47,34,47,47,34,34,47,34,34,47,34,34,47,47,34,47,34,34,47,47,47,47,47,34,47,47,47,47,34,34,34,47,47,34,34,34,47,34,34,47,47,34,34,47,34,34,34,47,47,47,34,34,34,47,47,47,34,47,47,34,47,34,34,47,47,47,34,47,34,47,34,34,47,34,34,47,47,34,34,47,47,34,34,47,47,47,34,34,47,34,34,47,47,47,34,34,47,34,34,34,47,47,47,34,34,47,47,34,34,47,47,34,34,47,47,47,47,47,34,47,47,47,34,47,47,34,34,47,34,47,34,34,34,47,47,47,47,47,47,34,34,47,47,47,34,34,34,34,34,34,34,34,47,34,34,34,34,34,47,34,34,34,47,47,34,34,34,47,34,47,47,34,47,34,34,34,47,47,34,47,34,47,34,34,47,34,47,34,34,47,47,34,34,34,47,34,34,34,34,47,34,47,47,34,34,34,47,47,34,34,34,47,47,47,34,34,47,34,47,34,47,34,34,34,47,34,47,34,34,34,47,47,34,34,47,34,47,34,34,34,34,47,47,47,47,47,34,47,47,34,47,34,34,34,34,34,34,34,47,47,34,34,47,47,47,34,34,34,47,34,34,34,34,34,47,34,47,47,34,47,47,34,34,34,34,47,34,34,47,47,34,34,34,34,47,47,47,47,34,47,34,47,47,34,34,47,34,47,47,34,34,34,34,34,34,34,47,34,34,34,47,34,34,34,34,34,47,47,47,47,34,47,47,34,34,47,34,47,47,34,34,34,47,47,34,47,47,47,47,47,34,47,34,34,47,47,34,34,34,47,47,34,34,47,34,34,34,47,34,34,47,47,34,47,34,34,47,47,47,47,34,34,34,34,34,34,34,47,47,47,34,34,47,47,47,34,47,34,47,34,34,47,47,47,47,34,47,34,47,47,34,34,34,34,47,47,47,47,34,34,47,34,34,47,34,34,47,34,47,34,34,47,34,34,34,47,34,34,34,47,47,47,34,47,34,34,47,47,47,34,34,47,34,47,47,34,47,47,47,47,47,34,34,34,47,34,34,34,34,47,34,34,47,34,34,34,34,47,47,34,47,47,34,47,34,34,47,34,47,47,47,34,47,34,34,34,47,47,47,47,34,47,47,34,34,47,47,34,47,47,34,47,34,34,47,34,34,34,34,34,34,47,47,47,34,47,34,34,34,47,47,34,47,34,47,34,47,34,34,47,34,34,34,47,34,34,47,34,34,47,47,47,34,47,47,34,34,47,47,34,34,34,34,34,34,47,47,34,34,47,34,34,47,34,47,47,34,47,47,34,47,34,34,34,47,34,34,47,34,34,34,34,47,47,34,47,34,34,34,47,47,47,34,34,34,47,34,47,34,34,34,34,47,34,34,34,34,34,47,34,34,34,47,47,34,34,34,47,34,34,47,34,34,34,34,47,34,47,34,34,47,34,34,47,47,47,47,47,34,47,34,47,47,47,47,47,47,47,47,47,34,34,34,34,47,47,47,34,47,47,34,47,47,47,47,34,47,34,34,34,47,34,34,47,47,34,47,47,34,34,34,47,34,34,47,47,47,47,47,34,47,34,34,34,47,47,47,47,47,47,34,47,47,47,47,34,47,34,34,34,34,34,34,47,47,34,34,34,34,47,34,47,47,47,34,34,47,47,47,34,47,34,47,47,34,47,47,34,47,47,34,34,47,47,47,47,34,47,47,47,34,47,47,34,34,34,34,34,34,47,34,47,47,47,47,34,34,34,34,47,47,34,47,34,47,47,34,47,34,34,34,47,34,34,47,47,47,47,47,34,34,34,47,34,47,47,34,34,47,34,34,34,47,34,47,34,47,34,47,47,47,34,34,34,34,34,34,47,47,47,47,34,34,47,47,34,34,47,47,47,34,34,34,47,34,34,34,34,34,47,34,34,34,34,34,34,47,34,47,34,34,47,47,47,47,34,34,34,34,47,47,34,47,34,47,34,34,47,34,47,47,47,34,34,34,34,47,34,47,34,47,47,47,34,34,47,47,47,47,34,34,34,47,34,47,47,34,47,34,47,34,47,47,47,47,34,34,47,47,47,47,47,47,47,34,47,34,34,47,47,47,34,47,34,34,47,34,47,47,34,47,47,34,34,34,34,34,47,34,34,34,34,47,34,47,34,34,47,47,47,47,47,34,34,34,47,34,34,47,47,47,47,34,34,34,47,34,34,47,34,47,34,34,47,47,47,34,34,34,47,34,47,47,47,47,34,47,34,47,34,47,34,47,34,34,47,34,47,34,47,47,47,34,34,47,47,34,34,34,47,47,34,34,34,34,34,34,47,34,34,34,47,34,34,34,47,47,34,34,47,47,34,47,47,34,47,34,47,47,47,47,34,34,47,34,34,47,34,34,47,47,34,47,34,34,34,34,34,34,34,47,34,34,47,47,34,47,34,34,34,47,34,34,34,47,47,47,47,47,47,47,47,47,47,34,47,47,47,34,47,34,34,47,34,47,34,47,47,47,34,34,47,34,34,34,47,34,47,34,34,34,47,34,34,47,34,34,34,34,47,47,34,47,34,47,34,47,47,47,34,34,47,34,34,34,47,47,34,34,34,47,47,47,47,34,34,47,47,47,47,34,34,47,47,47,34,34,47,34,47,34,34,34,47,34,34,34,47,34,47,47,34,47,34,34,34,34,47,34,47,34,47,47,47,47,47,34,34,34,47,47,34,34,34,47,47,34,34,34,47,47,47,47,47,34,34,47,47,34,34,47,34,47,47,47,47,47,34,34,47,47,34,34,47,34,34,47,34,34,47,47,47,47,34,34,47,34,34,34,34,34,47,34,47,47,47,47,47,47,34,34,47,34,34,34,47,47,34,47,34,34,34,34,47,34,47,47,34,34,34,34,34,34,47,47,47,47,34,34,47,34,47,34,47,47,34,34,34,34,34,47,34,47,34,34,47,34,47,47,47,34,34,34,34,47,34,47,34,47,47,34,34,47,34,34,34,34,34,47,47,34,47,47,34,47,47,34,34,47,47,47,47,34,47,47,34,34,34,34,34,34,47,34,47,34,47,34,47,34,47,34,47,34,34,47,47,47,47,34,47,34,47,34,34,34,34,47,47,34,34,47,34,34,47,47,34,34,47,47,34,34,34,34,47,47,47,34,47,47,34,47,34,47,47,47,34,47,47,34,47,34,34,34,34,34,34,34,34,47,47,34,34,34,34,47,34,47,47,47,47,47,34,47,47,47,34,47,47,47,47,47,34,47,34,34,47,47,34,47,34,34,34,47,47,34,34,47,47,47,47,34,47,34,47,47,34,34,34,47,47,47,47,34,34,34,47,47,34,34,34,47,34,47,47,47,34,47,34,34,47,34,47,47,34,34,34,34,47,47,47,34,34,34,34,47,47,34,47,47,47,34,34,34,47,47,34,47,34,47,34,47,34,47,47,47,34,34,34,34,34,47,34,47,47,47,47,34,47,34,34,47,34,34,34,47,34,47,34,34,47,47,47,47,34,34,47,34,47,34,34,34,34,34,34,34,47,47,47,34,47,47,34,47,47,34,34,34,34,47,34,47,47,34,34,47,34,47,34,34,34,47,34,47,34,34,34,47,34,34,47,34,47,34,47,34,47,47,34,34,34,34,47,47,34,34,34,34,34,34,34,47,47,34,34,47,47,47,47,34,34,47,34,34,47,34,47,34,34,47,47,47,34,34,47,34,34,34,47,47,47,34,34,47,34,34,34,47,34,34,34,47,34,34,47,34,34,47,34,47,34,34,34,34,47,34,34,34,34,47,34,47,47,47,34,34,34,34,34,47,47,47,47,34,34,47,47,34,47,47,34,34,34,47,34,47,34,47,47,34,34,34,47,47,47,34,47,34,47,34,47,47,47,34,34,47,34,34,47,34,34,47,34,47,34,47,34,34,47,34,34,34,47,34,34,34,47,34,34,47,34,47,34,47,34,34,34,34,47,34,34,47,47,47,47,47,47,34,47,47,34,47,34,34,34,47,34,34,47,47,47,34,34,34,47,34,47,47,47,47,47,47,47,34,34,47,34,47,34,34,47,34,34,47,47,34,34,47,47,47,34,34,34,47,47,34,47,47,34,34,34,47,34,47,47,47,47,47,47,47,47,34,47,34,34,47,47,34,34,34,34,47,34,47,47,34,47,34,47,47,47,34,34,47,34,47,47,47,47,34,34,47,34,34,47,47,34,47,47,47,47,34,47,47,47,47,47,47,47,34,34,47,47,47,34,47,47,34,34,47,47,34,47,34,47,47,47,34,47,47,47,47,47,34,47,47,47,47,34,47,34,34,47,34,47,34,34,34,34,34,34,34,34,34,47,47,34,47,34,47,47,47,34,34,47,34,47,34,47,47,47,47,47,34,34,34,34,34,34,47,47,47,34,34,34,47,47,34,34,47,47,34,47,34,34,47,34,34,34,47,47,34,34,34,47,47,34,47,34,47,47,34,47,34,34,34,34,47,47,47,34,47,47,47,47,47,47,47,47,47,34,47,34,47,34,47,47,34,34,34,34,34,47,47,47,34,34,47,34,47,34,47,34,34,47,34,47,47,47,34,47,34,47,34,34,34,34,47,34,47,47,34,34,34,34,47,34,47,47,47,34,47,47,34,34,47,34,34,34,47,47,47,34,47,47,34,34,34,47,34,47,34,47,47,47,34,34,47,34,34,47,34,34,34,47,34,47,47,47,47,47,47,34,34,34,47,47,47,34,47,47,47,34,47,34,34,34,34,47,47,47,47,34,34,34,34,34,47,47,34,47,34,34,47,34,34,47,34,47,47,34,47,34,34,47,34,34,34,47,47,34,47,34,34,47,47,47,34,47,34,47,47,34,34,47,47,47,47,47,47,47,34,34,47,34,34,47,47,47,47,47,47,47,34,47,47,47,34,34,47,34,47,47,34,34,34,34,47,47,34,34,34,34,34,34,34,34,34,34,47,34,47,47,34,34,34,47,47,47,34,34,34,34,47,34,47,47,34,47,47,47,34,34,34,34,34,47,34,47,47,34,34,34,47,34,34,47,47,47,47,47,34,34,47,47,34,47,34,34,47,34,47,34,47,34,47,47,34,34,34,34,34,47,34,34,34,47,47,47,34,34,47,47,47,47,34,34,34,34,47,47,47,34,34,34,47,47,34,47,34,47,34,47,47,47,47,34,34,47,47,34,34,47,34,47,47,34,47,34,47,47,47,47,34,34,47,47,34,34,47,34,47,34,34,34,47,47,47,47,34,34,47,47,47,34,47,34,34,47,47,34,34,34,47,34,34,47,47,34,47,47,34,34,47,34,47,34,47,34,47,34,47,47,34,47,47,34,47,34,34,34,34,47,47,47,34,47,47,47,47,47,34,47,34,34,47,34,47,34,34,34,34,47,47,47,47,34,47,34,34,34,34,34,47,47,34,34,47,47,34,34,34,34,47,34,34,47,47,34,47,34,47,34,34,47,47,47,47,34,47,34,34,34,34,34,34,34,34,47,47,34,47,34,47,47,47,34,47,34,47,47,34,34,34,47,34,47,34,34,34,34,47,47,34,34,34,47,34,34,34,34,34,47,34,47,47,47,47,34,34,47,47,34,34,47,47,34,47,47,47,34,34,47,34,47,34,47,34,34,47,47,47,47,34,34,34,47,34,47,34,34,47,47,47,34,47,47,47,47,47,47,34,47,47,47,47,47,34,47,34,47,34,34,34,34,47,34,47,34,34,47,34,34,34,34,47,47,47,47,47,47,47,47,34,47,34,34,47,34,47,34,47,47,47,34,47,34,47,34,34,47,47,47,47,47,47,34,34,34,47,47,47,47,34,34,47,34,34,34,34,47,34,34,34,34,34,47,47,47,47,47,47,47,47,47,47,34,47,47,34,47,47,47,34,34,34,47,47,47,47,47,34,47,47,47,47,34,34,34,47,34,34,47,47,34,47,34,34,47,47,47,34,47,47,47,34,34,34,34,34,47,47,47,47,34,47,34,47,47,34,34,34,34,34,47,34,47,34,47,34,34,47,47,47,47,47,34,34,47,47,47,34,47,34,34,47,47,47,47,34,34,34,34,34,34,47,47,34,34,34,34,34,34,47,47,34,47,47,34,34,47,34,47,34,47,34,47,47,34,34,47,47,34,47,34,47,34,47,34,34,34,34,34,34,47,47,34,34,34,47,47,34,34,34,34,47,34,34,34,47,47,34,47,34,34,34,47,47,47,34,47,34,34,47,34,34,47,47,47,47,47,34,34,34,34,47,34,47,34,47,34,34,47,34,47,34,47,34,34,47,47,47,47,34,47,47,47,47,47,47,47,34,47,47,34,47,47,47,34,47,47,47,34,34,47,47,34,47,34,47,47,34,47,47,47,47,34,47,47,47,34,34,47,47,47,34,34,34,34,47,34,47,34,47,34,47,47,34,47,47,34,34,34,47,34,34,34,47,34,34,34,47,34,47,47,34,34,34,47,34,47,47,34,34,47,34,34,47,47,34,34,34,34,47,34,47,34,47,47,34,47,34,34,47,47,47,34,47,47,34,34,47,47,47,34,34,47,34,47,47,47,47,47,34,47,47,34,47,47,47,47,47,47,47,34,34,47,47,47,47,34,34,47,47,47,47,34,47,47,34,34,34,47,34,34,34,34,34,47,34,47,34,34,47,34,47,47,34,34,34,47,34,47,34,47,34,47,34,47,34,47,47,47,34,47,47,34,34,34,34,47,34,34,47,47,34,47,34,34,47,47,34,47,47,34,34,47,34,34,34,47,34,47,47,47,34,47,34,47,47,34,47,34,47,34,47,47,47,34,47,47,47,47,47,34,34,47,47,34,34,34,47,47,47,34,47,34,47,34,47,47,47,34,47,34,47,34,47,34,34,47,47,34,34,47,47,47,34,34,34,47,34,47,34,34,34,47,34,34,47,34,47,47,34,34,34,34,47,47,47,47,47,47,34,47,34,34,47,47,47,34,47,47,47,34,34,34,34,34,47,47,47,47,34,34,47,47,47,47,47,34,34,47,34,47,47,47,34,34,34,34,47,47,34,47,34,47,34,34,34,47,34,47,47,47,34,34,34,47,47,34,34,34,34,47,47,47,47,47,34,34,47,47,34,34,34,34,47,47,47,34,34,34,34,34,34,34,34,47,34,47,34,34,34,47,47,34,34,47,34,47,47,34,34,47,47,47,34,47,34,47,34,34,34,47,47,47,47,47,34,34,34,47,47,47,34,34,34,47,34,34,47,34,34,47,47,34,34,34,34,34,47,47,47,34,47,47,47,34,34,47,34,47,34,34,34,47,34,47,47,34,47,47,47,47,47,47,47,47,47,47,34,34,47,47,47,47,34,47,47,34,47,34,34,47,47,34,47,47,34,47,34,34,34,34,47,47,34,47,34,47,34,47,47,34,47,34,47,34,47,34,47,47,34,47,47,47,47,47,47,34,47,47,34,34,34,34,47,34,47,47,47,34,34,47,34,47,34,34,47,34,34,34,34,34,34,34,47,47,47,47,47,34,34,47,47,47,47,34,34,47,34,34,34,47,47,34,47,47,34,34,47,47,34,47,34,47,34,47,47,47,47,34,34,34,47,34,47,34,34,47,47,34,47,34,34,34,34,47,47,47,34,47,47,47,47,47,47,47,34,34,34,34,34,34,34,34,47,34,34,47,34,47,34,47,34,34,47,47,47,34,47,47,34,47,47,34,47,34,34,47,34,47,34,34,47,34,34,34,34,34,47,47,47,47,47,47,47,34,34,47,47,47,34,47,47,34,47,34,34,34,47,34,34,47,34,47,47,34,47,47,47,47,47,34,34,47,34,34,34,34,47,47,47,47,34,34,34,34,34,34,47,34,34,34,47,34,47,47,34,34,34,47,34,34,34,47,34,47,34,47,34,47,47,34,47,47,34,47,47,47,47,34,34,47,47,47,34,34,47,34,34,34,47,34,34,34,47,47,34,47,47,34,34,34,34,47,47,47,47,47,47,34,34,34,47,34,34,34,34,34,47,34,34,47,34,34,34,47,47,34,47,47,47,47,34,34,47,34,34,47,47,34,47,34,34,47,34,47,34,47,34,47,34,34,34,34,34,34,47,34,34,47,47,34,34,34,47,34,34,34,34,47,34,34,47,47,47,47,34,34,34,47,34,47,34,34,47,47,34,47,47,34,47,47,34,34,34,34,47,47,47,34,34,47,47,47,34,34,47,47,34,47,34,34,34,47,47,47,34,34,34,34,34,34,47,34,47,34,34,34,34,47,47,47,34,47,47,34,47,34,47,47,34,34,47,47,47,34,47,47,34,34,34,34,34,47,34,47,34,47,47,34,34,47,47,34,47,47,34,47,47,34,47,47,47,34,47,34,47,34,34,47,47,47,34,47,34,47,47,47,47,47,47,47,34,34,34,47,47,47,34,47,47,34,47,34,47,47,47,34,47,47,34,47,47,47,47,47,34,34,47,47,34,47,47,34,47,34,34,47,34,34,34,34,34,47,34,34,47,34,34,47,34,47,47,47,34,34,34,47,34,47,34,34,47,47,34,34,34,34,34,34,34,34,47,34,47,47,34,47,34,47,34,34,34,47,34,47,34,47,47,34,47,47,47,47,47,34,34,34,47,34,34,34,47,34,47,47,34,34,34,34,34,34,34,47,47,47,34,34,47,34,34,47,47,47,47,34,47,34,47,34,47,34,47,47,47,47,47,47,47,47,47,47,47,34,47,34,34,34,47,34,34,47,47,47,34,34,47,34,34,34,34,34,47,34,47,47,34,34,34,47,47,47,47,47,47,34,47,34,34,47,47,34,47,47,34,47,34,34,34,34,34,47,34,34,47,34,34,34,34,47,34,34,34,34,47,34,47,34,34,47,47,47,47,47,34,47,34,47,34,34,34,47,34,47,47,47,34,47,34,34,47,34,34,47,47,47,34,34,34,47,34,47,47,47,34,47,47,34,34,34,34,34,34,34,34,34,47,34,47,34,34,34,34,47,47,34,47,34,34,34,47,47,47,47,47,34,34,34,47,34,47,47,47,47,34,47,34,34,34,34,47,47,34,47,34,47,47,47,34,34,34,34,34,47,47,47,47,34,34,34,47,47,47,34,47,47,47,34,47,34,34,47,47,47,34,47,34,34,34,47,34,34,47,47,47,34,34,47,34,34,34,47,47,34,34,34,47,34,47,34,34,47,34,34,34,47,47,47,34,34,34,47,47,34,47,47,34,47,34,47,47,47,34,47,47,34,34,34,47,34,34,34,34,34,34,47,47,34,34,47,34,34,34,34,34,47,34,47,34,47,34,34,47,34,47,47,34,47,34,34,47,34,34,47,47,47,34,47,34,47,47,47,47,34,34,47,47,34,34,34,34,34,47,34,47,34,34,34,47,47,34,34,47,47,34,47,34,47,34,34,47,34,34,47,34,47,34,47,34,47,47,47,34,34,34,34,34,34,47,47,34,34,34,34,34,34,34,34,34,47,34,47,47,34,47,34,47,34,34,47,47,47,34,34,47,34,47,47,34,47,34,34,34,47,34,34,34,47,47,34,34,47,34,34,34,47,34,47,34,34,34,47,47,34,34,47,34,34,34,47,47,34,34,47,34,34,47,34,47,34,47,47,34,47,47,34,34,34,47,34,47,47,47,47,47,47,34,47,34,47,34,34,34,47,47,34,34,47,34,34,47,34,34,47,34,34,34,34,47,34,34,34,34,34,47,47,47,34,47,47,47,34,34,34,34,47,34,34,47,47,34,34,34,47,34,47,47,34,47,47,34,47,34,34,34,47,34,47,47,34,47,34,34,47,47,34,34,47,34,47,47,47,47,34,47,47,34,34,47,47,47,47,47,47,47,47,47,47,47,34,47,34,47,47,47,47,47,34,47,47,34,34,34,34,34,47,34,47,47,34,34,47,34,47,34,34,47,47,34,47,47,47,47,34,47,34,47,34,34,47,47,34,34,34,34,47,47,47,47,34,34,34,47,34,34,47,47,34,47,34,47,34,47,47,34,47,47,47,34,47,34,47,34,34,47,47,47,34,47,47,47,47,47,34,47,47,47,34,34,47,47,47,47,34,34,47,34,34,47,47,34,34,47,34,47,47,34,34,47,34,47,47,47,34,34,47,47,47,34,34,47,34,34,34,47,47,47,47,47,47,34,34,47,34,34,34,34,47,34,34,47,34,47,47,34,47,34,47,47,34,47,47,34,34,47,34,47,34,47,34,47,47,34,47,47,34,47,34,47,34,47,34,34,34,47,47,47,34,34,47,34,34,47,47,47,47,47,47,47,34,34,47,34,34,34,47,34,34,34,47,34,47,34,34,34,47,34,47,47,47,47,34,47,47,34,47,47,47,34,47,34,34,34,47,34,34,34,34,34,47,34,47,47,34,47,47,47,47,34,47,47,47,47,34,47,47,47,47,34,47,47,47,47,47,34,34,34,47,34,34,47,34,47,47,34,47,47,34,34,47,34,34,47,34,47,47,34,34,34,47,47,47,47,34,34,34,47,34,47,47,34,34,47,34,34,47,34,47,47,34,47,47,34,34,34,47,47,47,34,34,47,34,47,47,34,34,47,47,34,47,47,47,47,47,47,47,34,47,47,47,34,34,34,34,47,47,34,47,34,34,47,34,34,34,47,34,34,34,47,34,34,34,47,34,34,34,47,47,34,47,47,34,47,34,47,47,34,34,34,47,34,47,34,47,47,47,34,47,47,47,47,47,34,47,34,47,47,34,34,34,47,34,34,47,47,34,34,34,34,47,47,47,47,47,34,34,47,47,34,47,34,34,34,47,34,34,34,47,34,34,34,34,34,47,47,47,34,47,34,34,34,47,34,34,47,34,47,34,47,34,47,47,34,34,47,34,47,34,34,47,47,34,47,47,34,34,47,47,34,34,34,47,34,34,47,34,47,34,34,47,47,34,34,47,47,47,34,47,47,47,47,47,34,47,34,34,47,34,34,47,47,34,47,34,34,47,34,34,47,47,34,47,34,47,34,47,47,47,47,34,34,47,47,34,47,34,47,34,34,47,34,47,47,47,47,34,34,47,47,47,47,34,47,47,47,47,34,34,47,34,47,47,47,34,34,34,34,34,34,47,47,47,34,34,47,47,47,34,34,34,34,47,34,47,34,47,34,34,34,34,47,47,47,34,47,34,47,34,34,47,47,34,34,47,47,47,34,34,34,34,47,47,47,34,34,47,47,47,47,47,47,34,34,47,47,47,47,34,34,47,34,34,34,34,34,34,47,47,47,47,34,47,34,47,34,34,47,47,47,34,34,47,47,47,34,47,34,47,34,34,47,34,34,34,34,34,34,34,34,34,34,34,47,47,47,34,34,34,47,47,34,34,34,47,47,47,34,47,34,34,34,34,34,34,34,47,34,34,47,47,47,47,34,47,34,34,47,34,34,47,34,34,47,47,47,47,47,47,47,34,34,34,34,47,34,34,34,34,47,34,47,47,34,47,34,34,47,34,47,34,47,47,47,34,34,47,47,47,47,47,47,34,47,34,34,47,34,34,47,47,47,47,47,47,34,47,34,34,34,34,47,47,34,34,47,34,34,47,47,47,34,34,47,34,34,34,34,34,47,34,47,34,47,34,34,34,47,34,34,34,34,47,47,47,47,47,34,34,47,34,34,47,34,34,34,34,47,34,34,47,47,47,47,47,34,34,47,47,34,47,34,34,34,34,47,34,34,47,47,47,47,47,34,34,34,47,34,34,34,34,34,47,47,47,34,47,34,47,34,47,47,47,34,47,47,47,47,47,34,34,34,47,34,47,34,47,47,47,34,47,34,34,47,34,34,34,47,47,47,47,34,34,47,34,47,34,47,34,34,34,34,34,34,47,47,34,34,47,34,34,47,34,34,47,34,34,47,47,47,34,34,34,47,47,47,47,34,47,47,47,34,47,34,47,47,47,34,47,34,34,47,34,47,47,47,47,34,47,47,34,47,34,47,47,47,34,47,47,47,47,47,34,47,47,34,34,47,34,47,34,34,34,47,47,34,47,34,47,34,34,34,47,47,47,34,47,34,34,47,34,34,34,47,47,47,47,47,47,47,34,47,34,34,47,34,34,47,47,34,47,34,34,34,34,47,34,47,34,47,47,47,47,47,34,47,47,47,34,34,47,47,34,34,47,47,47,34,47,47,34,34,34,47,47,47,34,34,34,47,34,47,47,34,47,47,47,34,47,47,34,47,47,34,47,47,34,34,34,47,47,47,34,47,34,34,47,34,47,34,47,47,34,47,47,47,47,47,34,47,34,47,47,34,34,34,47,47,34,34,47,47,47,47,47,34,34,34,47,47,34,47,47,47,34,34,34,34,47,47,34,34,47,47,47,47,47,34,34,34,47,47,34,47,47,47,34,34,47,34,34,47,34,47,34,47,34,34,47,34,47,47,34,34,47,34,34,34,34,47,34,34,47,47,47,47,47,47,47,34,34,34,34,34,34,34,34,47,47,34,34,47,47,47,47,34,47,47,47,34,34,47,47,34,34,34,34,47,34,34,47,47,34,34,47,47,34,34,34,34,34,34,47,47,34,47,47,34,34,47,34,34,34,34,47,34,34,34,34,34,34,47,47,47,47,34,47,34,34,34,34,47,47,34,34,47,47,47,47,47,34,34,47,47,47,47,47,47,47,47,47,34,34,47,34,47,47,34,47,47,47,34,34,47,47,34,34,47,47,47,34,34,47,34,34,34,34,34,34,47,47,47,47,34,47,47,34,34,47,34,47,34,34,34,47,34,34,47,34,34,34,34,34,47,34,34,47,47,34,34,34,47,47,34,47,47,47,47,47,34,47,34,47,34,34,34,34,47,34,47,34,34,47,47,34,34,47,34,34,34,34,47,47,34,47,34,34,34,34,47,47,47,47,47,47,34,34,47,47,34,34,34,34,34,34,47,34,47,47,34,47,34,47,34,34,34,47,34,34,34,34,34,34,47,47,34,34,47,34,34,47,47,34,34,47,34,34,47,47,34,34,34,34,34,47,34,47,47,47,47,47,34,47,47,34,47,47,34,47,47,34,34,47,34,47,47,47,47,34,47,34,47,34,47,34,47,47,34,47,47,47,47,47,34,34,34,47,47,34,47,47,47,47,34,34,47,47,34,47,34,47,34,34,34,47,34,47,47,34,47,47,34,34,34,47,47,34,34,34,47,47,34,47,47,34,34,34,34,34,47,34,47,34,47,47,34,34,47,34,47,34,34,34,34,47,47,34,47,34,47,34,34,47,34,47,34,34,34,47,47,47,47,34,34,47,47,47,47,34,34,47,47,34,34,47,34,34,47,34,47,47,34,47,34,34,47,47,47,34,47,47,47,47,34,47,34,34,34,34,34,34,34,34,47,34,34,34,34,47,47,47,47,34,47,34,34,34,47,34,34,34,47,34,47,34,34,34,34,47,34,34,34,47,34,47,47,47,34,34,47,47,47,47,47,34,47,47,47,47,34,34,47,34,34,47,34,47,34,47,34,34,47,47,47,34,47,47,34,34,34,47,34,34,47,47,47,34,47,34,34,47,47,47,47,34,34,47,34,47,34,47,34,47,34,34,47,47,47,34,34,34,34,47,34,47,47,47,47,47,34,47,47,47,34,34,47,47,34,47,34,34,34,34,47,34,34,47,34,47,34,47,47,34,34,47,47,34,34,47,34,47,47,34,47,47,34,34,34,34,47,34,47,47,47,34,47,34,34,34,34,34,47,47,34,47,47,47,34,34,47,34,47,34,34,47,34,34,47,47,47,34,47,34,34,34,47,34,34,34,47,47,47,34,34,34,47,47,47,34,34,34,34,34,34,47,34,47,34,34,47,34,34,47,34,47,47,34,47,47,34,47,34,34,47,34,34,34,47,34,47,47,47,34,47,34,47,47,34,47,34,34,47,47,34,34,47,47,47,34,47,47,47,34,34,47,47,34,34,47,34,47,34,34,34,34,47,47,34,47,47,47,47,34,34,47,34,34,34,47,47,34,34,34,47,34,47,34,34,34,47,47,47,47,34,34,47,47,34,47,47,47,47,34,34,47,47,47,34,47,47,47,47,47,47,34,34,47,47,34,34,34,34,47,47,47,34,34,47,47,47,47,47,34,47,34,47,47,34,34,34,47,34,34,34,34,47,47,34,47,47,34,34,47,34,34,47,34,34,34,47,47,34,34,47,34,34,47,47,47,34,34,47,34,47,34,34,34,47,34,47,47,34,34,34,34,34,47,34,47,47,47,47,47,34,34,34,34,47,34,47,34,47,47,34,34,34,47,47,47,47,47,47,34,47,47,47,47,47,34,47,34,34,34,34,47,34,34,34,34,47,47,34,47,34,47,34,47,47,34,34,34,47,34,47,47,47,34,47,34,47,47,34,47,34,47,47,34,47,47,47,47,34,47,34,47,47,47,34,34,47,47,34,47,34,34,34,34,47,34,47,34,47,34,34,34,34,34,47,34,47,47,34,34,34,47,34,34,34,47,47,47,47,34,34,47,34,34,47,47,47,34,47,34,34,47,47,47,34,34,34,34,34,34,47,34,34,34,47,47,47,34,34,34,34,47,47,47,34,34,47,47,47,47,47,34,47,34,34,34,47,34,34,47,47,34,34,47,34,34,47,47,47,34,47,34,47,34,47,47,47,34,47,47,47,34,47,34,47,47,34,47,34,34,47,34,47,34,34,47,47,47,34,47,34,34,47,47,47,47,47,34,47,47,47,34,34,34,34,47,34,47,34,34,34,34,34,34,34,47,47,47,47,34,47,47,47,47,47,34,34,34,47,47,47,47,47,34,34,47,47,34,34,47,47,34,34,47,34,34,34,34,34,47,47,34,34,47,34,34,34,47,47,47,47,47,34,34,34,47,34,34,47,34,47,47,47,47,47,47,34,34,47,47,47,34,34,47,47,47,34,47,34,34,34,47,47,47,47,47,47,47,34,47,34,34,34,34,47,47,34,47,47,34,47,47,34,34,47,47,34,47,47,47,34,34,34,34,34,34,34,34,34,34,47,34,47,34,47,34,34,34,34,47,34,34,34,34,34,34,47,34,47,34,34,34,47,47,34,47,47,34,34,47,34,47,34,47,34,34,47,47,47,34,47,34,47,34,47,47,34,47,34,47,47,34,34,34,34,47,34,47,34,34,34,34,34,34,34,47,47,34,47,34,47,47,34,47,34,34,34,47,47,34,34,47,34,47,47,34,47,34,47,47,34,34,47,47,34,34,34,47,34,34,34,47,47,34,34,47,47,34,47,34,47,34,47,47,34,34,47,34,47,34,47,47,34,47,47,34,47,47,34,34,47,34,34,34,34,47,47,47,34,34,34,47,34,47,47,34,34,34,34,47,34,34,47,47,47,47,47,34,34,34,47,34,47,34,47,34,34,34,34,47,47,47,47,47,34,47,47,34,34,34,47,34,47,34,47,34,47,34,47,34,34,34,47,47,47,34,34,34,47,34,34,34,47,47,47,34,47,34,47,34,34,47,34,47,34,34,34,34,34,47,47,47,47,34,34,34,34,47,34,47,47,34,47,34,34,47,47,47,34,34,47,47,34,47,34,34,34,34,34,34,34,47,47,34,34,47,34,34,34,47,47,47,34,34,34,47,47,34,34,47,34,47,47,34,47,47,47,47,34,34,47,47,47,47,34,34,47,34,47,47,47,47,34,34,34,47,47,34,34,47,34,47,34,47,34,47,47,47,34,47,47,34,47,34,34,34,34,47,34,34,47,34,34,47,47,34,47,34,34,47,47,47,47,34,47,47,34,34,34,34,47,34,34,34,34,47,47,34,34,47,47,34,34,34,47,47,34,34,47,34,47,47,47,47,47,34,34,47,34,47,34,47,47,47,47,47,47,47,34,47,34,47,47,47,47,47,47,47,47,34,34,34,47,47,34,47,34,47,34,34,47,47,47,47,47,34,47,34,47,34,34,47,47,47,47,34,34,34,34,47,34,34,34,34,47,34,47,34,34,47,34,34,47,47,34,34,47,47,47,47,47,34,34,47,34,34,34,34,47,47,34,47,47,47,47,47,47,34,47,47,47,47,47,47,47,47,47,47,34,47,47,34,34,47,47,47,34,47,34,34,34,34,34,34,47,47,47,34,34,34,47,34,34,34,34,47,47,34,34,47,47,47,47,34,47,34,47,47,47,47,47,34,34,34,47,34,34,47,47,34,47,34,34,47,34,47,47,47,34,34,47,34,34,47,34,34,47,47,47,47,47,47,47,47,47,34,47,34,34,34,47,47,34,34,47,34,47,34,34,34,47,47,47,34,47,47,34,34,47,47,34,34,34,47,47,47,47,34,47,47,47,34,34,47,47,34,34,47,47,47,47,47,47,34,34,34,47,34,34,34,47,34,47,47,34,34,47,47,34,47,34,47,47,47,34,34,47,47,34,34,34,34,47,47,47,47,34,34,34,34,34,47,34,34,47,34,47,34,34,34,47,47,47,34,47,34,34,34,47,34,34,47,47,47,47,47,47,34,47,47,34,47,47,34,47,47,34,47,47,47,34,34,47,47,34,34,34,34,34,34,47,34,34,47,34,34,34,34,47,47,47,34,34,47,34,34,34,34,47,34,34,34,47,34,47,47,34,47,34,34,34,47,34,34,34,47,34,47,34,34,47,34,47,47,34,47,47,34,34,34,34,34,34,47,47,47,47,47,34,47,34,34,47,47,34,47,47,34,47,47,47,34,34,47,47,47,34,34,47,34,47,47,47,34,34,34,47,47,47,47,47,47,34,47,47,47,47,47,34,34,34,47,34,34,47,47,47,47,34,47,34,34,34,47,47,34,34,47,47,47,47,47,47,34,47,34,47,47,34,34,47,34,34,34,47,34,47,47,47,34,47,47,34,47,34,34,47,34,34,47,47,47,47,47,34,34,34,47,34,34,34,47,34,47,47,47,47,47,34,47,34,47,47,47,47,34,47,34,47,47,47,47,47,47,47,34,34,34,34,34,47,34,34,47,34,47,34,34,47,47,47,47,47,47,47,34,47,47,47,47,34,34,47,47,34,34,34,47,47,34,34,34,47,34,47,34,34,34,34,47,34,47,47,34,47,47,47,47,47,47,47,47,47,34,47,47,34,47,47,47,47,47,34,47,34,34,34,47,34,34,47,47,47,34,47,34,34,34,47,47,34,34,34,47,47,34,34,47,34,34,47,34,34,34,47,34,34,34,34,34,47,47,47,34,47,47,34,47,47,34,34,47,34,34,34,47,34,34,47,34,34,47,34,34,34,34,34,34,34,34,47,47,47,47,34,34,34,34,47,34,47,47,47,47,47,34,34,34,34,47,47,47,34,47,34,34,47,47,47,47,34,47,34,47,47,47,34,34,34,47,34,47,47,34,34,34,34,34,47,47,34,34,47,47,47,47,34,47,47,34,47,47,34,47,34,34,34,47,34,34,47,34,34,47,34,47,47,34,47,34,47,34,34,34,34,47,34,47,34,34,34,47,47,47,47,47,47,47,34,34,47,34,34,34,47,47,47,34,47,34,34,47,34,47,47,47,47,34,47,47,47,34,34,47,47,47,34,34,47,34,47,34,34,47,34,34,47,34,34,34,47,47,47,34,34,34,47,34,47,34,47,34,34,47,34,34,47,34,47,47,47,34,34,34,47,47,34,47,34,47,34,47,34,34,34,47,47,47,47,34,47,47,34,47,34,34,34,34,34,34,34,34,47,47,34,34,34,34,34,47,34,34,47,47,34,47,34,34,47,47,34,47,34,34,34,34,34,34,47,47,34,34,34,47,47,47,47,47,47,47,34,34,34,47,34,34,47,47,47,47,34,47,47,34,34,47,47,34,47,47,34,34,47,47,47,47,47,34,34,34,34,47,34,47,34,34,47,34,47,47,47,34,34,47,47,47,47,34,47,34,34,47,34,34,47,34,47,47,34,47,34,47,47,47,47,47,47,47,34,34,34,34,34,34,34,34,34,47,34,47,47,47,47,47,47,47,47,34,47,47,47,47,47,47,34,47,47,47,47,34,34,34,47,47,34,47,47,47,47,47,47,34,47,34,34,34,34,34,34,34,47,34,34,47,34,47,47,34,47,34,34,34,47,34,34,34,34,34,47,47,34,34,34,47,47,47,47,47,34,47,47,34,47,34,47,47,47,34,47,34,34,47,47,47,34,47,47,47,47,47,34,47,34,34,47,34,34,47,34,34,47,34,34,47,47,34,34,47,47,47,34,47,47,47,34,47,34,34,47,47,34,34,34,47,34,34,34,34,47,34,34,47,34,34,47,34,47,47,34,47,47,34,34,47,34,34,34,47,34,47,34,34,34,34,34,47,34,34,47,34,34,34,47,34,47,34,47,47,34,34,34,34,34,47,34,47,34,34,47,47,47,34,47,34,34,47,47,47,34,34,34,34,34,34,47,47,34,47,47,47,34,34,34,34,34,34,47,47,47,47,34,34,47,47,47,47,34,34,34,34,34,47,34,47,34,34,47,47,47,47,47,34,34,34,34,47,34,34,34,34,34,34,47,34,47,34,34,47,47,34,34,47,34,47,34,34,34,47,47,34,34,47,47,47,47,34,34,34,47,34,47,47,34,47,34,34,47,34,47,47,34,47,34,34,47,47,47,47,34,47,47,47,34,47,34,34,47,34,34,47,34,47,47,47,34,34,47,34,47,34,34,34,34,47,47,34,34,34,47,34,47,34,47,34,34,34,47,34,34,47,34,34,34,47,34,34,34,47,34,47,47,47,34,47,34,34,47,47,34,47,47,47,47,47,47,47,47,34,34,47,34,34,34,34,34,47,47,47,34,34,34,47,47,34,47,34,34,34,47,47,47,47,34,34,34,34,47,47,47,34,47,34,34,47,47,47,34,47,47,34,34,47,47,34,47,47,47,34,47,47,47,34,47,34,47,47,34,34,34,47,34,47,47,47,34,47,47,47,47,34,34,34,47,34,34,47,47,34,34,34,34,34,47,34,34,47,47,34,34,47,34,34,34,34,47,47,47,47,47,47,34,34,34,34,47,34,34,34,47,47,34,34,47,47,47,47,47,47,47,34,47,47,47,47,34,34,34,34,34,34,34,34,47,34,34,34,47,47,34,34,47,34,34,34,34,47,47,47,47,47,47,34,34,47,47,34,47,47,34,47,47,34,47,34,47,34,47,47,34,47,34,34,47,34,47,34,34,34,47,47,34,34,34,47,34,47,34,34,34,47,34,47,34,47,34,47,47,34,34,47,47,47,34,47,47,47,34,34,47,34,47,47,47,47,34,47,34,47,34,34,47,34,34,47,47,47,47,47,34,47,47,47,47,47,34,47,34,47,34,34,34,47,47,47,34,47,34,34,34,47,47,47,34,47,47,34,34,34,34,34,47,47,47,47,47,47,34,47,34,47,34,34,34,34,47,47,47,47,47,34,34,47,34,47,34,34,34,34]

print( dailyTemperatures(temp) )
