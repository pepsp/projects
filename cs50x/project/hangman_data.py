hangman_lives = {
    0: '''
      ------
      |    |
      |
      |
      |
      |
    ------
    ''',
    1: '''
      ------
      |    |
      |    O
      |
      |
      |
    ------
    ''',
    2: '''
      ------
      |    |
      |    O
      |    |
      |
      |
    ------
    ''',
    3: '''
      ------
      |    |
      |    O
      |   /|
      |
      |
    ------
    ''',
    4: '''
      ------
      |    |
      |    O
      |   /|\\
      |
      |
    ------
    ''',
    5: '''
      ------
      |    |
      |    O
      |   /|\\
      |   /
      |
    ------
    ''',
    6: '''
      ------
      |    |
      |    O < AHH, I"M HANGED!)
      |   /|\\
      |   / \\
      |
    ------
    '''
}


difficulty = {
    "easy": ["bark", "jump", "kite", "wall", "hand", "fish", "lake", "snow", "song", "tree", "cart", "nose",
             "talk", "king", "flag", "wave", "lamp", "coin", "rock", "star"],
    "hard": ["adventure", "chocolatey", "formidable", "disapprove", "questioning", "celebrator", "mysterious", "remarkable", "treasured",
             "awareness", "generation", "understand", "opportunity", "happiness", "continuous", "incredible", "decorate", "landscape",
             "tournament", "innovation"]
}


def get_hang(n):
    print(hangman_lives[n])


if __name__ == "__main__":
    main()
