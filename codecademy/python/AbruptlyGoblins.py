import unittest

MONDAY = 'MONDAY'
TUESDAY = 'TUESDAY'
WEDNESDAY = 'WEDNESDAY'
THURSDAY = 'THURSDAY'
FRIDAY = 'FRIDAY'
SATURDAY = 'SATURDAY'
SUNDAY = 'SUNDAY'
WEEKDAYS = [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY]
FORM_EMAIL = 'Hello {name}! You are invited to play {game} on {day}'


def add_gamer(gamers, gamer):
    gamers[gamer['name']] = gamer['availability']


def build_daily_frequency_table():
    return {day: 0 for day in WEEKDAYS}


def calculate_availability(availability_by_day, gamers):
    for availability in gamers.values():
        for weekday in availability:
            availability_by_day[weekday] += 1
    return availability_by_day


def find_optimal_day(gamers_by_day):
    return max(gamers_by_day, key=gamers_by_day.get)


def find_gamers_for_night(gamers, night):
    gamers_for_night = []
    for gamer, availability in gamers.items():
        if night in availability:
            gamers_for_night.append(gamer)
    return gamers_for_night


def send_email(invitees, night, game):
    return [FORM_EMAIL.format(name=invitee, game=game, day=night) for invitee in invitees]


class AbruptlyGoblinsTests(unittest.TestCase):
    gamers_by_day = build_daily_frequency_table()
    gamers = {}

    def setUp(self):
        self.gamers = {}
        add_gamer(self.gamers, {
            'name': 'Kimberly Warner', 'availability': [MONDAY, TUESDAY, FRIDAY]})
        add_gamer(self.gamers, {
            'name': 'Thomas Nelson', 'availability': [TUESDAY, THURSDAY, SATURDAY]})
        add_gamer(self.gamers, {
            'name': 'Joyce Sellers', 'availability': [MONDAY, WEDNESDAY, FRIDAY, SATURDAY]})
        add_gamer(self.gamers, {
            'name': 'Michelle Reyes', 'availability': [WEDNESDAY, THURSDAY, SUNDAY]})
        add_gamer(self.gamers, {
            'name': 'Stephen Adams', 'availability': [THURSDAY, SATURDAY]})
        add_gamer(self.gamers, {
            'name': 'Joanne Lynn', 'availability': [MONDAY, THURSDAY]})
        add_gamer(self.gamers, {
            'name': 'Latasha Bryan', 'availability': [MONDAY, SUNDAY]})
        add_gamer(self.gamers, {
            'name': 'Crystal Brewer', 'availability': [THURSDAY, FRIDAY, SATURDAY]})
        add_gamer(self.gamers, {
            'name': 'James Barnes Jr.', 'availability': [TUESDAY, WEDNESDAY, THURSDAY, SUNDAY]})
        add_gamer(self.gamers, {
            'name': 'Michel Trujillo', 'availability': [MONDAY, TUESDAY, WEDNESDAY]})

    def test_add_gamer(self):
        gamer_list = {}
        gamer = {'name': 'Kimberly Warner', 'availability': [MONDAY, TUESDAY, FRIDAY]}
        add_gamer(gamer_list, gamer)

        self.assertEqual({'Kimberly Warner': [MONDAY, TUESDAY, FRIDAY]}, gamer_list)

    def test_daily_frequency_table(self):
        self.assertEqual(7, len(build_daily_frequency_table()))

    def test_calculate_availability(self):
        calculate_availability(self.gamers_by_day, self.gamers)

        self.assertEqual(5, self.gamers_by_day.get(MONDAY))
        self.assertEqual(4, self.gamers_by_day.get(TUESDAY))
        self.assertEqual(4, self.gamers_by_day.get(WEDNESDAY))
        self.assertEqual(6, self.gamers_by_day.get(THURSDAY))
        self.assertEqual(3, self.gamers_by_day.get(FRIDAY))
        self.assertEqual(4, self.gamers_by_day.get(SATURDAY))
        self.assertEqual(3, self.gamers_by_day.get(SUNDAY))

    def test_find_optimal_day(self):
        optimal_day = find_optimal_day(self.gamers_by_day)
        self.assertIsNotNone(optimal_day)
        self.assertEqual(THURSDAY, optimal_day)

    def test_find_gamers_for_night(self):
        self.assertIsNotNone(find_gamers_for_night(self.gamers, THURSDAY))
        self.assertEqual(
            ['Thomas Nelson', 'Michelle Reyes', 'Stephen Adams', 'Joanne Lynn', 'Crystal Brewer', 'James Barnes Jr.'],
            find_gamers_for_night(self.gamers, THURSDAY))

    def test_send_email(self):
        invitees = find_gamers_for_night(self.gamers, THURSDAY)
        emails_to_send = send_email(invitees, THURSDAY, 'Abruptly Goblins')
        self.assertIsNotNone(emails_to_send)
        self.assertEqual(6, len(emails_to_send))
        self.assertEqual([
            'Hello Thomas Nelson! You are invited to play Abruptly Goblins on THURSDAY',
            'Hello Michelle Reyes! You are invited to play Abruptly Goblins on THURSDAY',
            'Hello Stephen Adams! You are invited to play Abruptly Goblins on THURSDAY',
            'Hello Joanne Lynn! You are invited to play Abruptly Goblins on THURSDAY',
            'Hello Crystal Brewer! You are invited to play Abruptly Goblins on THURSDAY',
            'Hello James Barnes Jr.! You are invited to play Abruptly Goblins on THURSDAY'],
            emails_to_send)

    def test_get_gamers_not_invited(self):
        invited = find_gamers_for_night(self.gamers, THURSDAY)
        unable_to_attend_best_night = {gamer: availability for gamer, availability in self.gamers.items()
                                       if gamer not in invited}

        self.assertEqual({'Kimberly Warner': ['MONDAY', 'TUESDAY', 'FRIDAY'],
                          'Joyce Sellers': ['MONDAY', 'WEDNESDAY', 'FRIDAY', 'SATURDAY'],
                          'Latasha Bryan': ['MONDAY', 'SUNDAY'],
                          'Michel Trujillo': ['MONDAY', 'TUESDAY', 'WEDNESDAY']},
                         unable_to_attend_best_night)


if __name__ == '__main__':
    unittest.main()
