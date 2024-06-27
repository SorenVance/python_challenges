import unittest

letter_to_points = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
                    'K': 5, 'L': 1, 'M': 3, 'N': 4, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
                    'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10, ' ': 0}


def score_word(word):
    score = 0
    for letter in word.upper():
        score += letter_to_points.get(letter, 0)
    return score


def score_words(words):
    score = 0
    for word in words:
        score += score_word(word)
    return score


def score_game(game):
    game_score = {}
    for player, words_and_score in game.items():
        game_score[player] = score_words(words_and_score[1])
    return game_score


def play_word(player_words, player, word):
    current_words_and_score = player_words[player]
    new_score = current_words_and_score[0] + score_word(word)
    new_words = current_words_and_score[1].copy() + [word.upper()]
    player_words[player] = (new_score, new_words)


class ListSorterTests(unittest.TestCase):
    player_words = {}

    def setUp(self):
        self.player_words = {'player1': (29, ['BLUE', 'TENNIS', 'EXIT']),
                             'wordNerd': (32, ['EARTH', 'EYES', 'MACHINE']),
                             'Lexi Con': (31, ['ERASER', 'BELLY', 'HUSKY']),
                             'Prof Reader': (31, ['ZAP', 'COMA', 'PERIOD'])}

    def test_score_word_givenSingleLetter_ReturnsExpectedPoints(self):
        self.assertEqual(1, score_word('A'))
        self.assertEqual(3, score_word('B'))
        self.assertEqual(10, score_word('Z'))

    def test_score_word_GivenWord_ReturnsExpectedPoints(self):
        self.assertIsNotNone(score_word('CAT'))
        self.assertEqual(5, score_word('CAT'))
        self.assertEqual(5, score_word('DOG'))
        self.assertEqual(10, score_word('RABBIT'))
        self.assertEqual(27, score_word('XYLOPHONE'))
        self.assertEqual(27, score_word('xylophone'))

    def test_score_game(self):
        self.assertEqual(29, score_words(['BLUE', 'TENNIS', 'EXIT']))

    def test_score_game_withMultiplePlayers(self):
        game_score = score_game(self.player_words)
        self.assertEqual(29, game_score['player1'])
        self.assertEqual(32, game_score['wordNerd'])
        self.assertEqual(31, game_score['Lexi Con'])
        self.assertEqual(31, game_score['Prof Reader'])

    def test_play_word_AddsWordToPlayerList(self):
        self.assertIsNone(play_word(self.player_words, 'player1', 'XYLOPHONE'))
        self.assertEqual((56, ['BLUE', 'TENNIS', 'EXIT', 'XYLOPHONE']), self.player_words['player1'])

    def test_run_game_from_scratch(self):
        game = {'player1': (0, []), 'wordNerd': (0, []), 'Lexi Con': (0, []), 'Prof Reader': (0, [])}
        play_word(game, 'player1', 'BLUE')
        play_word(game, 'wordNerd', 'EARTH')
        play_word(game, 'Lexi Con', 'ERASER')
        play_word(game, 'Prof Reader', 'zap')

        play_word(game, 'player1', 'TENNIS')
        play_word(game, 'wordNerd', 'eyes')
        play_word(game, 'Prof Reader', 'COMA')
        play_word(game, 'Lexi Con', 'BELLY')

        play_word(game, 'player1', 'exit')
        play_word(game, 'wordNerd', 'MACHINE')
        play_word(game, 'Lexi Con', 'HUSKY')
        play_word(game, 'Prof Reader', 'PERIOD')

        self.assertEqual(self.player_words, game)


if __name__ == '__main__':
    unittest.main()
