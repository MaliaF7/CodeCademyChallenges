def missing_nos(arr, k):
  # Write your code here
  return sorted(set(range(arr[0], arr[-1])) - set(arr))

print(missing_nos([1, 2, 4, 5, 6, 7, 8, 10], 2))

    
  
