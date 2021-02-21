def find_all_increasing_subsequences(start, k, n, previous_sequence):
  if k == 0:
    print(' '.join(map(str, previous_sequence)))
    return 1
 
  if start > n:
    return 0    
 
  total_count = 0
 
  # Get all the subsequences that start with start
  previous_sequence.append(start)
  total_count += find_all_increasing_subsequences(start, k-1, n, previous_sequence)
  previous_sequence.pop()
 
  # Get all the subsequences that don't start with start
  total_count += find_all_increasing_subsequences(start+1, k, n, previous_sequence)    
 
  return total_count
 
n = int(input())
k = int(input())
 
total_count = find_all_increasing_subsequences(1, k, n, [])
 
print("Total: ", total_count)