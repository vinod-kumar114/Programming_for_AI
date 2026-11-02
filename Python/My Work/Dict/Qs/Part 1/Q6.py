# Loop — Finding Maximum Manually

# Given a dictionary mapping cricket players to the runs they scored, write a loop (do NOT use the built-in max() function directly on the dictionary) that finds and prints the player with the highest runs and their score.

runs = {'Babar': 117, 'Rizwan': 64, 'Shaheen': 12, 'Imam': 102, 'Fakhar': 45}

max_score = 0
player = None
    
for name, score in runs.items():
    if score>max_score:
        max_score=score
        player=name

print(player,max_score)

    
