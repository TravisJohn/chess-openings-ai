import csv
from pathlib import Path

def load_chess_openings(file_path):
    openings = []
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            opening = {
                'id': row['Event'],  # Adjust field names as necessary
                'content': f"{row['Event']} is a chess opening. It typically begins with the moves: {row['Moves'][:30]}...",
                'metadata': {
                    'name': row['Event'],
                    'moves': row['Moves'],
                    'white': row['White'],
                    'black': row['Black'],
                    'result': row['Result']
                }
            }
            openings.append(opening)
    return openings

def get_chess_openings_data():
    file_path = Path(__file__).parent.parent.parent / 'data' / 'chess_openings' / 'openings.csv'
    return load_chess_openings(file_path)