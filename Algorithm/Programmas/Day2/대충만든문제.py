def solution(keymap, targets):
    result=[]
    
    # 2차원 리스트 생성
    keymap=[list(i) for i in keymap]
    targets=[list(i) for i in targets]
    
    for target in targets:
        count = 0
        for tar in target:
            min_count = 101
            for key in keymap:
                if tar in key:
                    min_count = min(min_count, key.index(tar) + 1)
            if min_count == 101:
                count = -1
                break
            count += min_count
        result.append(count if count != 0 else -1)
    return result
                    