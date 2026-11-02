


# ================= Pattern 4: Dictionary with Adjacency List for Graphs / Searching AI ==========
# ================= (A Search / BFS / DFS ke liye graph representation)* =========================


# 1. DATA STRUCTURE (Graph: Node -> List of Neighbor Dictionaries with Costs)
graph = {
    "A": [{"node": "B", "cost": 4}, {"node": "C", "cost": 2}],
    "B": [{"node": "D", "cost": 5}],
    "C": [{"node": "B", "cost": 1}, {"node": "D", "cost": 8}],
    "D": []
}


# 2. ACTION & LOOP: Neighbors traverse karke 3 se kam cost waale paths find karna
print("--- CHEAP ROUTES (Cost < 3) ---")
for start_node, neighbors in graph.items():
    for neighbor_info in neighbors:
        target = neighbor_info["node"]
        edge_cost = neighbor_info["cost"]
        
        if edge_cost < 3:
            print(f"Path: {start_node} -> {target} with Cost: {edge_cost}")