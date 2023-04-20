def knight_tour(n):
    # Khởi tạo bàn cờ
    board = [[-1 for i in range(n)] for j in range(n)]

    # Di chuyển của mã
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Đánh dấu ô bắt đầu đã được đi qua
    board[0][0] = 0

    # Thực hiện di chuyển
    if knight_tour_helper(n, board, 0, 0, 1, move_x, move_y) == False:
        print("Không tìm thấy giải pháp!")
    else:
        print_board(board)


def knight_tour_helper(n, board, curr_x, curr_y, move_count, move_x, move_y):
    # Nếu đã đi hết bàn cờ thì trả về True
    if move_count == n * n:
        return True

    # Thử tất cả các nước đi có thể
    for i in range(8):
        next_x = curr_x + move_x[i]
        next_y = curr_y + move_y[i]

        # Kiểm tra xem nước đi có hợp lệ không
        if next_x >= 0 and next_y >= 0 and next_x < n and next_y < n and board[next_x][next_y] == -1:
            board[next_x][next_y] = move_count
            if knight_tour_helper(n, board, next_x, next_y, move_count + 1, move_x, move_y) == True:
                return True

            # Nếu nước đi không dẫn đến giải pháp, quay lại và thử nước đi khác
            board[next_x][next_y] = -1

    return False