def main():
    print('''Please pick one:
                rock
                scissors
                paper''')

    while True:
        game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
        player_one = str(input("Player one: "))
        player_two = str(input("Player two: "))
        play_player_one = game_dict.get(player_one)
        play_player_two = game_dict.get(player_two)
        difference = play_player_one - play_player_two

        if difference in [-1, 2]:
            print('Player one wins')
        elif difference in [-2, 1]:
            print('Player two wins')
        else:
            print('It`s a Draw. Please continue.\n')
            continue

        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('Game Over')
            break


if __name__ == "__main__":
    main()
