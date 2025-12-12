import pandas as pd
from doubt_solver import DoubtSolver
from config import DATASET_PATH

solver = DoubtSolver(DATASET_PATH)

df = pd.read_csv(DATASET_PATH)

correct = 0
total = len(df)

for q, a in zip(df["question"], df["answer"]):
    predicted_answer, score = solver.ask(q)
    if predicted_answer == a:
        correct += 1

print(f"Model consistency score: {correct}/{total} = {correct/total:.2f}")