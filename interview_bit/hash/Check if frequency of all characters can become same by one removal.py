def allSame(freq, N): 

    for i in range(0, N): 
        if(freq[i] > 0): 
            same = freq[i] 
            break
    for j in range(i + 1, N): 
        if(freq[j] > 0 and freq[j] != same): 
            return False
  
    return True

def possibleSameCharFreqByOneRemoval(str1): 
    l = len(str1) 
  
    freq = [0] * M 
    for i in range(0, l): 
        freq[getIdx(str1[i])] += 1
          
    if(allSame(freq, M)): 
        return True
      
    for i in range(0, 26): 

        if(freq[i] > 0): 
            freq[i] -= 1
  
            if(allSame(freq, M)): 
                return True
            freq[i] += 1
  
    return False