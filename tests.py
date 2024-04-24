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

    def test_custom_case(self):
        date = datetime.datetime.now()

        self.tree.users[1] = User(user_id=1, tariff=1500, purchased=date)
        self.tree.users[2] = User(user_id=2, ambassador_id=1, tariff=1500, purchased=date)
        self.tree.users[3] = User(user_id=3, ambassador_id=1, tariff=1500, purchased=date)

        self.tree.users[4] = User(user_id=4, ambassador_id=2, tariff=1500, purchased=date)
        self.tree.users[5] = User(user_id=5, ambassador_id=2, tariff=1500, purchased=date)

        self.tree.users[6] = User(user_id=6, ambassador_id=3, tariff=1500, purchased=date)
        self.tree.users[7] = User(user_id=7, ambassador_id=3, tariff=1500, purchased=date)

        self.tree.users[8] = User(user_id=8, ambassador_id=4, tariff=1500, purchased=date)
        self.tree.users[9] = User(user_id=9, ambassador_id=4, tariff=1500, purchased=date)

        self.tree.users[10] = User(user_id=10, ambassador_id=5, tariff=1500, purchased=date)
        self.tree.users[11] = User(user_id=11, ambassador_id=5, tariff=1500, purchased=date)

        self.tree.users[12] = User(user_id=12, ambassador_id=6, tariff=500, purchased=date)
        self.tree.users[13] = User(user_id=13, ambassador_id=6, tariff=1500, purchased=date)

        self.tree.users[14] = User(user_id=14, ambassador_id=7, tariff=1500, purchased=date)
        self.tree.users[15] = User(user_id=15, ambassador_id=7, tariff=1500, purchased=date)

        self.tree.users[16] = User(user_id=16, ambassador_id=14, tariff=1500, purchased=date)
        self.tree.users[17] = User(user_id=17, ambassador_id=14, tariff=1500, purchased=date)

        self.tree.users[18] = User(user_id=18, ambassador_id=15, tariff=1500, purchased=date)
        self.tree.users[19] = User(user_id=19, ambassador_id=15, tariff=1500, purchased=date)

        self.tree.tree_structure = {
            1: [2, 3],
            2: [4, 5],
            3: [6, 7],
            4: [8, 9],
            5: [10, 11],
            6: [12, 13],
            7: [14, 15],
            8: [],
            9: [],
            10: [],
            11: [],
            12: [],
            13: [],
            14: [16, 17],
            15: [18, 19],
            16: [],
            17: [],
            18: [],
            19: []
        }

        result = bfs_tree_pass(self.tree)
        for k, v in result.items():
            print(k, v)
