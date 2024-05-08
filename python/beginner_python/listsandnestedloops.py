#lists inside lists
#Don't forget commas in seperating list

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

#4 rows
#3 columns 

print(number_grid[0][0])
#output is 1
#[0] = row the next [0] is a column

#nested for loops

for row in number_grid: #prints through the rows
    for col in row:#prints through indices of each row
        print(col)

