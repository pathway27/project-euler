

TRIANGLE = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

TRIANGLE_TEST = """
3
7 4
2 4 6
8 5 9 3
"""
# doesn't work
def greedy():
    rows = []
    for i in TRIANGLE.split('\n'):
        rows.append(i.split(' '))

    total = 0
    index = 0
    for row in rows[1:-1]:
      if len(row) == 1:
        total += int(row[0])
      else:
        subset = map(int, row[index:index+2])
        print subset,
        if subset[0] > subset[1]:
          total += subset[0]
          print subset[0]
        else:
          total += subset[1]
          index += 1
          print subset[1]

    print total

def recSumAtRow(rowData, rowNum):
    # iterate over the given row
    for i in range(len(rowData[rowNum])):
        # add the largest of the values below-left or below-right
        rowData[rowNum][i] += max([rowData[rowNum+1][i],rowData[rowNum+1][i+1]])
        for i in rowData:
            print(i)
    # base case
    if len(rowData[rowNum])==1: return rowData[rowNum][0]
    # recursive case
    else: return recSumAtRow(rowData, rowNum-1)


def first():
  rows = []
  for i in TRIANGLE.split('\n')[1:-1]:
      rows.append([int(j) for j in i.split(' ')])
  
  # print(rows)
  result = recSumAtRow(rows, len(rows)-2) # start at second to last row

  print result
if __name__ == '__main__':
    first()
