'''
输入式kruskal算法
'''

m = int(input('m(边数):'))  #边数
n = int(input('n(顶点数):'))  #顶点数
a = [[] for _ in range(m)]
print('请输入连结矩阵:')
for i in range(m):
    a[i] = list(map(int,input().split(' ')))  #此处为实现输入式算法关键
a.sort(key=lambda a:a[2])

fa = [_ for _ in range(n)]
def found(node):
    if fa[node] == node:
        return node
    else:
        fa[node] = found(fa[node])
        return fa[node]

def unite(node1,node2):
    node1 = found(node1)
    node2 = found(node2)
    if node1 == node2:
        return False
    else:
        fa[node1] = node2
        return True

def kruskal(m,n,a):
    a.sort(key=lambda a:a[2])

    lian_num = 0
    res = []
    for i in range(m):
        if unite(a[i][0],a[i][1]):
            res.append(a[i])
        lian_num += 1

        if lian_num == n - 1:
            break
    return res

res = kruskal(m , n, a)
s = 0
for l in res:
    print(f'{l[0]}<-->{l[1]}:{l[2]}')
    s = s + l[2]
print(f'最小树权值之和:{s}')
print(a)

'''
输入示例

m = 12
n = 7
输入连结矩阵
0 1 2
0 3 5
0 5 8
1 2 7
1 3 7
1 4 2
2 4 3
3 4 6
3 5 7
3 6 3
4 6 4
5 6 4
'''