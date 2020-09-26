# CSPT10 Graphs IV

from collections import deque
import random
import math
import time

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        for i in range(0, num_users):
            self.add_user(f"User {i}")
        possible_friendships = []
        # Generate all possible friendships possible
        for user_id in self.users:
            # To avoid duplicating friendships, create friendships from user_id + 1
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # Shuffle the entire array of possible friendships
        random.shuffle(possible_friendships)

        # Select the first num_users * avg_friendships / 2
        # We / 2 because a friendship is a bidirectional edge (we're essentially adding two edges)
        for i in range(0, math.floor(num_users * avg_friendships / 2)):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])


    def populate_graph_linear(self, num_users, avg_friendships):
        # Keep randomly making friendships until we've made the right amount
        # randomly select two vertices to become friends
        # if it's a success, then increment number of friendships made
        # else try again
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        for i in range(0, num_users):
            self.add_user(f"User {i}")

        target_friendships = num_users * avg_friendships
        total_friendships = 0
        collisions = 0

        while total_friendships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            if self.add_friendship_linear(user_id, friend_id):
                total_friendships += 2
            else:
                collisions += 1
        print(f"collisions: {collisions}")

    # returns true if making friendship was a success
    def add_friendship_linear(self, user_id, friend_id):
        if user_id == friend_id:
            return False
        # we don't wanna make a friendship if it already exists
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {} # a dictionary mapping from node id --> [path from user_Id]
        queue = deque() # we need this for a bft
        queue.append([user_id])
        while len(queue) > 0:
            currPath = queue.popleft()
            currNode = currPath[-1]
            visited[currNode] = currPath # bft guarantees us that this is the shortest path to currNode from user_id
            for friend in self.friendships[currNode]:
                if friend not in visited:
                    newPath = currPath.copy()
                    newPath.append(friend)
                    queue.append(newPath)
        return visited

if __name__ == '__main__':
    sg = SocialGraph()
    start_time = time.time()
    sg.populate_graph(1000, 5)
    end_time = time.time()
    print (f"runtime: {end_time - start_time} seconds")
    connections = sg.get_all_social_paths(1)
    # print(sg.friendships)
    # print(connections)
    total = 0
    for user_id in connections:
        total += len(connections[user_id]) - 1
    print(len(connections))
    print(total / len(connections))

    total_connections = 0
    total_degrees = 0
    iterations = 10
    for i in range(0, iterations):
        sg.populate_graph(1000, 5)
        connections = sg.get_all_social_paths(1)
        total = 0
        for user_id in connections:
            total += len(connections[user_id]) - 1
        total_connections += len(connections)
        total_degrees += total / len(connections)
        print("-----")
        print(f"Friends in network: {len(connections)}")
        print(f"Avg degrees: {total / len(connections)}")
    print(total_connections / iterations)
    print(total_degrees / iterations)
