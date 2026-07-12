# Last updated: 7/12/2026, 6:23:28 PM
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        inorderList = []

        node = root

        while True:
            if node:
                st.append(node)
                node = node.left
            
            else:
                if not st: break

                node = st.pop()
                inorderList.append(node.val)
                node = node.right
            

        return inorderList



                
                


        