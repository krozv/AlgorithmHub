def solution(words, queries):
    answer = []
    # tree를 두개 만들면 되지않을까? pre-tree, post-tree
    # 검색 기능이 포함되어야함 -- search
    # 접두사, 접미사 검색이 가능해야함
    class Node:
        def __init__(self):
            # self.val = ''
            self.children = {}
            self.is_end = False
            self.word = {}
        
    class Tree:
        def __init__(self):
            self.root = Node()
        
        # query를 집어넣었을 경우, 검색하는 함수
        def search(self, query):
            node = self.root
            # num = 0
            for char in query:
                if char == '?':
                    # print(node.word)
                    return node.word.get(len(query), 0)
                # 물음표 처리는 나중에 하자~
                if not node.children:
                    return 0
                if char not in node.children:
                    return 0
                node = node.children[char]
                
                if len(query) not in node.word:
                    return 0
            
        
        def insert(self, string):
            node = self.root
            
            for char in string:
                # 불포함의 경우
                if char not in node.children.keys():
                    new_node = Node()
                    # new_node.val = char
                    node.children[char] = new_node
                    
                if len(string) not in node.word.keys():
                    node.word[len(string)] = 1
                else:
                    node.word[len(string)] += 1
                # print(string, char, node.word)
                node = node.children[char]
            
            node.is_end = True
            # print(node.val)
                
    
    pre_tree = Tree() # 앞에서 검색하는 트리
    post_tree = Tree() # 뒤에서 검색하는 트리
    
    # tree 생성
    for word in words:
        pre_tree.insert(word)
        re_word = word[::-1]
        post_tree.insert(re_word)
    
    temp = {}
    for query in queries:
        
        # 검색어 중복의 경우
        if query in temp.keys():
            if query[0] == '?':
                answer.append(post_tree.search(query[::-1]))
            else:
                answer.append(pre_tree.search(query))
            continue
        temp[query] = 0
        
        # post-tree에서 검색
        if query[0] == '?':
            answer.append(post_tree.search(query[::-1]))
        # pre-tree에서 검색    
        else:
            answer.append(pre_tree.search(query))
        
    return answer