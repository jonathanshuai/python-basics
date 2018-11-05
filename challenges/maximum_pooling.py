
def maximum_pooling(elements, split):
  h_split = split[0]
  v_split = split[1]
  m1 = max([max(row[:v_split]) for row in elements[:h_split]])
  m2 = max([max(row[v_split:]) for row in elements[:h_split]])
  m3 = max([max(row[:v_split]) for row in elements[h_split:]])
  m4 = max([max(row[v_split:]) for row in elements[h_split:]])

  return [[m1, m2], [m3, m4]]

array = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [1, 2, 3, 4],
         [9, 2, 3, 3]]

test1 = maximum_pooling(array, (1, 1))
test2 = maximum_pooling(array, (2, 2))

def test_max_pooling(elements, h_splits, v_splits):
  n_h_splits = len(h_splits)
  n_v_splits = len(v_splits)

  

array = [[1, 2, 3, 4, 6],
         [5, 6, 7, 8, 3],
         [1, 2, 3, 4, 2],
         [9, 2, 3, 3, 7]]
test_t1 = test_max_pooling(array, [1,2,3], [1,2,3])
