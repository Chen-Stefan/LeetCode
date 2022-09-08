# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # 这样就不需要再初始化一个list了，直接确保了每个value都是一个list
        column_table = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        min_column = max_column = 0
        while queue:
            node, column = queue.popleft()
            # 为什么要check node存在? 因为有些node没有左右孩子
            if node:
                min_column = min(min_column, column)
                max_column = max(max_column, column)
                
                column_table[column].append(node.val)
                
                #把左右孩子以及对应的column放进queue中
                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))
        # dict comprehension YYDS
        return [column_table[x] for x in range(min_column, max_column + 1)]