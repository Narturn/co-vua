class ChesBoard:
    def __init__(self):
        # Khởi tạo bàn cờ 8x8 với tất cả ô trống (".")
        self.board = [["." for _ in range(8)] for _ in range(8)]
        # Đặt quân cờ ban đầu
        self.board[0] = ["r", "n", "b", "q", "k", "b", "n", "r"]  # Hàng 1: quân đen
        self.board[1] = ["p" for _ in range(8)]  # Hàng 2: quân đen
        self.board[6] = ["P" for _ in range(8)]  # Hàng 7: quân trắng
        self.board[7] = ["R", "N", "B", "Q", "K", "B", "N", "R"]  # Hàng 8: quân trắng