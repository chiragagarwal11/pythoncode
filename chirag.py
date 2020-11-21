from collections import defaultdict
import sys
def SmallestSubString (S):
  distinct_count = len(set(list(S)))
  n = len(S)
  freq = defaultdict(int)
  start_idx = 0
  min_len = sys.maxsize
  distinct_till_here = 0 
  for j in range(n):
    freq[S[j]] += 1
    if freq[S[j]] == 1:
      distinct_till_here += 1
    
    if distinct_count == distinct_till_here:
      while freq[S[start_idx]] > 1:
        if freq[S[start_idx]] > 1:
          freq[S[start_idx]] -= 1
        start_idx += 1
      
      curr_len = j - start_idx + 1
      min_len = min(min_len, curr_len)
  return min_len
 
 
    
 
S = input()
 
out_ = SmallestSubString(S)
print (out_)