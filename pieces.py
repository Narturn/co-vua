from abc import ABC, abstractmethod
import rules

class Piece(ABC):
    def __init__(self, color, vi_tri_ban_dau):
        self.color = color
        self.vi_tri = vi_tri_ban_dau

    # Trả về chữ cái đại diện (R, N, B, Q, K, P)
    @abstractmethod
    def get_char_code(self):
        pass
    
    # Bắt lớp con tự tính đường đi theo hình học thô
    @abstractmethod
    def get_raw_moves(self, board_matrix):
        pass

    # Trả về danh sách các nước đi hợp lệ dựa trên luật cờ vua
    def get_valid_moves(self, board_matrix):
        raw_moves = self.get_raw_moves(board_matrix)
        valid_moves = []

        for row, col in raw_moves:
            if 0 <= row < 8 and 0 <= col < 8:  # Kiểm tra xem nước đi có nằm trong bàn cờ không
                valid_moves.append((row, col))
        return valid_moves

class Rook(Piece):
    def __init__(self, color, vi_tri_ban_dau):
        super().__init__(color, vi_tri_ban_dau)
    
    def get_char_code(self):
        return "R" if self.color == "white" else "r"

    def get_raw_moves(self, board_matrix):
        current_row, current_col = self.vi_tri
        return rules.rook_moves(current_row, current_col, board_matrix)