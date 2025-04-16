# === PART 0: Stack implementation with linked list ===
from LinkedList import ListNode, LinkedList

class Node:
    """A node in a singly linked list."""

    def __init__(self, value, link):
        self.value = value
        self.next = link


class LinkedStack:


    def __init__(self):
        self._top = None
        self.len = 0


    def is_empty(self):
        if self._top is None:
            return "The list is empty"
        else:
            return "The list aint empty"

    def push(self, item):
            self._top.next = self._top
            self._top = Node(item, self._top)
            self.len += 1

    def pop(self):
        if self._top is not None:
            node = self._top
            self._top = self._top.next
            self.len -= 1
            return node.value

    def peek(self):
        if self._top is not None:
            node = self._top
            return node.item



# === PART 1: Balanced Parentheses Checker ===

def is_balanced(expr):
    """
    Check if all types of parentheses are balanced.
    Valid brackets: (), [], {}
    """
    




# === PART 3: Evaluate Postfix Expression ===

def evaluate_postfix(expr):
    """
    Evaluate a postfix expression.
    Example: "3 4 +" => 7
    """
    # TODO: Use stack to evaluate the postfix expression
    pass


# === PART 4: Evaluate Prefix Expression ===

def evaluate_prefix(expr):
    """
    Evaluate a prefix expression.
    Example: "+ 3 4" => 7
    """
    # TODO: Use stack to evaluate the prefix expression
    pass


# === BONUS: Convert Infix Expression ===

def precedence(op):
    """Helper function to return precedence of operators."""
    # Provided
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    return 0


def infix_to_postfix(expr):
    """
    Convert fully parenthesized infix to postfix.
    Example: "( 3 + 4 )" => "3 4 +"
    """
    # TODO: Use operator and output stacks to build postfix
    pass


def infix_to_prefix(expr):
    """
    Convert fully parenthesized infix to prefix.
    Example: "( 3 + 4 )" => "+ 3 4"
    """
    # TODO: Reverse the expression and apply infix-to-postfix logic
    pass


# === TEST CASES ===
if __name__ == "__main__":
    # Balanced parentheses tests
    assert is_balanced("()") == True, "is_balanced not correctly implemented!"
    assert is_balanced("([]{})") == True, "is_balanced not correctly implemented!"
    assert is_balanced("((a + b) * c)") == True, "is_balanced not correctly implemented!"
    assert is_balanced("({[()]})") == True, "is_balanced not correctly implemented!"
    assert is_balanced("([)]") == False, "is_balanced not correctly implemented!"
    assert is_balanced("(") == False, "is_balanced not correctly implemented!"
    assert is_balanced("}") == False, "is_balanced not correctly implemented!"
    assert is_balanced("") == True, "is_balanced not correctly implemented!"

    # Postfix evaluation tests
    assert evaluate_postfix("3 4 +") == 7, "evaluate_postfix not correctly implemented!"
    assert evaluate_postfix("10 5 /") == 2, "evaluate_postfix not correctly implemented!"
    assert evaluate_postfix("5 1 2 + 4 * + 3 -") == 14, "evaluate_postfix not correctly implemented!"
    assert evaluate_postfix("2 3 * 5 4 * + 9 -") == 17, "evaluate_postfix not correctly implemented!"

    # Prefix evaluation tests
    assert evaluate_prefix("+ 3 4") == 7, "evaluate_prefix not correctly implemented!"
    assert evaluate_prefix("/ 10 5") == 2, "evaluate_prefix not correctly implemented!"
    assert evaluate_prefix("- + * 2 3 * 5 4 9") == 17, "evaluate_prefix not correctly implemented!"
    assert evaluate_prefix("- + 5 * 1 2 3") == 4, "evaluate_prefix not correctly implemented!"

    # Infix to Postfix
    assert infix_to_postfix("( 3 + 4 )") == "3 4 +", "infix_to_postfix not correctly implemented!"
    assert infix_to_postfix("( 2 + ( 3 * 4 ) )") == "2 3 4 * +", "infix_to_postfix not correctly implemented!"
    assert infix_to_postfix("( ( 5 + 6 ) * 2 )") == "5 6 + 2 *", "infix_to_postfix not correctly implemented!"

    # Infix to Prefix
    assert infix_to_prefix("( 3 + 4 )") == "+ 3 4", "infix_to_prefix not correctly implemented!"
    assert infix_to_prefix("( 2 + ( 3 * 4 ) )") == "+ 2 * 3 4", "infix_to_prefix not correctly implemented!"
    assert infix_to_prefix("( ( 5 + 6 ) * 2 )") == "* + 5 6 2", "infix_to_prefix not correctly implemented!"

    # Evaluate converted expressions
    assert evaluate_postfix(infix_to_postfix("( 5 + ( 6 * 2 ) )")) == 17, "evaluate_postfix not correctly implemented!"
    assert evaluate_prefix(infix_to_prefix("( 5 + ( 6 * 2 ) )")) == 17, "evaluate_postfix not correctly implemented!"

    print("All tests passed!")
