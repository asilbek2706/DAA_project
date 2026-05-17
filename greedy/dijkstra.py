import heapq

def dijkstra(graph, start):
    """
    Dijkstra's Algorithm to find the shortest path from a start node to all other nodes in a weighted graph.
    
    Args:
    graph: A dictionary where keys are nodes and values are lists of (neighbor, weight) tuples.
    start: The starting node.
    
    Returns:
    A dictionary of shortest distances from the start node to each node.
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If the current distance is greater than the already found shortest distance, skip it.
        if current_distance > distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # If a shorter path to the neighbor is found, update it.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

if __name__ == "__main__":
    # Example usage
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    print("Dijkstra's distances from A:", dijkstra(graph, 'A'))
