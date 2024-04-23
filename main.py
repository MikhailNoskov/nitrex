import datetime
import random


TARIFFS = [500, 1500, 3000]


class User:
    def __init__(self, user_id: int, purchased: datetime.datetime, tariff: int, ambassador_id: int = None):
        self.id = user_id
        self.ambassador_id = ambassador_id
        self.purchased = purchased
        self.tariff = tariff

    def __str__(self):
        return f'User - {self.id} parent - {self.ambassador_id} tariff {self.tariff} purchased on {self.purchased}'


class UserTree:
    def __init__(self):
        self.users = dict()
        self.tree_structure = dict()

    def create_user(self):
        if self.tree_structure.keys():
            new_user_id = max(self.tree_structure.keys()) + 1
        else:
            new_user_id = 1
        if self.tree_structure:
            abm_id = random.choice(list(self.tree_structure.keys()))
        else:
            abm_id = None
        if abm_id:
            purchased = self.users[abm_id].purchased + datetime.timedelta(days=random.choice(range(15)))
        else:
            purchased = datetime.datetime.now().date()
        tariff = random.choice(TARIFFS)
        return User(user_id=new_user_id, ambassador_id=abm_id, purchased=purchased, tariff=tariff)

    def add_new_user(self):
        user = self.create_user()
        self.users[user.id] = user
        try:
            self.tree_structure[user.ambassador_id].append(user.id)
        except KeyError:
            pass
        self.tree_structure[user.id] = []


def check_referrals(parent_id: int, tree: UserTree) -> list:
    """
    Function for bonus receipt conditions check
    :param parent_id: id of the current ambassador being checked
    :param tree: UserTree
    :return:list of referrals affecting the bonus
    """
    current_parent = tree.users[parent_id]
    cu_tariff = current_parent.tariff
    referrals = []
    if len(tree.tree_structure[parent_id]) < 2 or cu_tariff < 1500:
        return []
    for child_id in tree.tree_structure[parent_id]:
        child_user = tree.users[child_id]
        if len(tree.tree_structure[child_id]) >= 2:
            if child_user.tariff >= 1500 and (child_user.purchased - current_parent.purchased).days <= 30:
                grands = []
                count = 0
                for grand_child_id in tree.tree_structure[child_id]:
                    gc_user = tree.users[grand_child_id]
                    if gc_user.tariff >= 1500 and (gc_user.purchased - current_parent.purchased).days <= 30:
                        grands.append(grand_child_id)
                        count += 1
                        if count == 2:
                            break
                if count >= 2:
                    referrals.append(child_id)
                    referrals += grands
    length = len(referrals)
    if length >= 6:
        new_length = length // 6
        referrals = referrals[:new_length * 6]
        return referrals
    else:
        return []


def bfs_tree_pass(tree: UserTree) -> dict:
    """
    Function to pass the tree with breadth first search
    :param tree: UserTree
    :return: Dict with ambassadors ids as keys and lists of referrals bringing the bonus as values
    """
    resulted_data = dict()
    queue = [1]

    while queue:
        node = queue.pop(0)
        if node not in resulted_data:
            referrals = check_referrals(node, tree)
            resulted_data[node] = referrals
            neighbours = tree.tree_structure[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    return resulted_data


if __name__ == '__main__':
    user_tree = UserTree()
    for _ in range(10000):
        user_tree.add_new_user()
    # print(user_tree.tree_structure)
    for _, value in user_tree.users.items():
        print(value)
    result = bfs_tree_pass(user_tree)
    for k, v in result.items():
        print(k, v)
