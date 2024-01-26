#선형 스트 = 순차 리스트 (입력 순서대로 저장) 처리 프로그램


#[1] 데이터 삽입
'''
원리 이해

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

맨 뒤에 빈칸을 삽입하고 바로 앞자리와 교환하는 행위를 반복
이후 빈칸이 된 해당 위치까지 가서 새로운 값을 삽입
'''

#배열 선언 선형리스트 생성 -> 파이썬 배열로
katok=[] 
select=0

# 데이터 삽입함수 
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


# 데이터 삽입함수

def insert_data(position,friend):
    if position<0 or position>len(katok):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return
    
    katok.append(None) #빈 자리 삽입
    length=len(katok) #현재 배열의 크기
    
    for i in range(length-1,position,-1):
        katok[i]=katok[i-1] # 빈 자리와 교환해서 뒤로 보내기
        katok[i-1]=None #원래 자리를 빈칸으로
    
    katok[position]=friend #지정한 위치에 새로운 값 추가
    print(katok)


# for i in range(값1, 값2, 값3)에서 값1과 값2가 같으면 한 번도 수행하지 않는다.

#작동 테스트
insert_data(3,'다은')

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

해당 위치의 데이터를 None으로 삭제한 후 뒤의 데이터를 앞으로 보냄. 
반복해서 빈칸이 된 마지막 원소 삭제
'''

# 데이터 삭제 함수
def delete_data(position):
    
    if position<0 or position>len(katok):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return
    
    length=len(katok) #현재 배열의 크기
    katok[position]=None # 데이터 삭제
    
    for i in range(position+1,length):
        katok[i-1]=katok[i] # 뒤의 값을 앞으로 땡겨옴
        katok[i]=None #뒷자리를 다시 빈칸으로
    
    del(katok[length-1])
    print(katok)
    
delete_data(2)

# 메인코드

if __name__=="__main__": # 모듈이 아닌 파이썬 파일을 직접 실행했을 때만 아래 코드를 실행
    while (select!=4):
        select=int(input("메뉴를 선택하세요. 1: 추가, 2: 삽입, 3:삭제, 4:종료"))
        
        if (select==1):
            data=input("추가할 데이터를 입력하세요.")
            add_data(data)
            
        if (select==2):
            pos=int(input("삽입할 위치를 입력하세요."))
            data=input("삽입할 데이터를 입력하세요.")
            insert_data(pos,data)
            
        if(select==3):
            pos=input("삭제할 데이터의 위치를 입력하세요.")
            delete_data(pos)
        
        elif(select==4):
            print(katok)
            exit
            2
            
        else:
            print("1~4 중 하나를 입력하세요.")