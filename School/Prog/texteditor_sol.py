# Custom DLL node. Notice the additional fields.
class Node:
    def __init__(self, data, is_endline=False, is_bold=False):
        self.data = data
        self.is_endline = is_endline
        self.is_bold = is_bold
        self.prev = None
        self.next = None

# DLL with the needed implementation. It looks very similar to the DLL seen in class but it has a 
# particular additional adding method.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data, is_endline=False, is_bold=False):
        if self.tail:
            return self.insert_after(self.tail, data, is_endline, is_bold)
        else:
            # List is empty, so create the first node
            new_node = Node(data, is_endline, is_bold)
            self.head = self.tail = new_node
            self.size += 1
            return new_node

    def insert_after(self, node, data, is_endline=False, is_bold=False):
        new_node = Node(data, is_endline, is_bold)
        new_node.prev = node
        new_node.next = node.next

        if node.next:
            node.next.prev = new_node
        else:
            self.tail = new_node

        node.next = new_node
        self.size += 1
        return new_node

    def remove_node(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        self.size -= 1
        return node

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next


class TextEditor:
    def __init__(self):
        """
        Initializes the TextEditor with an empty doubly linked list for words,
        sets the cursor to the start, and initializes statistics.
        """
        self.words_list = DoublyLinkedList()
        self.cursor_line = 1
        self.cursor_word = 0
        self.cursor_node = None  # Points to the node after the cursor
        self.commands_number = 0

    
    def process_file(self, filename):
        """
        Reads a file line by line, processing commands (lines starting with ##)
        and adding words or endlines to the editor.
        """
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                    
                if line.startswith('##'):
                    self._process_command(line)
                    self.commands_number += 1
                else:
                    self._add_word(line)
    

    def process_file_animated(self, filename):
        """
        Reads a file line by line, processing commands (lines starting with ##)
        and adding words or endlines to the editor.
        After each line/command, prints the current state of the text.
        """
        import time
        import os

        with open(filename, "r") as file:
            for line in file:
                os.system("cls" if os.name == "nt" else "clear")  # Clear console

                line = line.strip()
                if not line:
                    continue

                if line.startswith("##"):
                    self._process_command(line)
                    self.commands_number += 1
                    print(f"\nAfter running command: {line}")
                else:
                    self._add_word(line)
                    print(f"\nAfter adding word: {line}")

                self.print_formatted_text()
                #time.sleep(0.1)  # Pause for half a second to visualize changes
                input("press enter to process next line...")

    def _insert_at_cursor(self, data, is_endline=False):
        """
        Inserts a word or endline at the current cursor position.
        Updates the cursor to be after the inserted node.
        """
        if self.cursor_node is None:
            # Insert at end
            new_node = self.words_list.append(data, is_endline=is_endline)
            self.cursor_node = None  # Cursor stays after the new end
        else:
            # Insert before cursor_node
            if self.cursor_node.prev:
                new_node = self.words_list.insert_after(
                    self.cursor_node.prev, data, is_endline=is_endline
                )
            else:
                # Insert at head
                new_node = Node(data, is_endline=is_endline)
                new_node.next = self.words_list.head
                if self.words_list.head:
                    self.words_list.head.prev = new_node
                self.words_list.head = new_node
                if self.words_list.tail is None:
                    self.words_list.tail = new_node
                self.words_list.size += 1
            self.cursor_node = new_node.next  # Move cursor after the inserted node

        # Update stats and logical cursor position
        if is_endline:
            self.cursor_line += 1
            self.cursor_word = 0
        else:
            self.cursor_word += 1

    def _add_word(self, word):
        """
        Adds a word at the current cursor position.
        """
        self._insert_at_cursor(word, is_endline=False)

    def _add_endline(self):
        """
        Adds an endline marker at the current cursor position.
        """
        self._insert_at_cursor(None, is_endline=True)

    def _process_command(self, command):
        """
        Parses and executes a command (e.g., ##ENDLINE, ##MOVE, ##REMOVE, etc.).
        """
        arguments = command.split()
        cmd = arguments[0]

        if cmd == "##ENDLINE":
            self._add_endline()
        elif cmd == "##MOVE":
            line = int(arguments[1])
            word = int(arguments[2])
            self._move_cursor(line, word)
        elif cmd == "##REMOVE":
            n = int(arguments[1])
            self._remove_words(n)
        elif cmd == "##SORTL":
            line = int(arguments[1])
            self._sort_line(line)
        elif cmd == "##MOVESTART":
            self._move_start()
        elif cmd == "##MOVEEND":
            self._move_end()
        elif cmd == "##REPLACE":
            word1 = arguments[1]
            word2 = arguments[2]
            self._replace_words(word1, word2)
        elif cmd == "##BOLD":
            line = int(arguments[1])
            word = int(arguments[2])
            self._bold_word(line, word)

    def _move_cursor(self, line, word):
        """
        Moves the cursor to the specified line and word position.
        Updates self.cursor_node, self.cursor_line, and self.cursor_word.
        """
        current_line = 1
        current_word = 0
        node = self.words_list.head
        while node:
            if node.is_endline:
                if current_line == line and word == 0:
                    self.cursor_node = node
                    self.cursor_line = line
                    self.cursor_word = word
                    return
                current_line += 1
                current_word = 0
            else:
                current_word += 1
                if current_line == line and current_word == word:
                    self.cursor_node = node
                    self.cursor_line = line
                    self.cursor_word = word
                    return
            node = node.next
        # If not found, cursor is at end
        self.cursor_node = None
        self.cursor_line = line
        self.cursor_word = word

    def _remove_words(self, n):
        """
        Removes n words or endlines starting from the cursor position.
        Updates statistics accordingly.
        """
        current_line = 1
        current_word = 0
        start_node = None

        # Find the node at cursor position
        for node in self.words_list:
            if node.is_endline:
                if current_line == self.cursor_line and self.cursor_word == 0:
                    start_node = node
                    break
                current_line += 1
                current_word = 0
            else:
                current_word += 1
                if (
                    current_line == self.cursor_line
                    and current_word == self.cursor_word
                ):
                    start_node = node
                    break

        if not start_node:
            return  # Nothing to remove

        # Remove n nodes starting from start_node
        nodes_to_remove = []
        current = start_node
        for _ in range(n):
            if not current:
                break
            nodes_to_remove.append(current)
            current = current.next

        for node in nodes_to_remove:
            self.words_list.remove_node(node)

    def _sort_line(self, line, method="quicksort"):
        """
        Sorts the words in the specified line using the given method (quicksort or mergesort).
        """
        current_line = 1
        line_nodes = []
        line_start = None
        line_end = None

        for node in self.words_list:
            if node.is_endline:
                if current_line == line:
                    line_end = node
                    break
                current_line += 1
            elif current_line == line:
                if not line_start:
                    line_start = node
                line_nodes.append(node)

        if not line_nodes:
            return  # Empty line

        # Extract words and bold flags
        words = [(node.data, node.is_bold) for node in line_nodes]

        # Sort using the selected method
        if method == "quicksort":
            self._quicksort(words, 0, len(words) - 1)
        elif method == "mergesort":
            words = self._mergesort(words)
        else:
            raise ValueError("Unknown sort method")

        # Rebuild the line with sorted words
        current = line_start
        for i, (word, is_bold) in enumerate(words):
            current.data = word
            current.is_bold = is_bold
            if i < len(line_nodes) - 1:
                current = current.next

    def _quicksort(self, arr, low, high):
        """
        In-place quicksort for sorting a list of (word, is_bold) tuples by word (case-insensitive).
        """
        if low < high:
            pi = self._partition(arr, low, high)
            self._quicksort(arr, low, pi - 1)
            self._quicksort(arr, pi + 1, high)

    def _partition(self, arr, low, high):
        """
        Partition helper for quicksort.
        """
        pivot = arr[high][0].lower()
        i = low - 1
        for j in range(low, high):
            if arr[j][0].lower() <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def _mergesort(self, arr):
        """
        Mergesort for sorting a list of (word, is_bold) tuples by word (case-insensitive).
        Mainly the word part is considered. The flag is carried out.
        """
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self._mergesort(arr[:mid])
        right = self._mergesort(arr[mid:])
        return self._merge(left, right)

    def _merge(self, left, right):
        """
        Merge helper for mergesort. As seen in class.
        """
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i][0].lower() <= right[j][0].lower():
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def _move_start(self):
        """
        Moves the cursor to the start of the list (right after the first word).
        """
        self.cursor_line = 1
        self.cursor_word = 1
        self.cursor_node = self.words_list.head
        # If the list is empty, cursor_node stays None

    def _move_end(self):
        """
        Moves the cursor to the end of the list.
        If the last node is an ENDLINE, the cursor is at the start of a new line.
        Otherwise, the cursor is after the last word of the last line.
        """
        node = self.words_list.tail
        if node is None:
            # Empty list
            self.cursor_node = None
            self.cursor_line = 1
            self.cursor_word = 0
            return

        # Count lines and words up to the end
        line = 1
        word = 0
        current = self.words_list.head
        last_endline = None
        while current:
            if current.is_endline:
                line += 1
                word = 0
                last_endline = current
            else:
                word += 1
            current = current.next

        if self.words_list.tail.is_endline:
            # Last node is ENDLINE: cursor is after it (new line, word 0)
            self.cursor_node = None
            self.cursor_line = line
            self.cursor_word = 0
        else:
            # Last node is a word: cursor is after it (same line, word+1)
            self.cursor_node = None
            self.cursor_line = line
            self.cursor_word = word

    def _replace_words(self, word1, word2):
        """
        Replaces all occurrences of word1 with word2 in the current line.
        """
        current_line = 1
        line_nodes = []

        for node in self.words_list:
            if node.is_endline:
                if current_line == self.cursor_line:
                    break
                current_line += 1
            elif current_line == self.cursor_line:
                line_nodes.append(node)

        for node in line_nodes:
            if node.data == word1:
                node.data = word2

    def _bold_word(self, line, word):
        """
        Sets the is_bold flag to True for the specified word in the given line. 
        Remember to check if the node is a normal word.
        """
        current_line = 1
        current_word = 0

        for node in self.words_list:
            if node.is_endline:
                current_line += 1
                current_word = 0
            else:
                current_word += 1
                if current_line == line and current_word == word:
                    node.is_bold = True
                    break

    def print_formatted_text(self):
        """
        Prints the text with line numbers and bold formatting for bold words.
        """
        line_number = 1
        first_word_in_line = True
        for node in self.words_list:
            if node.is_endline:
                print()
                line_number += 1
                first_word_in_line = True
            else:
                if first_word_in_line:
                    print(f"{line_number:03d}", end=" ")
                    first_word_in_line = False
                if node.is_bold:
                    print(f"*{node.data}*", end=" ")
                else:
                    print(node.data, end=" ")
        print()

    def print_stats(self):
        """
        Prints statistics: number of words, lines, and commands processed.
        Only one statistic needs to be kept while updating. The rest can be 
        recomputed.
        """
        lines = 0
        words = 0
        for node in self.words_list:
            if node.is_endline:
                lines += 1
            else:
                words += 1

        # If the text doesn't end with an endline, count the last line
        if self.words_list.tail and not self.words_list.tail.is_endline:
            lines += 1

        print(f"Words: {words}")
        print(f"Lines: {lines}")
        print(f"Commands processed: {self.commands_number}")


# Test the implementation
if __name__ == "__main__":
    # Read a test file
    test_filename = "test_input.txt"
    #create_test_file(test_filename) # this function was used to generate the example input file, it does not exist in the solution and is not needed anymore.

    # Process the test file
    editor = TextEditor()
    #editor.process_file(test_filename) # use this call to show the final result after all the lines are processed.
    editor.process_file_animated(test_filename) # use this call to process line by line and display the updated list.

    # Print results
    print("Final formatted Text:")
    editor.print_formatted_text()
    print("\nStatistics:")
    editor.print_stats()
