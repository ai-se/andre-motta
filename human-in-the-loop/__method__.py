from fileIO import IO
from satsolver import SATSolver
from tree_cluster import sway
from ranker import Ranker
from search import Search
import math

QUESTION_IMPORTANCE_DECAY_FACTOR = 0.1
DECAY_FACTOR = 0.9
INCREASE_FACTOR = 1.1


class Method:
    def __init__(self):
        names, cnf = IO.read_dimacs('Scrum.dimacs')
        self.items = SATSolver.get_solutions(10000, cnf)
        self.weights = [0.5] * len(self.items)
        self.tree = sway(self.items, 100)
        self.names = names
        self.rank = Ranker.level_rank_features(self.tree, self.weights)
        self.cur_best_node = Ranker.rank_nodes(self.tree, self.rank)
        self.questions = IO.get_question_text('terms_sentence_map.csv', 'sentence')

    def find_node(self):
        return Search.bfs(self.tree, self.cur_best_node)

    def pick_questions(self, node):
        diff = node.diff_array()
        ranked_ranks = sorted(self.rank, reverse=True)
        ranks = ranked_ranks[:4]
        ranks.reverse()
        ranks = set(ranks)
        return self.get_index(diff, ranks)

    def get_index(self, diff, ranks):
        questions = []
        for r in ranks:
            for i in range(len(diff)):
                if r == self.rank[i] and diff[i]:
                    questions.append(i)
        return questions

    def ask_questions(self, q_idx, node):
        east_options, west_options = [], []
        for i in range(min(len(q_idx), 4)):
            if node.east[0].item[q_idx[i]]:
                east_options.append(self.questions[q_idx[i]])
            elif node.west[0].item[q_idx[i]]:
                west_options.append(self.questions[q_idx[i]])

        len_east = len(east_options)
        len_west = len(west_options)
        diff = abs(len_east - len_west)
        if len_east > len_west:
            for i in range(diff):
                west_options.append('           ')
        else:
            for i in range(diff):
                east_options.append('           ')
        print('Would you rather')
        print('Option 1 \t Option 2')
        for e, w in zip(east_options, west_options):
            print('1 -', e, '\t', '2 -', w)

    def adjust_weights(self, node, picked, q_idx):
        node.asked += 1
        if picked == 0:  # EAST
            for i in range(min(len(q_idx), 4)):
                self.weights[q_idx[i]] *= QUESTION_IMPORTANCE_DECAY_FACTOR
            self.adjust_up(node.east_node)
            self.adjust_down(node.west_node)
        if picked == 1:  # WEST
            for i in range(min(len(q_idx), 4)):
                self.weights[q_idx[i]] *= QUESTION_IMPORTANCE_DECAY_FACTOR
            self.adjust_up(node.west_node)
            self.adjust_down(node.east_node)

    def adjust_up(self, node, depth=0, growth_factor=INCREASE_FACTOR):
        # f(t)=A⋅log(t)+B
        node.weight *= growth_factor
        growth_factor *= (DECAY_FACTOR ** depth)
        if node.east_node is not None and node.west_node is not None:
            self.adjust_up(node.east_node, depth + 1, growth_factor)
            self.adjust_up(node.west_node, depth + 1, growth_factor)

    def adjust_down(self, node, depth=0):
        # y=a(1-b)^x
        node.weight *= (DECAY_FACTOR ** depth)
        if node.east_node is not None and node.west_node is not None:
            self.adjust_down(node.east_node, depth + 1)
            self.adjust_down(node.west_node, depth + 1)

    def re_rank(self):
        self.rank = Ranker.level_rank_features(self.tree, self.weights)
        self.cur_best_node = Ranker.rank_nodes(self.tree, self.rank)

    def check_solution(self):
        value = Ranker.check_solution(self.tree)
        if value is None:
            return None
        return Search.bfs(self.tree, value)

    def get_item(self, path):
        return Search.get_item(self.tree, path)
