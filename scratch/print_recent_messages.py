import os
import json

transcript_path = "/Users/anilgopakumar/.gemini/antigravity/brain/1517de7a-87b6-4ba5-b261-bb6e77038596/.system_generated/logs/transcript.jsonl"
if not os.path.exists(transcript_path):
    print("Transcript not found")
    exit(1)

user_inputs = []
with open(transcript_path, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        try:
            step = json.loads(line)
            if step.get("type") == "USER_INPUT":
                user_inputs.append(step)
        except:
            pass

print(f"Total user inputs: {len(user_inputs)}")
for idx, step in enumerate(user_inputs[-10:]):
    print(f"\n--- USER INPUT {len(user_inputs) - 10 + idx + 1} (Step {step.get('step_index')}) ---")
    print(step.get("content", ""))
