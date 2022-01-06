def gcdOfStrings(self, str1: str, str2: str) -> str:
        q1,q2=[],[]
        for a in str1:
            if a not in q1:
                q1.append(a)
        for b in str2:
            if b not in q2:
                q2.append(b)
        if q1==q2:
            answer=""
            for i in q1:
                answer+=i
            return answer
        return ""