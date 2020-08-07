from players import Players

player1 = Players(1)

player1.rank=4
player_rank_change = 1
def change_ranks(player1, player_rank_change):
    if player_rank_change == 1 and player1.rank <= 3:
        player1.rank += 1
    elif player_rank_change == 2 and player1.rank <=2:
        player1.rank += 2
    elif player_rank_change == -1 and player1.rank >= 2:
        player1.rank -= 1
    elif player_rank_change == -1 and player1.rank == 1:
        player1.rank = 1
    else:
        pass
    return player1.rank
print(change_ranks(player1, player_rank_change))