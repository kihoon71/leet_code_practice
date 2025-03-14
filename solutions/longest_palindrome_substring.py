class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        manacher_string = "#" + '#'.join(s) + "#"
        length_string = len(manacher_string)
        P = [0] * length_string
        center = 0
        right = 0
        longest = ''
        
        for idx in range(1, length_string):
            mirror = 2 * center - idx # 수직선을 떠올리면 좀 더 쉽게 이해 가능

            # right값과 mirror 값을 통해 내부 회문인지를 평가함과 동시에 기존 검사했던 문자열에 회문이 있었는지를 알 수 있음
            if (idx < right ) & ( mirror >= 0 ):
                P[idx] = min(P[mirror], right - idx)

            elif ( idx < right ) & ( mirror < 0 ):
                P[idx] = right - idx

            elif ( idx >= right ):
                P[idx] = 0

            if (idx + P[idx] + 1) >= length_string:
                break
                
            while manacher_string[idx - P[idx] - 1] == manacher_string[idx + P[idx] + 1]: 
                P[idx] += 1
                if (idx + P[idx] + 1) >= length_string:
                    break
               
            if idx + P[idx] > right:
                
                center = idx
                right = idx + P[idx]
                recording_mirror = 2 * center - right # 업데이트 된 시점의 palindrome을 얻기 위하여
                span = manacher_string[recording_mirror:right]
                span_string = ''.join([elem if elem != '#' else '' for elem in span ])
                if len(span_string) > len(longest):
                    longest = span_string
                
        return longest

    # first approach ..!!
    # ### not bad but it is not fast enough
    # def isPalindrome(self, s: str) -> str:
    #     if s == s[::-1]:
    #         return True
    #     return False    

    # def longestPalindrome(self, s: str) -> str:
    #     longest = ''
        
    #     for span in range(1, len(s)+1):
    #         for idx in range(len(s)):
    #             target_string = s[idx:idx+span]
    #             is_palin = self.isPalindrome(target_string)
    #             if is_palin and len(longest) < len(target_string):
    #                 longest = target_string
    #                 break

    #     return longest
