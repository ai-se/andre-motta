from __method__ import Method
from oracle import Oracle
import pandas as pd
import numpy as np
import time

folder = 'CSVModels/'
filename = 'FFM-1000-200-0.50-SAT-1.csv'


a, p, c, s, d, u, scores, t = [], [], [], [], [], [], [], []

for i in range(20):
    start_time = time.time()
    m = Method(folder+filename)
    o = Oracle(len(m.rank))
    asked = 0
    first_qidx = set()
    while True:
        path, node = m.find_node()
        # print("Node id =", node.id)
        q_idx = m.pick_questions(node)
        #m.ask_questions(q_idx, node)
        for q in q_idx:
            first_qidx.add(q)
        asked += 1
        picked = o.pick(q_idx, node)
        m.adjust_weights(node, picked, q_idx)
        m.re_rank()
        solutions = m.check_solution()
        if solutions is not None:
            print("Found solution in", asked, "questions")
            print("Selected", np.sum(o.picked), "features")
            print("Went down to", len(solutions), "items")
            for item in solutions:
                item.selectedpoints = np.sum(np.multiply(item.item, o.picked)) / np.sum(o.picked) * 100

            best = m.pick_best(solutions)
            a.append(asked)
            p.append(np.sum(o.picked))
            c.append(best.totalcost)
            s.append(best.selectedpoints)
            d.append(best.knowndefects)
            u.append(best.featuresused)
            scores.append(best.score)
            t.append(time.time() - start_time)
            break

df = pd.DataFrame(
    {
        'Asked': a,
        'User Picked': p,
        'Cost': c,
        'Selected Points': s,
        'Known Defects': d,
        'Features Used': u,
        'Score': scores,
        'Time': t
     }).T
df.to_csv('Scores/Score'+filename)
