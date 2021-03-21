#A :북쪽으로부터 떨어진 칸의 개수(X좌표) b : 서쪽으로부터 떨어진 칸의 개수(Y좌표)
#1 : 현재위치에서 현재방향을 기준으로 왼쪽방향(반시계방향으로 90 도 회전한 방향)부터 차례대로 갈곳을 정한다.
#2 : 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면 왼쪽방향으로 회전한 다음 왼쪽으로 한칸을 전진한다. 왼쪽방향에 가보지 않은 칸이 없다면 왼쪽방향으로 회전만 수행하고 1단계
#    돌아간다.
#3 : 만약 네방향 모두 이미 가본 칸이거나 바다로 되어있는 칸인 경우에는 바라보는 방향을 유지한채로 한칸 뒤로가고 1단계로 돌아간다. 단, 이때 뒤쪽방향이 바다인 칸이라 뒤로 갈수 없는 경우
#    움직임을 멈춘다.
# 0 : 북쪽 1: 동쪽 2 : 남쪽 3 : 서쪽
# 0 : 육지 1: 바다
#캐릭터가 방문한 칸의 수 출력

n,m = map(int,input().split())
d=[[0]*m for i in range(n)]
x,y,direction = map(int,input().split())

array = []
for i in range(n):
  array.append(list(map(int,input().split()))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
 
def turn_left():
  global direction
   if direction == -1:
           direction = 3
               
count = 1
turn_time =0
while True:
		turn_left()
		nx = x+dx[direction]
		ny = y+dy[direction]
							 
		if d[nx][ny]==0 and array[nx][ny]==0:
				x=nx
				y=ny
			  count+=1
				turn_time = 0
		else:
				turn_time+=1
		if turn_time == 4:
				nx = x-dx[direction]
				ny = y-dy[direction]
				if array[nx][ny]==0:
							x=nx
							y=ny
		    else:
							 break
				turn_time = 0
print(count)
							
							 
							 
							 
							 
							 
							 
							 
							 
							 
							 
               
               

