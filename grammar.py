import random

rules = {'S': ['NP VP'], 'NP': ['Det N'], 'VP': ['V NP'], 'Det': ['the', 'a'], 'N': ['dog', 'cat', 'bird'],
         'V': ['chased', 'ate', 'sang']}


class Tree:

    def __init__(self, rule):
        self.rule = rule
        self.nodes = []

    def add_node(self, rule) -> None:
        self.nodes.append(Tree(rule))


def build_tree(node) -> None:
    rule = node.rule
    # checks if node's rule is in rules
    if rule in rules:
        for child in rules.get(rule):
            node.add_node(child)
    # checks if node's rule is concatenated
    elif ' ' in rule:
        for child in rule.split(' '):
            node.add_node(child)
    for child in node.nodes:
        # recursive step build_tree for each child
        build_tree(child)


# should never be called outside of random_generator_tree,
# fills ls with terminal values
def _generate(node, ls) -> None | bool:
    # checks if node is not terminal
    if len(node.nodes) > 0:
        for child in node.nodes:
            # recursive step to choose a terminal element
            if _generate(child, ls):
                # selects random child node
                ls.append(random.choice(node.nodes).rule)
                break
    else:
        return True


# calls _generate and returns generated sentence as a string
def random_generator_tree(node) -> str:
    sentence_ls = []
    _generate(node, sentence_ls)
    # formats list as string
    return ' '.join(sentence_ls).capitalize()+'.'


# generates a correct sentence from a context-free grammar
def random_generator_stack() -> str:
    terminal = []
    non_terminal = ['S']
    while len(non_terminal) > 0:
        val = rules.get(non_terminal.pop())
        # random element from val
        temp = random.choice(val)
        if ' ' in temp:
            non_terminal.extend(temp.split(' '))
        else:
            terminal.append(temp)
    # formats reversed list as string
    return ' '.join(terminal[::-1]).capitalize()+'.'


rule_tree = Tree('S')
build_tree(rule_tree)


print('\nRandomly generated sentences with a tree:')
for i in range(5):
    print(random_generator_tree(rule_tree))


print('\nRandomly generated sentences with a stack:')
for i in range(5):
    print(random_generator_stack())
