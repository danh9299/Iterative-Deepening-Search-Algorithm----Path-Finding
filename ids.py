graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['G'],
    'D': [],
    'E':['F'],
    'G':[],
    'F':[]
}
# Khởi tạo giá trị cha của các nút ban đầu là rỗng
parent = {
    'A': '',
    'B' : '',
    'C' : '',
    'D' : '',
    'E' : '',
    'F' : '',
    'G' : ''
}
#Chiều sâu
def DFS(start,end,graph,maxDepth):
    print('Đang tìm đường...',start)
    if start == end:
        return True
    if maxDepth <= 0:
        return False
    for node in graph[start]:
        #Lưu lại giá trị cha của nút (phục vụ cho việc in đường đi sau này)
        parent[node] = start
        if DFS(node,end,graph,maxDepth-1):
            return True
    return False
#Sâu dần
def iterativeDDFS(start,end,graph,maxDepth):
    for i in range(maxDepth):
        if DFS(start,end,graph,i):
            return True
    return False
#In ra đường đi
def pathShow(end):
    if end == start:
        print(end,end="")
        return
    else:
        print(end,end="")
        while parent[end] != start:
            print("->",parent[end],end="")
            end = parent[end]
        print("->",parent[end])
        
#Nhập dữ liệu
start = (input("Nhập điểm bắt đầu: "))
start = start.upper()
while start not in graph:
    print("Điểm bắt đầu phải có trong cây!")
    start = input("Nhập lại điểm bắt đầu: ")
    start = start.upper()
end = input("Nhập điểm cần đến: ")
end = end.upper()
while end not in graph:
    print("Điểm đến phải có trong cây!")
    end = input("Nhập lại điểm cần đến: ")
    end = end.upper()

depth = int(input("Nhập độ sâu (nhập dữ liệu số): "))
while (depth == 0):
    depth = int(input("Nhập độ sâu (nhập dữ liệu số): "))

#Gọi hàm
if not iterativeDDFS(start,end,graph,depth):
    print("Không tìm thấy đường đi!")
else:
    print('Đã thấy đường')
    pathShow(end)


