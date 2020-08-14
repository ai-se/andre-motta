from __method__ import Method
from oracle import Oracle
import pandas as pd

a, g, t, p = [], [], [], []

for i in range(20):
    m = Method()
    o = Oracle(len(m.rank))
    asked = 0
    first_qidx = set()
    while True:
        path, node = m.find_node()
        q_idx = m.pick_questions(node)
        m.ask_questions(q_idx, node)
        for q in q_idx:
            first_qidx.add(q)
        asked += 1
        picked = o.pick(q_idx, node)
        m.adjust_weights(node, picked, q_idx)
        m.re_rank()
        solution = m.check_solution()
        if solution is not None:
            print("Found solution in", asked, "questions")
            a.append(asked)
            item = m.get_item(solution[0])
            total = len(first_qidx)
            t.append(total)
            good = 0
            for q in first_qidx:
                if o.picked[q] == item[q]:
                    good += 1
            g.append(good)
            p.append(good / total)
            print(good, total, good / total)
            print(o.picked)
            print(item)

            break

df = pd.DataFrame(
    {'QuestionsAsked': a,
     'Total': t,
     'Good': g,
     'Precision': p
     })
df.to_csv('experiment.csv')
