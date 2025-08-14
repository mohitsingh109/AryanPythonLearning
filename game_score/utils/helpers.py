def sort_players(players):
    sorted_player_scores = sorted(players, key=lambda player: player.get_score(), reverse=True)
    return sorted_player_scores

def validation(score):
    if isinstance(score, int) and score >= 0:
        return True
    return False

