class Solution:
    def traverse_node(self, word, y, x):
      if y < 0 or y >= len(self.board) or x < 0 or x >= len(self.board[0]):
        return False
      if self.board[y][x] is None or self.board[y][x] != word[0]:
        return False
      next_word = word[1:]
      if len(next_word) == 0:
        return True
      self.board[y][x] = None
      result = self.traverse_node(next_word, y - 1, x) or self.traverse_node(next_word, y, x + 1) or self.traverse_node(next_word, y + 1, x) or self.traverse_node(next_word, y, x - 1)
      self.board[y][x] = word[0]
      return result
        
    def exist(self, board: List[List[str]], word: str) -> bool:
      self.board = board
      unq = {i for i in word}
      for y in range(len(board)):
          for x in range(len(board[0])):
              if board[y][x] not in unq:
                board[y][x] = None
                continue
              if (self.traverse_node(word, y, x)):
                return True
      return False
