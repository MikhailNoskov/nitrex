# Quick start bonus check calculation

## Main.py 

Users, UserTree creation

bfs_tree_pass() - function for passing the tree from top to bottom

check_referrals() - checking bonus conditions for current user and getting the list of referrals affecting the bonus


## Tests.py 

Some test cases for checking


### Custom case

Tree structure

```commandline
User 1 [1500]
    User 2 [1500]
        User 4 [1500]
            User 8 [1500]
            User 9 [1500]
        User 5 [1500]
            User 10 [1500]
            User 11 [1500]
    User 3 [1500]
        User 6 [1500]
            User 12 [500]
            User 13 [1500]
        User 7 [1500]
            User 14 [1500]
                User 16 [1500]
                User 17 [1500]
            User 15 [1500]
                User 18 [1500]
                User 19 [1500]
```

Result:

```commandline
1 [2, 4, 5, 3, 6, 7]
2 [4, 8, 9, 5, 10, 11]
3 []
4 []
5 []
6 []
7 [14, 16, 17, 15, 18, 19]
8 []
9 []
10 []
11 []
12 []
13 []
14 []
15 []
16 []
17 []
18 []
19 []

```