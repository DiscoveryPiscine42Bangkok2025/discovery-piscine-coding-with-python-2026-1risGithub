def checkmate(board: str):
    try:
        grid = parse_board(board)
        size = len(grid)

        king_pos = find_king(grid)
        if not king_pos:
            print("Fail")
            return

        if is_king_in_check(grid, king_pos):
            print("Success")
        else:
            print("Fail")

    except Exception:
        print("Error")


def parse_board(board: str):
    rows = board.strip().split("\n")
    size = len(rows)

    for row in rows:
        if len(row) != size:
            raise ValueError("Board is not square")

    return [list(row) for row in rows]


def find_king(grid):
    king_positions = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "K":
                king_positions.append((i, j))

    if len(king_positions) != 1:
        raise ValueError("Invalid number of Kings")

    return king_positions[0]


def is_king_in_check(grid, king_pos):
    size = len(grid)
    kr, kc = king_pos

    for r in range(size):
        for c in range(size):
            piece = grid[r][c]

            if piece == "P":
                if check_pawn(r, c, kr, kc):
                    return True
            elif piece == "R":
                if check_rook(grid, r, c, kr, kc):
                    return True
            elif piece == "B":
                if check_bishop(grid, r, c, kr, kc):
                    return True
            elif piece == "Q":
                if check_rook(grid, r, c, kr, kc) or check_bishop(grid, r, c, kr, kc):
                    return True
    return False


def check_pawn(r, c, kr, kc):
    return (r - 1, c - 1) == (kr, kc) or (r - 1, c + 1) == (kr, kc)


def check_rook(grid, r, c, kr, kc):
    if r == kr:
        step = 1 if kc > c else -1
        for col in range(c + step, kc, step):
            if grid[r][col] != ".":
                return False
        return True

    if c == kc:
        step = 1 if kr > r else -1
        for row in range(r + step, kr, step):
            if grid[row][c] != ".":
                return False
        return True

    return False


def check_bishop(grid, r, c, kr, kc):
    if abs(r - kr) != abs(c - kc):
        return False

    step_r = 1 if kr > r else -1
    step_c = 1 if kc > c else -1

    row, col = r + step_r, c + step_c
    while (row, col) != (kr, kc):
        if grid[row][col] != ".":
            return False
        row += step_r
        col += step_c

    return True
