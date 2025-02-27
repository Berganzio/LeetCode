class Solution:
    def judgeCircle(self, moves: str) -> bool:
        robot_position = [0, 0]
        for move in list(moves):
            if move == 'U':
                robot_position[1] += 1
            elif move == 'D':
                robot_position[1] -= 1
            elif move == 'L':
                robot_position[0] += 1
            elif move == 'R':
                robot_position[0] -= 1
        return robot_position == [0, 0]

        # fastest solution - not mine
        #return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')

# test
print(Solution().judgeCircle("LDRRLRUULR"))