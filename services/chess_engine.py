import random
import json
import re

class CHESSENGINE:
    def __init__(self) -> None:
        pass

    def get_valid_moves(self, pieces, color):
        valid_moves = []
        
        move_offsets = {
            'Pawn': [(1, 0), (1, -1), (1, 1)],  # forward, captures
            'Rook': [(0, 1), (0, -1), (1, 0), (-1, 0)],
            'Knight': [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)],
            'Bishop': [(1, 1), (1, -1), (-1, 1), (-1, -1)],
            'Queen': [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)],
            'King': [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        }
        
        for piece, position in pieces.items():
            if isinstance(position, list):
                positions = position
            else:
                positions = [position]
            
            for pos in positions:
                x, y = 8 - int(pos[1]), ord(pos[0]) - ord('a')  # Convert to (row, column)
                for move in move_offsets.get(piece.split('_')[0], []):  # Get move offsets
                    new_x, new_y = x + move[0], y + move[1]
                    
                    # Check if the new position is in bounds
                    if 0 <= new_x < 8 and 0 <= new_y < 8:
                        new_position = f"{chr(new_y + ord('a'))}{8 - new_x}"
                        
                        # Check if the new position is occupied by own piece (simple logic)
                        if not any(new_position in pos or new_position == pos for color_pos in pieces.values() for pos in (color_pos if isinstance(color_pos, list) else [color_pos])):
                            valid_moves.append({"piece": piece, "position": new_position})

        return valid_moves

    def next_best_move(self, black_pieces):
        valid_moves = self.get_valid_moves(black_pieces, 'black')
        if valid_moves:
            data = random.choice(valid_moves)
            print(f'CHESS_ENGINE: {data}')
            return data
        else:
            return {}
    
    def get_black_pieces(self, chessboard_str):
        # Replace single quotes with double quotes
        chessboard_str = chessboard_str.replace("'", '"')
        
        # Replace '=' with ':'
        chessboard_str = chessboard_str.replace('=', ':')
        
        # To ensure that all keys in the dictionary format are valid, we structure it to be a valid JSON
        # First, replace the outer braces to make it a valid dictionary
        chessboard_str = re.sub(r'^\s*{', '{', chessboard_str)  # Remove leading spaces if any
        chessboard_str = re.sub(r'}\s*$', '}', chessboard_str)  # Remove trailing spaces if any

        try:
            # Load the modified string as a dictionary
            chessboard_dict = json.loads(chessboard_str)
            return chessboard_dict['black_pieces']
        
        except json.JSONDecodeError as e:
            print("CHESS_ENGINE: Error decoding JSON:", e)
            return {}