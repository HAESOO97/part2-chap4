#문제 : 수평으로 두칸 이동한 뒤에 수직으로 한칸 이동하기
#     : 수직으로 두칸 이동한 뒤에 수평으로 한칸 이동하기
#8*8좌표평면에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오
#행위치 : 1~8 , 열위치 : a~l ex) (1,1)=a1
#<입력> : a1-> <출력>:2

#현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]))-int(ord('a'))+1
#column = input_data[0]  
steps = [(-1,-2),(-1,2),(1,-2),(1,2),(-2,-1),(-2,1),(2,-1),(2,1)]

result = 0
for step in steps:
  next_row = row+step[0]
  next_column = column + step[1]

  if next_row>=1 and next_row<=8 and next_column>=1 and next_column<=8:
    result+=1
print(result)  
