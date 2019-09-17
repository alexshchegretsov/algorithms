def initializer(number: int) -> tuple:
    height = number
    width = number * 2 - 1
    rows = [[' ' for _ in range(width)] for _ in range(height)]
    return height, width, rows


def solution(number: int):
    height, width, rows = initializer(number)
    for row_id in range(height):
        for cell_id in range(width):
            if cell_id == (number - 1 - row_id) or cell_id == (number - 1 + row_id):
                rows[row_id][cell_id] = str(number)
                # rows vertically decreasing number
                next_row = row_id + 1
                decreasing_num = number - 1
                while next_row < height:
                    rows[next_row][cell_id] = str(decreasing_num)
                    next_row += 1
                    decreasing_num -= 1
    # unite first half within revers first half
    rows.extend(rows[:-1][::-1])
    return rows


def print_matrix(matrix: list):
    for row in matrix:
        print(''.join(row))


if __name__ == '__main__':
    number = 9
    matrix = solution(number)
    print_matrix(matrix)
    