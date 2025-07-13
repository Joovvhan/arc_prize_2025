import json
import os

arc_base_dir = '../arc-prize-2025'

def load_data(target="training"):

    challenge_file = os.path.join(arc_base_dir, f"arc-agi_{target}_challenges.json")
    solution_file = os.path.join(arc_base_dir, f"arc-agi_{target}_solutions.json")

    with open(challenge_file, "r") as f:
        challenge_data = json.load(f)

    with open(solution_file, "r") as f:
        solution_data = json.load(f)

    return challenge_data, solution_data