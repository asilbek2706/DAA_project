import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define comparison operators for heapq to handle Node objects
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_coding(data):
    """
    Huffman Coding algorithm for data compression.
    
    Args:
    data: The string of characters to encode.
    
    Returns:
    A dictionary of character-to-Huffman-code mappings.
    """
    if not data:
        return {}

    # Calculate frequency of each character
    frequency = Counter(data)
    
    # Create a priority queue of nodes
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)
    
    # Build the Huffman tree
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        
        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        
        heapq.heappush(heap, merged)
        
    # Generate Huffman codes from the tree
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
    
    # Special case for a single character
    if len(frequency) == 1:
        char = list(frequency.keys())[0]
        codes[char] = "0"

    return codes

if __name__ == "__main__":
    # Example usage
    data = "huffman coding example"
    codes = huffman_coding(data)
    print("Huffman Codes:", codes)
    encoded_data = "".join(codes[char] for char in data)
    print("Encoded Data:", encoded_data)
