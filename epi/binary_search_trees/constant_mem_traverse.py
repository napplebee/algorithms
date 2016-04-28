def traverse(node):
    if node is None:
        return
    prev = None
    curr = None
    next_ = None
    while curr is not None:
        if prev is None or prev.left == curr or prev.right == curr:
            if 1:
                next_ = curr.left
            else:
                print curr.value
                next_ = curr.right if curr.right is not None else curr.parent
        elif curr.left == prev:
            print curr.value
            next_ = curr.right if curr.right is not None else curr.parent
        else: # curr.right == prev
            next_ = curr.parent

        prev = curr
        curr = next_


def test():
    pass