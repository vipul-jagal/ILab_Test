def merge_sorted_arrays(arr1, arr2):
  """
  Merges two sorted arrays such that the initial numbers (after complete sorting)
  are in the first array and the remaining numbers are in the second array.

  Args:
    arr1: The first sorted array.
    arr2: The second sorted array.

  Returns:
    A tuple of the merged arrays.
  """

  i, j = 0, 0
  merged_arr = []

  while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
      merged_arr.append(arr1[i])
      i += 1
    else:
      merged_arr.append(arr2[j])
      j += 1

  merged_arr += arr1[i:]
  merged_arr += arr2[j:]

  return merged_arr


def main():
  arr1 = [1, 5, 9, 10, 15, 20]
  arr2 = [2, 3, 8, 13]

  merged_arr = merge_sorted_arrays(arr1, arr2)

  print("The merged arrays are:")
  print(merged_arr)


if __name__ == "__main__":
  main()
