#선형 스트 = 순차 리스트 (입력 순서대로 저장)

#선형 리스트 생성 -> 배열로
katok=["성민",'다현','나연','나현','민영'] 

#[1] 데이터 삽입
'''
간단하게 

katok.append(None) #빈칸 삽입
print(katok)
katok[5]= "윤영"
print(katok)

# 중간 칸에 새로운 데이터를 삽입해야할 때 
katok.append(None)
katok[6]=katok[5]
katok[5]=None #빈칸으로 만들기
print(katok)

katok[5]=katok[4]
katok[4]=None
print(katok)
katok[4]=katok[3]
katok[3]=None
print(katok)
katok[3]="미나"
print(katok)
'''

katok=[] 
# 선형리스트 데이터 추가 함수 
def add_data(friend):
    katok.append(None)
    length=len(katok)
    katok[length-1]=friend
add_data("성민")
add_data("다현")
add_data("나연")
add_data("나현")
add_data("민영")
print(katok)


# 중간 데이터 삽입
katok.append(None)
for current in range(last,current,-1):
    katok[current]=katok[current-1]
    katok[current-1]=None
    
katok[current]=friend

#[2] 데이터 삭제

'''
간단하게 원리 이해

katok[4]=None
katok[4]=katok[5]
katok[5]=katok[6]
katok[6]=None
print(katok)
del(katok[6])
print(katok)
'''
