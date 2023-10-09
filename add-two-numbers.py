try:
    from typing import Optional
except:
    pass
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0  # Inicializamos el acarreo como 0
        dummy_head = ListNode()
        current = dummy_head  # Inicializamos el nodo actual en el nodo dummy

        while l1 or l2 or carry:
            # Obtenemos los valores de los nodos l1 y l2, si existen
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculamos la suma de los valores y el acarreo
            total_sum = val1 + val2 + carry
            carry = total_sum // 10  # El acarreo será 0 o 1
            print(f"\n{val1}+{val2}= {val1+val2};")
            print("carry:",carry)
            # Creamos un nuevo nodo con el valor actual y lo agregamos a la lista
            current.next = ListNode(total_sum % 10)
            
            # Movemos los punteros si los nodos l1 y l2 existen
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
            # Movemos el puntero actual
            current = current.next

        return dummy_head.next  # El resultado empieza desde el siguiente del nodo dummy

import unittest

class TestSolution(unittest.TestCase):
    def create_linked_list(self, nums):
        # Función auxiliar para crear una lista enlazada desde una lista de números
        dummy_head = ListNode()
        current = dummy_head
        for num in nums:
            current.next = ListNode(num)
            current = current.next
        return dummy_head.next

    def linked_list_to_list(self, head):
        # Función auxiliar para convertir una lista enlazada en una lista de números
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    def test_case_1(self):
        sol = Solution()
        l1 = self.create_linked_list([2, 4, 3])
        l2 = self.create_linked_list([5, 6, 4])
        expected = [7, 0, 8]
        result = sol.addTwoNumbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(result), expected)

    # def test_case_2(self):
    #     sol = Solution()
    #     l1 = self.create_linked_list([9, 9, 9, 9, 9])
    #     l2 = self.create_linked_list([9, 9, 9])
    #     expected = [8, 9, 9, 0, 0, 1]
    #     result = sol.addTwoNumbers(l1, l2)
    #     self.assertEqual(self.linked_list_to_list(result), expected)

    # def test_case_3(self):
    #     sol = Solution()
    #     l1 = self.create_linked_list([0])
    #     l2 = self.create_linked_list([0])
    #     expected = [0]
    #     result = sol.addTwoNumbers(l1, l2)
    #     self.assertEqual(self.linked_list_to_list(result), expected)

if __name__ == '__main__':
    unittest.main()
