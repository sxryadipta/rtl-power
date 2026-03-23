import json
import os
import pandas as pd
import random

DATA_DIR = "data/json"
rows = []

for file in os.listdir(DATA_DIR):
    if file.endswith(".json"):
        with open(os.path.join(DATA_DIR, file)) as f:
            data = json.load(f)

        modules = data.get("modules", {})

        for module in modules.values():
            cells = module.get("cells", {})
            nets = module.get("netnames", {})

            cell_count = len(cells)
            wire_count = len(nets)

            and_count = sum("AND" in c["type"] for c in cells.values())
            or_count = sum("OR" in c["type"] for c in cells.values())
            not_count = sum("NOT" in c["type"] for c in cells.values())

            # Consistent synthetic power
            power = (
                0.5 * cell_count +
                0.3 * and_count +
                0.2 * or_count +
                0.1 * not_count +
                random.uniform(-5, 5)
            )

            rows.append([
                file, cell_count, wire_count,
                and_count, or_count, not_count,
                power
            ])

df = pd.DataFrame(rows, columns=[
    "design", "cells", "wires",
    "and_count", "or_count", "not_count",
    "power"
])

os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/dataset.csv", index=False)

print("Dataset ready.")