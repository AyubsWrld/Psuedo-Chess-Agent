class Player:
    BLACK = 'B'
    WHITE = 'W'

    def opponent(self) -> 'Player':
        return Player.BLACK if self == Player.WHITE else Player.WHITE
