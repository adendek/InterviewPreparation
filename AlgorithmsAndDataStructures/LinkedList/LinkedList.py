class LinkedListError(Exception):
    def __init__(self, msg):
        self.msg = msg

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "value " + str(self.value) + " next " + str(self.next)


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, value):
        if isinstance(value, list):
            for element in value:
                self._insert_single_element(element)
        else:
            self._insert_single_element(value)

    def length_recursive(self):
        return self._calculate_length(self.head, 0)

    def _calculate_length(self, node, actual_size):
        if node is None:
            return actual_size
        return self._calculate_length(node.next, actual_size+1)

    def _insert_single_element(self, value):
        if self.head is None:
            self.head = Node(value)
            self.size = 1
            return

        list_iterator = self.head
        while list_iterator.next is not None:
            list_iterator = list_iterator.next

        if isinstance(value, Node):
            list_iterator.next = value
        else:
            list_iterator.next = Node(value)
        self.size += 1

    def __str__(self):
        output = ""
        list_iterator = self.head
        while list_iterator is not None:
            output += str(list_iterator.value) + "->"
            list_iterator = list_iterator.next
        output += "None"
        return output

    def sum(self, other):
        def f_sum(a,b):
            return a+b
        return self._calculate_sum(self.head, other.head, f_sum, 0)

    def dot(self, other):
        return self._calculate_sum(self.head, other.head, lambda x,y: x*y, 0)

    def _calculate_sum(self, first, second, f, accumulator):
        if first is None:
            return accumulator
        accumulator += f(first.value, second.value)
        return self._calculate_sum(first.next, second.next, f, accumulator)

    def find_k_element_from_end(self, k):
        if k > self.size:
            raise LinkedListError("K is bigger than the list size, cannot process")
        elif k == self.size:
            return self.head.value

        shifted_iterator = self._move_iterator_k_times(k)
        return self._find_k_element(shifted_iterator)

    def _move_iterator_k_times(self, k):
        out_iterator = self.head
        for _ in range(k):
            out_iterator = out_iterator.next
        return out_iterator

    def _find_k_element(self, shifted_iterator):
        delayed_iterator = self.head
        while shifted_iterator is not None:
            shifted_iterator = shifted_iterator.next
            delayed_iterator = delayed_iterator.next
        return delayed_iterator.value

    def reverse(self):
        self._do_reverse(None, self.head)

    def _do_reverse(self, previous, element):
        if element is None:
            return element

        tmp = element.next
        element.next = previous
        self.head = element
        self._do_reverse(element, tmp)

    def merge_sorted(self, other):
        merged = LinkedList()
        first_iter = self.head
        second_iter = other.head
        while (first_iter is not None) or (second_iter is not None):
            if first_iter is None:
                second_iter = self._append_and_move_iterator(merged, second_iter)
            elif second_iter is None:
                first_iter = self._append_and_move_iterator(merged, first_iter)
            elif first_iter.value < second_iter.value:
                first_iter = self._append_and_move_iterator(merged, first_iter)
            else:
                second_iter = self._append_and_move_iterator(merged, second_iter)
        return merged

    def _append_and_move_iterator(self, merged, iterator):
        merged.insert(iterator.value)
        iterator = iterator.next
        return iterator

    def contains_cycles(self):
        if self.size < 2 :
            return False

        fast_iter = self.head
        slow_iter = self.head

        while fast_iter is not None:
            fast_iter = fast_iter.next.next
            slow_iter = slow_iter.next
            if fast_iter is slow_iter:
                return True, slow_iter
        return False

    def middle_elemet(self):
        if self.size == 1:
            return
        fast_iter = self.head
        slow_iter = self.head
        while fast_iter is not None:
            fast_iter = fast_iter.next.next
            slow_iter = slow_iter.next
        return slow_iter

    def print_reversed(self):
        return self._do_print_reversed(self.head)

    def _do_print_reversed(self, node):
        if node is None:
            return
        self._do_print_reversed(node.next)
        print(node.value)



if __name__ == "__main__":
    """

    elements_to_insert = [1, 2, 3, 45, 56, 6, 7]
    linked_list = LinkedList()
    for element in elements_to_insert:
        linked_list.insert(element)

    print(linked_list)
    print(linked_list.find_k_element_from_end(3))
    linked_list.reverse()
    print(linked_list)
        """


    odd_list = LinkedList()
    odd_list.insert(list(range(0, 10, 2)))
    even_list = LinkedList()
    even_list.insert(list(range(1,10,2)))
    print(odd_list)
    print(even_list)


    merged = even_list.merge_sorted(odd_list)
    merged = merged.merge_sorted(LinkedList())
    print(merged)
    print(merged.length_recursive() == merged.size )

    print(even_list.sum(odd_list)==sum(range(10)))
    print(even_list.dot(odd_list))

    print("Cycle  " +str(merged.contains_cycles()))

    cycle_beginning_node = Node(12)

    cycled_Linked_List = LinkedList()
    cycled_Linked_List.insert([1,2,3,4,5,6])
    cycled_Linked_List.insert(cycle_beginning_node)
    cycled_Linked_List.insert([20,21,22,23,24,25,26,27])
    cycled_Linked_List.insert(cycle_beginning_node)

    result =  cycled_Linked_List.contains_cycles()
    print("Cycle  " +str(result[0]) + str(result[1].value))


    print(merged)
    print(merged.middle_elemet())
    print(merged.print_reversed())
