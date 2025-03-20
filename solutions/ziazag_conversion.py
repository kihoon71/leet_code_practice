class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        '''
        규칙 1 : 먼저 numRows + numRows - 2 만큼 구간을 끊음
        규칙 2 : 직선 부분을 먼저 모아줌 마지막 라인이 모자라면 모자란 만큼 '' 붙여주기
        규칙 3  : 나머지 부분을 모아서 거꾸로 만들어주기
        '''
        if numRows == 1:
            return s

        size = 2*numRows - 2
        n_iter = len(s) // size + 1

        nbyn_array = []

        for idx in range(n_iter):

            # 직선 라인은 그대로 끊어줌
            left, right = idx*size , (idx+1)*size
            straight_nums = list(s[left:right - (numRows-2)])
            if len(straight_nums) < numRows:
                straight_nums = straight_nums + [''] * (numRows - len(straight_nums))

            # 직선라인 먼저 어펜드
            nbyn_array.append(straight_nums)

            # 이제 경사로 올라가는 라인
            zigzag_nums = s[left + numRows: right]
            if right > len(s) + numRows - 2:
                break
            else:
                reverse_zigzag = list(zigzag_nums)
                reverse_zigzag.reverse() # 아래에서 위로 올라가게 되므로 거꾸로 바꿔줌
                if reverse_zigzag != []:
                    reverse_zigzag = reverse_zigzag + ['']
                    head = [''] * (numRows - len(reverse_zigzag))
                    reverse_zigzag = head + reverse_zigzag 
                    nbyn_array.append(reverse_zigzag)

        result_string = ''
        for data in zip(*nbyn_array):
            temp_string = ''.join(data)
            result_string += temp_string

        return result_string     
