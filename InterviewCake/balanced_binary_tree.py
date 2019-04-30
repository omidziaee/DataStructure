class Solution():
    def is_balanced_binary_tree(self, root_node):
        #todo: Edge CASES
        stack_to_keep_node_level = []
        stack_to_keep_node_level.append((root_node, 0))
        
        level_keep = []
        while stack_to_keep_node_level:
            node, level = stack_to_keep_node_level.pop()
            # check if we arrive to Leaf
            if not node.left or not node.right:
                if level not in level_keep:
                    