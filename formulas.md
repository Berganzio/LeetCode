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
