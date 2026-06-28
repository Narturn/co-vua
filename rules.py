# Tính đường đi quân xe
def rook_moves(row, col, matrix):
    looks = []
    # Các hướng di chuyển của quân xe
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # down, up, right, left

    for delta_row, delta_col in directions:
        # tính toán vị trí tiếp theo dựa trên hướng di chuyển 
        next_row = current_row = row + delta_row
        next_col = current_col = col + delta_col

        # Tiếp tục di chuyển trong hướng hiện tại cho đến khi gặp biên hoặc quân cờ khác
        while 0 <= next_row < 8 and 0 <= next_col < 8:
            looks.append((next_row, next_col))
            # Tiến thêm 1 bước về hướng hiện tại
            next_row += delta_row
            next_col += delta_colrow

return looks