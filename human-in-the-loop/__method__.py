import scipy.stats as st
from fileIO import IO
from satsolver import SATSolver
from tree_cluster import sway
from ranker import Ranker
from search import Search
import math
import sys
import numpy as np

QUESTION_IMPORTANCE_DECAY_FACTOR = 0.1
DECAY_FACTOR = 0.9
INCREASE_FACTOR = 1.1


class Method:
    def __init__(self, filename):
        x = 5000
        sys.setrecursionlimit(x)
        #names, cnf = IO.read_dimacs('SPLOT-3CNF-FM-500-50-1.00-SAT-10')
        self.items = SATSolver.get_solutions(10000, filename)
        self.weights = [1] * len(self.items)
        self.tree = sway(self.items, 100)
        self.names = [] #names
        # Weight of top node = 0
        # self.tree.weight = 0
        self.rank = Ranker.level_rank_features(self.tree, self.weights)
        self.cur_best_node = Ranker.rank_nodes(self.tree, self.rank)
        self.questions = IO.get_question_text('terms_sentence_map.csv', 'sentence')

    def find_node(self):
        return Search.bfs(self.tree, self.cur_best_node)

    def pick_questions(self, node):
        diff = node.diff_array()
        ranked_ranks = sorted(self.rank, reverse=True)
        ranks = [x for x in ranked_ranks if x != 0]
        ranks.reverse()
        ranks = set(ranks)
        return self.get_index(diff, ranks)

    def adjust_tree(self, node, q_idx):
        if node.west:
            for i in q_idx:
                if i in node.west[0].item:
                    node.west_node.weight = 0
                    self.adjust_tree(node.west_node, q_idx)
        if node.east:
            for i in q_idx:
                if i in node.east[0].item:
                    node.east_node.weight = 0
                    self.adjust_tree(node.east_node, q_idx)

    def get_index(self, diff, ranks):
        questions = []
        for r in ranks:
            for i in range(len(diff)):
                if r == self.rank[i] and diff[i]:
                    questions.append(i)
        return questions

    def ask_questions(self, q_idx, node):
        east_options, west_options = [], []
        for i in range(len(q_idx)):
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
        east_options, west_options = [], []
        for i in range(len(q_idx)):
            if node.east[0].item[q_idx[i]]:
                east_options.append(q_idx[i])
            elif node.west[0].item[q_idx[i]]:
                west_options.append(q_idx[i])
        if picked == 0:  # EAST
            for i in range(len(q_idx)):
                self.weights[q_idx[i]] = 0
            self.adjust_down(node.west_node)
            self.adjust_tree(self.tree, west_options)
        if picked == 1:  # WEST
            for i in range(len(q_idx)):
                self.weights[q_idx[i]] = 0
            self.adjust_down(node.east_node)
            self.adjust_tree(self.tree, east_options)




    #OBSOLETE
    def adjust_up(self, node, depth=0, growth_factor=INCREASE_FACTOR):
        # check for presence of no answers. If so
        node.weight *= growth_factor
        growth_factor *= (DECAY_FACTOR ** depth)
        if node.east_node is not None and node.west_node is not None:
            self.adjust_up(node.east_node, depth + 1, growth_factor)
            self.adjust_up(node.west_node, depth + 1, growth_factor)

    def adjust_down(self, node, depth=0):
        # weight = 0
        node.weight = 0
        if node.east_node is not None and node.west_node is not None:
            self.adjust_down(node.east_node, depth + 1)
            self.adjust_down(node.west_node, depth + 1)

    def re_rank(self):
        self.rank = Ranker.level_rank_features(self.tree, self.weights)
        self.cur_best_node = Ranker.rank_nodes(self.tree, self.rank)

    def check_solution(self):
        if sum(self.rank) == 0:
            return Search.get_all_items(self.tree)
        value = Ranker.check_solution(self.tree)
        if value is None:
            return None
        return Search.get_all_items(self.tree)

    def get_item(self, path):
        return Search.get_item(self.tree, path)

    def pick_best(self,solutions):
        sumsq = lambda *args: sum([i ** 2 for i in args])
        all_items = Search.get_all_leaves(self.tree)
        scores = list(map(lambda x: sumsq(x.totalcost, x.knowndefects, 124-x.featuresused, 1.5*(100 - x.selectedpoints))
                          , solutions))
        total_scores = list(map(lambda x: sumsq(x.totalcost, x.knowndefects, 124-x.featuresused, 1.5*(100 -
                                                                                                      x.selectedpoints))
                                , all_items))
        minimizer = np.argmin(scores)
        solutions[minimizer].score = st.percentileofscore(total_scores, scores[minimizer])
        return solutions[minimizer]

