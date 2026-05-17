import time
import sys
import random
import string
from greedy.dijkstra import dijkstra
from greedy.huffman import huffman_coding
from divide_and_conquer.merge_sort import merge_sort
from divide_and_conquer.quick_sort import quick_sort

def measure_performance(func, *args, **kwargs):
    """
    Measures execution time and approximates space usage.
    Note: Space usage is difficult to measure precisely in Python. 
    We record the size of the primary input object as a baseline.
    """
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    
    # sys.getsizeof provides the size of the object itself in bytes.
    # For a list or dict, it includes the overhead of the container.
    space_usage = sys.getsizeof(args[0]) if args else 0
    
    return execution_time, space_usage

def generate_graph(num_nodes, num_edges):
    graph = {str(i): {} for i in range(num_nodes)}
    for _ in range(num_edges):
        u = str(random.randint(0, num_nodes - 1))
        v = str(random.randint(0, num_nodes - 1))
        if u != v:
            weight = random.randint(1, 100)
            graph[u][v] = weight
    return graph

def run_tests():
    sizes = {
        "Small": 100,
        "Medium": 1000,
        "Large": 5000
    }
    
    results = {}

    for size_name, size in sizes.items():
        print(f"Running tests for {size_name} input (size {size})...")
        results[size_name] = {}
        
        # Dijkstra's Algorithm
        graph = generate_graph(size, size * 2)
        exec_time, space = measure_performance(dijkstra, graph, '0')
        results[size_name]["Dijkstra"] = {"time": exec_time, "space": space}
        
        # Huffman Coding
        data = ''.join(random.choices(string.ascii_letters + string.digits, k=size))
        exec_time, space = measure_performance(huffman_coding, data)
        results[size_name]["Huffman"] = {"time": exec_time, "space": space}
        
        # Merge Sort
        arr = [random.randint(0, 100000) for _ in range(size)]
        exec_time, space = measure_performance(merge_sort, arr)
        results[size_name]["Merge Sort"] = {"time": exec_time, "space": space}
        
        # Quick Sort
        arr = [random.randint(0, 100000) for _ in range(size)]
        exec_time, space = measure_performance(quick_sort, arr)
        results[size_name]["Quick Sort"] = {"time": exec_time, "space": space}

    return results

def format_results(results):
    md_output = "# Performance Analysis Results\n\n"
    md_output += "> **Note on Space Usage:** The values below represent the approximate size of the input data structure in memory (in bytes). While they do not capture the auxiliary peak memory usage of each algorithm, they provide a relative scale of the data being processed.\n\n"
    
    for size_name, algos in results.items():
        md_output += f"## {size_name} Input\n\n"
        md_output += "| Algorithm | Execution Time (s) | Input Space (approx. bytes) |\n"
        md_output += "|-----------|-------------------|----------------------------|\n"
        for algo_name, metrics in algos.items():
            md_output += f"| {algo_name} | {metrics['time']:.6f} | {metrics['space']} |\n"
        md_output += "\n"
        
    return md_output

if __name__ == "__main__":
    results = run_tests()
    formatted_results = format_results(results)
    print(formatted_results)
    with open("analysis/results.md", "w") as f:
        f.write(formatted_results)
