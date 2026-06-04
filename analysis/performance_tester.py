import time
import sys
import random
import string
import heapq
from collections import Counter


# =====================================================================
# 1. GREEDY ALGORITHMS (Ochko'z algoritmlar)
# =====================================================================

def dijkstra(graph, start):
    """Dijkstra algoritmi - Eng qisqa masofani topish"""
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def huffman_coding(data):
    """Xaffmen algoritmi - Ma'lumotlarni siqish kodi"""
    if not data:
        return {}

    frequency = Counter(data)
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, merged)

    root = heap[0]
    codes = {}

    def generate_codes(node, current_code):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = current_code
            return
        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")

    generate_codes(root, "")

    if len(frequency) == 1:
        char = list(frequency.keys())[0]
        codes[char] = "0"

    return codes


# =====================================================================
# 2. DIVIDE AND CONQUER ALGORITHMS (Bo'lib tashla va hukmronlik qil)
# =====================================================================

def merge_sort(arr):
    """Merge Sort (Birlashtirish orqali saralash)"""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)


def _merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    """Quick Sort (Tezkor saralash)"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# =====================================================================
# 3. PERFORMANCE MEASUREMENT & TEST RUNNER
# =====================================================================

def measure_performance(func, *args, **kwargs):
    """Algoritmning ishlash vaqti va xotira hajmini o'lchash"""
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    execution_time = end_time - start_time

    space_usage = sys.getsizeof(args[0]) if args else 0
    return execution_time, space_usage


def generate_graph(num_nodes, num_edges):
    """Dijkstra uchun tasodifiy xavfsiz graf yaratish"""
    graph = {str(i): {} for i in range(num_nodes)}
    for _ in range(num_edges):
        u = str(random.randint(0, num_nodes - 1))
        v = str(random.randint(0, num_nodes - 1))
        if u != v:
            weight = random.randint(1, 100)
            graph[u][v] = weight
    return graph


def run_tests():
    """Barcha hajmdagi testlarni ishga tushirish"""
    sizes = {
        "Small": 100,
        "Medium": 1000,
        "Large": 3000  # Quick Sortda RecursionError bermasligi uchun 3000 qilindi
    }

    results = {}

    for size_name, size in sizes.items():
        print(f"Running tests for {size_name} input (size {size})...")
        results[size_name] = {}

        # 1. Dijkstra Test
        graph = generate_graph(size, size * 2)
        exec_time, space = measure_performance(dijkstra, graph, '0')
        results[size_name]["Dijkstra"] = {"time": exec_time, "space": space}

        # 2. Huffman Test
        data = ''.join(random.choices(string.ascii_letters + string.digits, k=size))
        exec_time, space = measure_performance(huffman_coding, data)
        results[size_name]["Huffman"] = {"time": exec_time, "space": space}

        # 3. Merge Sort Test
        arr_merge = [random.randint(0, 100000) for _ in range(size)]
        exec_time, space = measure_performance(merge_sort, arr_merge)
        results[size_name]["Merge Sort"] = {"time": exec_time, "space": space}

        # 4. Quick Sort Test
        arr_quick = [random.randint(0, 100000) for _ in range(size)]
        exec_time, space = measure_performance(quick_sort, arr_quick)
        results[size_name]["Quick Sort"] = {"time": exec_time, "space": space}

    return results


def format_results(results):
    """Natijalarni Markdown jadval ko'rinishiga keltirish"""
    md_output = "# Performance Analysis Results\n\n"
    md_output += "> **Note on Space Usage:** The values below represent the approximate size of the input data structure.\n\n"

    for size_name, algos in results.items():
        md_output += f"## {size_name} Input\n\n"
        md_output += "| Algorithm | Execution Time (s) | Input Space (approx. bytes) |\n"
        md_output += "|-----------|-------------------|----------------------------|\n"
        for algo_name, metrics in algos.items():
            md_output += f"| {algo_name} | {metrics['time']:.6f} | {metrics['space']} |\n"
        md_output += "\n"

    return md_output


if __name__ == "__main__":
    # Testlarni ishga tushirish
    results = run_tests()
    formatted_results = format_results(results)

    # Natijani konsolga chiqarish
    print("\n" + formatted_results)

    # Natijani faylga yozish
    try:
        import os

        os.makedirs("analysis", exist_ok=True)
        with open("analysis/results.md", "w") as f:
            f.write(formatted_results)
        print("Natijalar 'analysis/results.md' fayliga muvaffaqiyatli yozildi.")
    except Exception as e:
        print(f"Faylga yozishda xatolik: {e}")