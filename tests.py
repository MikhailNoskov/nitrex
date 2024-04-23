from main import *
import datetime
from unittest import TestCase


class TestTrees(TestCase):
    def setUp(self):
        self.tree = UserTree()

    def test_tariff_and_date_ok(self):
        users = [User(user_id=i, ambassador_id=i // 2, tariff=1500, purchased=datetime.datetime.now()) for i in range(1, 8)]
        self.tree.users = {i + 1: user for i, user in enumerate(users)}

        self.tree.tree_structure = {
            1: [2, 3],
            2: [4, 5],
            3: [6, 7],
            4: [],
            5: [],
            6: [],
            7: []
        }

        expected = {1: [2, 4, 5, 3, 6, 7], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
        result = bfs_tree_pass(self.tree)
        print(result)

        self.assertEqual(expected, result)

    def test_tariff_500(self):
        users = [User(user_id=i, ambassador_id=i // 2, tariff=1500, purchased=datetime.datetime.now()) for i in range(1, 8)]
        users[5].tariff = 500
        self.tree.users = {i + 1: user for i, user in enumerate(users)}

        self.tree.tree_structure = {
            1: [2, 3],
            2: [4, 5],
            3: [6, 7],
            4: [],
            5: [],
            6: [],
            7: []
        }

        expected = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
        result = bfs_tree_pass(self.tree)
        print(result)

        self.assertEqual(expected, result)

    def test_late_date(self):
        users = [User(user_id=i, ambassador_id=i // 2, tariff=1500, purchased=datetime.datetime.now()) for i in range(1, 8)]
        users[5].purchased += datetime.timedelta(days=60)
        self.tree.users = {i + 1: user for i, user in enumerate(users)}

        self.tree.tree_structure = {
            1: [2, 3],
            2: [4, 5],
            3: [6, 7],
            4: [],
            5: [],
            6: [],
            7: []
        }

        expected = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
        result = bfs_tree_pass(self.tree)
        print(result)

        self.assertEqual(expected, result)

    def test_20_persons(self):
        users = [User(user_id=i, ambassador_id=i // 2, tariff=500, purchased=datetime.datetime.now()) for i in range(1, 21)]
        self.tree.users = {i + 1: user for i, user in enumerate(users)}
        for user in users[8:19]:
            user.tariff = 1500
        users[17].tariff = 500

        self.tree.tree_structure = {
            1: [2, 3],
            2: [4, 5],
            3: [6, 7],
            4: [8, 9],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [10, 11],
            10: [12, 13],
            11: [14, 15],
            12: [16, 17],
            13: [18, 19],
            14: [20],
            15: [],
            16: [],
            17: [],
            18: [],
            19: [],
            20: []
        }

        expected = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [10, 12, 13, 11, 14, 15], 10: [],
                    11: [], 12: [], 13: [], 14: [], 15: [], 16: [], 17: [], 18: [], 19: [], 20: []}
        result = bfs_tree_pass(self.tree)
        print(result)

        self.assertEqual(expected, result)
