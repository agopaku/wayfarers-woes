import os
import json
import re

transcript_path = "/Users/anilgopakumar/.gemini/antigravity/brain/1517de7a-87b6-4ba5-b261-bb6e77038596/.system_generated/logs/transcript.jsonl"
recovered_file = "/Users/anilgopakumar/Documents/Antigravity Projects/Travelogue Blog/scratch/recovered_all_approvals.json"

if not os.path.exists(transcript_path):
    print(f"Error: Transcript not found at {transcript_path}")
    exit(1)

all_approved = {}

def clean_escaped_string(s):
    # Replace any sequence of backslashes followed by a double quote with just a double quote
    s = re.sub(r'\\+"', '"', s)
    s = s.replace('\\n', '\n').replace('\\t', '\t')
    return s

def extract_candidates_from_text(text):
    text_clean = clean_escaped_string(text)
    
    # We find all occurrences of CAND_XXX
    # A candidate object typically looks like:
    # "cand_id": "CAND_002", "title": "...", "description": "...", "location": "...", "category": "..."
    # We can split the text by "cand_id" or cand_id matches
    cand_indices = [m.start() for m in re.finditer(r'CAND_\d+', text_clean)]
    
    for i, idx in enumerate(cand_indices):
        # Extract a chunk from this candidate up to the next candidate to avoid bleeding fields
        end_idx = cand_indices[i+1] if i+1 < len(cand_indices) else idx + 1000
        end_idx = min(end_idx, idx + 1000)
        chunk = text_clean[idx:end_idx]
        
        cand_id_match = re.search(r'CAND_\d+', chunk)
        if not cand_id_match:
            continue
        cand_id = cand_id_match.group(0)
        
        # Regex to find title, description, location, category, filename
        # Since the values can contain quotes, we match non-quote characters or escaped quotes
        title_match = re.search(r'"title"\s*:\s*"((?:[^"\\]|\\.)*)"', chunk)
        desc_match = re.search(r'"description"\s*:\s*"((?:[^"\\]|\\.)*)"', chunk)
        loc_match = re.search(r'"location"\s*:\s*"((?:[^"\\]|\\.)*)"', chunk)
        cat_match = re.search(r'"category"\s*:\s*"((?:[^"\\]|\\.)*)"', chunk)
        file_match = re.search(r'"filename"\s*:\s*"((?:[^"\\]|\\.)*)"', chunk)
        
        title = title_match.group(1).replace('\n', ' ').strip() if title_match else None
        desc = desc_match.group(1).replace('\n', ' ').strip() if desc_match else None
        loc = loc_match.group(1).replace('\n', ' ').strip() if loc_match else None
        cat = cat_match.group(1).strip() if cat_match else "landscape"
        fname = file_match.group(1).strip() if file_match else None
        
        # If we found at least a title or description, save it
        if title or desc or loc:
            if cand_id not in all_approved or (not all_approved[cand_id].get('title') and title):
                all_approved[cand_id] = {
                    "cand_id": cand_id,
                    "title": title,
                    "description": desc,
                    "location": loc,
                    "category": cat
                }
                if fname:
                    all_approved[cand_id]["filename"] = fname

with open(transcript_path, 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        # Check both tool calls and raw text in USER_INPUT or PLANNER_RESPONSE
        if 'CAND_' in line:
            extract_candidates_from_text(line)

print(f"Total recovered approved candidates from logs: {len(all_approved)}")
for cid in sorted(all_approved.keys()):
    item = all_approved[cid]
    print(f"{cid}: filename={item.get('filename')} | Title={item.get('title')} | Loc={item.get('location')}")

# Save them back
with open(recovered_file, "w") as out:
    json.dump(list(all_approved.values()), out, indent=2)
print(f"Wrote all recovered candidates to {recovered_file}")
