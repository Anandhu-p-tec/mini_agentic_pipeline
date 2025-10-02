import os
from datetime import datetime
from src.controller import Controller

# Ensure logs folder exists
os.makedirs("logs", exist_ok=True)

# Initialize agent
agent = Controller()

# Load demo queries
with open("demo_queries.txt", "r") as f:
    queries = [line.strip() for line in f if line.strip()]

# Prepare a log file for this run
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file_path = f"logs/run_{timestamp}.json"

results = []

# Run all queries automatically
for query in queries:
    print("\n==============================")
    print(f"Q: {query}")
    answer = agent.handle_query(query)
    print(f"A: {answer}")

    # Save only query and answer
    results.append({
        "query": query,
        "answer": answer
    })

# Write logs to JSON
import json
with open(log_file_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print(f"\nAll queries executed. Logs saved to {log_file_path}")
