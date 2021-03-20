# N---Queens-

### AIM
To solve n-queens problem using hill-climbing search and its variants.

### PROBLEM STATEMENT
Implement Hill-climbing search, Hill-climbing search with sideway moves and Random-restart 
hill-climbing with and without sideways move and apply it to n-queens problem. List average 
number of steps when the algorithm succeeds and fails along with the success and failure rate 
for multiple iterations.

### N-QUEENS PROBLEM
The N-queens puzzle is the problem of placing N queens on a N x N chessboard such that no two 
queens attack each other. The queen is the most powerful piece in chess and can attack from any 
distance horizontally, vertically, or diagonally. Thus, a solution requires that no two queens share 
the same row, column, or diagonal.

### PROBLEM FORMULATION
Initial State: A random arrangement on n queens, with one in each column.
Goal State: N queens placed on the board such that no two queens can attack each other.
States: Any arrangement of n queens, one in each column.
Actions: Move any attacked queen to another square in the same column.
Performance: Number of steps and success rate to find a solution.
