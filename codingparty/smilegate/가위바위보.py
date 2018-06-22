# -*- coding: utf-8 -*-
# 한국어 주석을 사용할 경우 UTF-8 encoding을 꼭 이용해주세요

# [Notice for Python2]
# - 별도의 병렬 처리나 시스템콜, 네트워크/파일접근 등을 하지 마세요 
# - 기본 제공되는 뼈대 코드는 입출력의 이해를 돕기위해 제공되었습니다.
# - 뼈대코드의 활용은 선택사항이며 코드를 직접 작성하여도 무관합니다.

#가장 먼저 실행되는 메인 코드
if __name__ == "__main__":
    # <---메인 코드의 시작---> 

		player = [ int(choose) for choose in raw_input().split() ] #각 플레이어의 선택 결과를 입력받는다 
		winner = 0 # 이 변수에 승리하는 사람들의 수를 저장한다 
		
		rule = {
			"1,2" : 2,
			"1,3" : 1,
			"2,3" : 3,
		}
		
		result = set(player)
		winner = player.count(rule[",".join([str(x) for x in result])]) if len(result) == 2 else 0
			
			
			
		print(winner)
    # <---메인 코드의 끝--->
