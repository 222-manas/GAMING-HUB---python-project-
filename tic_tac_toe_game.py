import tkinter as tk
from tkinter import messagebox

def check_win(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def check_draw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe")
        self.scores = {'X': 0, 'O': 0}
        self.total_rounds = 0
        self.draws = 0
        self.start_new_game()

    def start_new_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.player = 'X'
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self, text=' ', font=('Arial', 40), width=5, height=2, command=lambda row=i, col=j: self.click(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.player
            self.buttons[row][col].config(text=self.player)

            if check_win(self.board, self.player):
                self.scores[self.player] += 1
                self.total_rounds += 1
                self.game_over(f"Player {self.player} wins!")
            elif check_draw(self.board):
                self.draws += 1
                self.total_rounds += 1
                self.game_over("It's a draw!")
            else:
                self.player = 'O' if self.player == 'X' else 'X'

    def game_over(self, message):
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)
        messagebox.showinfo("Game Over", message)
        self.ask_to_continue()

    def ask_to_continue(self):
        if messagebox.askyesno("Continue", "Do you want to play the next game?"):
            self.start_new_game()
        else:
            self.show_final_scores()

    def show_final_scores(self):
        final_message = f"Total Rounds Played: {self.total_rounds}\n"
        final_message += f"Final Scores:\nPlayer X: {self.scores['X']}\nPlayer O: {self.scores['O']}\nDraws: {self.draws}\n"
        
        if self.scores['X'] > self.scores['O']:
            final_message += "Player X is the overall winner!"
        elif self.scores['O'] > self.scores['X']:
            final_message += "Player O is the overall winner!"
        else:
            final_message += "It's an overall draw!"
        
        final_message += "\n\nMade by Rahul Kumar Agrawal"
        messagebox.showinfo("Game Over", final_message)
        self.quit()

if __name__ == "__main__":
    game = TicTacToe()
    game.mainloop()