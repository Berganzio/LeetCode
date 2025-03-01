# Formulas

## Triangle Inequality Theorem

$$
a + b > c
$$

$$
a + c > b
$$

$$
b + c > a
$$

$$
P = a + b + c
$$

## Slope Formula

$$
m = \frac{y_2 - y_1}{x_2 - x_1}
$$

## Collinearity Condition

$$
m_1 = \frac{y_2 - y_1}{x_2 - x_1}
$$

$$
m_2 = \frac{y_3 - y_2}{x_3 - x_2}
$$

$$
m_1 = m_2
$$

## Binary Addition

To add two binary numbers, follow these steps:

1. Represent the two binary numbers as $A$ and $B$.
2. Perform bit-wise addition from the least significant bit (rightmost) to the most significant bit (leftmost).
3. Use the following rules for binary addition:
   - $0 + 0 = 0$
   - $0 + 1 = 1$
   - $1 + 0 = 1$
   - $1 + 1 = 0$ (with a carry of 1 to the next higher bit)
4. Include the carry in the addition for each bit position.
5. If there is a carry left after the most significant bit, append it to the result.

For example, the sum of two binary numbers $A = 1011$ and $B = 1101$ can be calculated as follows:

$$
\begin{array}{c}
  \phantom{1}1 \\
  1011 \\
+ 1101 \\
\hline
11000 \\
\end{array}
$$

Below is a GitHub-ready markdown section that explains, step by step, how to solve the spiral order matrix problem.

---

## Spiral Order Matrix Traversal

This guide explains how to traverse a 2D matrix in spiral order and output a list of its elements.

## Problem Statement

Given a matrix (a list of lists of integers), return all elements in spiral order.

**Example:**

Input:
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Output:
```python
[1, 2, 3, 6, 9, 8, 7, 4, 5]
```

## Step-by-Step Instructions

1. **Check for an Empty Matrix:**  
   - If the matrix is empty or its first row is empty, return an empty list.

2. **Initialize the Boundaries:**  
   - **Top:** Start index for rows (`top = 0`).
   - **Bottom:** End index for rows (`bottom = len(matrix) - 1`).
   - **Left:** Start index for columns (`left = 0`).
   - **Right:** End index for columns (`right = len(matrix[0]) - 1`).

3. **Prepare the Result Container:**  
   - Create an empty list named `result` to store the spiral order elements.

4. **Traverse the Matrix in a Spiral Manner:**  
   - **While** `top <= bottom` **and** `left <= right`:
     - **Traverse the Top Row:**  
       Loop from `left` to `right` and append each element from the top row (`matrix[top][j]`) to `result`.  
       Then, increment `top` by 1.
     - **Traverse the Right Column:**  
       Loop from `top` to `bottom` and append each element from the right column (`matrix[i][right]`) to `result`.  
       Then, decrement `right` by 1.
     - **Traverse the Bottom Row (if applicable):**  
       If there are remaining rows (`top <= bottom`), loop backwards from `right` to `left` and append each element from the bottom row (`matrix[bottom][j]`) to `result`.  
       Then, decrement `bottom` by 1.
     - **Traverse the Left Column (if applicable):**  
       If there are remaining columns (`left <= right`), loop backwards from `bottom` to `top` and append each element from the left column (`matrix[i][left]`) to `result`.  
       Then, increment `left` by 1.

5. **Return the Result:**  
   - Once all boundaries cross (i.e., `top > bottom` or `left > right`), the loop stops, and `result` contains the matrix elements in spiral order.
