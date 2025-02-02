if __name__ == '__main__':
    from strutture.Stack import PilaArrayList
    from strutture.Queue import CodaArrayList_deque
else:
    from .strutture.Stack import PilaArrayList
    from .strutture.Queue import CodaArrayList_deque


class BinaryNode:
    def __init__(self, info):
        self.info = info #le info di un nodo posso essere anche una lista di cose. esempio: [key, value]
        self.father = None
        self.leftSon = None
        self.rightSon = None


class BinaryTree:
    def __init__(self, rootNode=None):
        self.root = rootNode

    def insertAsLeftSubTree(self, father, subtree):
        """Permette di inserire la radice di un sottoalbero come figlio sinistro
        del nodo father"""
        son = subtree.root
        if son != None:
            son.father = father
        father.leftSon = son

    def insertAsRightSubTree(self, father, subtree):
        #father=BinaryNode, nodo di self
        #subtree=BinaryTree
        """Permette di inserire la radice di un sottoalbero come figlio destro
        del nodo father"""
        son = subtree.root
        if son != None:
            son.father = father
        father.rightSon = son

    def cutLeft(self, father):
        """Permette di rimuovere l'intero sottoalbero che parte dal figlio
        sinistro del nodo father"""
        son = father.leftSon
        newTree = BinaryTree(son)
        father.leftSon = None
        return newTree

    def cutRight(self, father):
        """Permette di rimuovere l'intero sottoalbero che parte dal figlio
        destro del nodo father"""
        son = father.rightSon
        newTree = BinaryTree(son)
        father.rightSon = None
        return newTree

    def DFS(self):
        """Permette di restituire una lista di elementi ottenuta da una visita
        in profondita' dell'albero."""
        res = []
        stack = PilaArrayList()
        if self.root != None:
            stack.push(self.root)
        while not stack.isEmpty():
            current = stack.pop()
            res.append(current.info)
            if current.rightSon != None:
                stack.push(current.rightSon)
            if current.leftSon != None:
                stack.push(current.leftSon)
        return res

    def BFS(self):
        """Permette di restituire una lista di elementi ottenuta da una visita
        in ampiezza dell'albero."""
        res = []
        q = CodaArrayList_deque()
        if self.root != None:
            q.enqueue(self.root)
        while not q.isEmpty():
            current = q.dequeue()
            res.append(current.info)
            if current.leftSon != None:
                q.enqueue(current.leftSon)
            if current.rightSon != None:
                q.enqueue(current.rightSon)
        return res

    def cut(self, node):
        """Stacca e restituisce l'intero sottoalbero radicato in node. L'operazione
        cancella dall'albero il nodo node e tutti i suoi discendenti."""
        if node == None:
            return BinaryTree(None)
        if node.father == None:  # nodo radice
            self.root = None
            return BinaryTree(node)
        f = node.father
        if node.leftSon == None and node.rightSon == None:  # a leaf!
            if f.leftSon == node:
                f.leftSon = None
            else:
                f.rightSon = None
            return BinaryTree(node)
        elif f.leftSon == node:
            nt = self.cutLeft(f)
            # f.leftSon = None  --> Questa operazione viene fatta in cutLeft
            return nt
        else: #f.rightSon == node
            nt = self.cutRight(f)
            # f.rightSon = None  --> Questa operazione viene fatta in cutRight
            return nt

    def stampa(self):
        """Permette di stampare l'albero. Per farlo si usa una pila di appoggio"""
        stack = PilaArrayList()
        if self.root != None:
            stack.push([self.root, 0])  # pila di liste di due elementi [il nodo, il livello occupato dal nodo]
        else:
            print("Empty tree!")
        while not stack.isEmpty():
            current = stack.pop()
            level = current[1]
            print("|---" * level + str(current[0].info))

            if current[0].rightSon != None:
                stack.push([current[0].rightSon, level + 1])
            if current[0].leftSon != None:
                stack.push([current[0].leftSon, level + 1])

#BinaryTree e' una struttura in cui ogni nodo e' un BinaryNode o non e' niente. Quindi per definire un albero binario
#con radice diversa da none devo: tree=BinaryNode(radice) dove radice e' un BinaryNode


if __name__ == "__main__":

    radice=BinaryNode(5)
    radice.leftSon=BinaryNode(6)
    radice.rightSon=BinaryNode(7)
    tree=BinaryTree(radice)
    figlioSx=radice.leftSon
    figlioSx.leftSon=BinaryNode(8)


    radice2 = BinaryNode(5)
    radice2.leftSon = BinaryNode(6)
    radice2.rightSon = BinaryNode(7)
    tree2 = BinaryTree(radice2)

    figlioSx2 = radice2.leftSon
    figlioSx2.leftSon = BinaryNode(8)

    tree.insertAsLeftSubTree(figlioSx,tree2)
    print (tree.root.info)
    tree.root.info=[7,6]
    print (tree.root.info)



    tree.stampa()
    tree2.stampa()