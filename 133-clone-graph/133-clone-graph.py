"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        # 1.找到所有点
        nodes = self.find_nodes_by_bfs(node)
        # 2.复制所有点
        mapping = self.copy_nodes(nodes)
        # 3. 复制所有边
        self.copy_edges(mapping)
        
        # 4. 返回复制出来的初始节点
        
        return mapping[node]
    
    def find_nodes_by_bfs(self, node):
        queue = collections.deque([node])
        # 这里有于没有最短路径问题，不需要存储distance, 所以用set就可以
        visited = set([node])
        while queue:
            cur_node = queue.popleft()
            for neighbor in cur_node.neighbors:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)
        return visited
    
    def copy_nodes(self, nodes):
        mapping = {}
        for node in nodes:
            mapping[node] = Node(node.val)
        
        return mapping
    
    def copy_edges(self, mapping):
        for node in mapping.keys():
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)