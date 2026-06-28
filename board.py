from pieces import Rook

class ChesBoard:
    def __init__(self):
        # Khởi tạo bàn cờ 8x8 với tất cả ô trống (".")
        self.matrix = [["." for _ in range(8)] for _ in range(8)]
        self.setup_pieces()

    def setup_pieces(self):
        # xắp xếp quân xe trắng ở hàng 0 và quân xe đen ở hàng 7
        self.matrix[0][0] = Rook("white", (0, 0))
        self.matrix[0][7] = Rook("white", (0, 7))
        self.matrix[7][0] = Rook("black", (7, 0))
        self.matrix[7][7] = Rook("black", (7, 7))

    def display(self):
        # Hiển thị bàn cờ
        output = "\n 0 1 2 3 4 5 6 7\n"
        output += "  ----------------\n"
        
        for row_indef, row_data in enumerate(self.matrix):
            row_str = f"{row_indef}| "
            for cell in row_data:
                if cell == ".":
                    row_str += ". "
                else:
                    row_str += f"{cell.get_char_code()} "
            output += row_str + "\n"
        
        return output