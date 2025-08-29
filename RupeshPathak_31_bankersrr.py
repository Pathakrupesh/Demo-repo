P = 5 
R = 3  

def req(r, avail, allot, need, p_id):
    if any(r[j] > avail[j] for j in range(R)):
        print("Resources insufficient")
        return
    
    for j in range(R):
        avail[j] -= r[j]
        allot[p_id][j] += r[j]
        need[p_id][j] -= r[j]
        
    if isSafe(avail, max, allot):
        print("Req granted")
        
    for i in range(P):
        print(f"P{i:<8} {max[i]} {allot[i]} {need[i]}")
    print()
    
def calcNeed(need, max, allot):
    for i in range(P):
        for j in range(R):
            need[i][j] = max[i][j] - allot[i][j]

def isSafe(avail, max, allot):
    need = [[0] * R for _ in range(P)]
    calcNeed(need, max, allot)
    finish = [0] * P
    safe = []
    work = avail[:]
    count = 0

    while count < P:
        found = False
        for p in range(P):
            if finish[p] == 0 and all(need[p][j] <= work[j] for j in range(R)):
                work = [work[j] + allot[p][j] for j in range(R)]
                safe.append(p)
                count += 1
                finish[p] = 1
                found = True

        if not found:
            print("Unsafe state")
            return False

    print("Safe state")
    print("Safe sequence is:", safe)
    return

process = [0, 1, 2, 3, 4]
avail = [1, 3, 2]
max = [[3, 2, 2], 
       [8, 0, 2], 
       [4, 3, 3], 
       [2, 2, 2], 
       [4, 3, 3]]
allot = [[0, 1, 0], 
         [2, 0, 0], 
         [3, 0, 2], 
         [2, 1, 1], 
         [0, 0, 2]]

need = [[0] * R for sthg in range(P)]
calcNeed(need, max, allot)

r = [0, 2, 1]
i = 2
print(f"Request: {r} on Process P{i}")
print("Available Resources:", avail)
print()

print(f"{'Process'} {'Max':>5} {'Allocated':>15} {'Need':>4}")

for i in range(P):
    print(f"P{i:<8} {max[i]} {allot[i]} {need[i]}")
print()

req(r, avail, allot, need, i)