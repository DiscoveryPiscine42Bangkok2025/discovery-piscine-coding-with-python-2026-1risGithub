def find_king(grid, size):
    king_pos = None
    for r in range(size):
        for c in range(size):
            if grid[r][c] == 'K':
                if king_pos is not None:
                    return None
                king_pos = (r, c)
    return king_pos


def check_rook_and_queen(grid, size, kr, kc):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            if grid[r][c] != '.':
                if grid[r][c] in ('R', 'Q'):
                    return True
                break
            r += dr
            c += dc
    return False


def check_bishop_and_queen(grid, size, kr, kc):
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    for dr, dc in directions:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            if grid[r][c] != '.':
                if grid[r][c] in ('B', 'Q'):
                    return True
                break
            r += dr
            c += dc
    return False


def check_pawn(grid, size, kr, kc):
    # Pawn กินขึ้นบน → ดังนั้น Pawn ต้องอยู่ล่าง King
    for dr, dc in [(1, -1), (1, 1)]:
        r, c = kr + dr, kc + dc
        if 0 <= r < size and 0 <= c < size:
            if grid[r][c] == 'P':
                return True
    return False


def checkmate(board_str):
    try:
        rows = [r.strip() for r in board_str.strip().split('\n')]
        size = len(rows)

        if size == 0:
            print("Error")
            return

        if any(len(r) != size for r in rows):
            print("Error")
            return

        grid = [list(r) for r in rows]

        king = find_king(grid, size)
        if king is None:
            print("Error")
            return

        kr, kc = king

        if (check_rook_and_queen(grid, size, kr, kc) or
            check_bishop_and_queen(grid, size, kr, kc) or
            check_pawn(grid, size, kr, kc)):
            print("Success")
        else:
            print("Fail")

    except Exception:
        print("Error")
    