import os
import json


data_dir = "/private/home/maxbartolo/_code/checklist/release_data/squad/"
data_file = "squad.json"

with open(os.path.join(data_dir, data_file), "r") as f:
    squad_data = json.load(f)

# Add answers
for dp in squad_data['data']:
    for para in dp['paragraphs']:
        for qa in para['qas']:
            qa['answers'] = []

# Save
with open(os.path.join(data_dir, "squad_ans.json"), "w") as f:
    json.dump(squad_data, f)
