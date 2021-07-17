class Segment:
    gunintham = ['ా', 'ి', 'ీ', 'ు', 'ూ', 'ృ', 'ౄ', 'ె', 'ే', 'ై', 'ొ', 'ో', 'ౌ', 'ఁ', 'ం', 'ః']
    achulu = ['అ', 'ఆ', 'ఇ', 'ఈ', 'ఉ', 'ఊ', 'ఋ', 'ౠ', 'ఎ', 'ఏ', 'ఐ', 'ఒ', 'ఓ', 'ఔ', 'అం', 'అః']
    ik = '్'

    def extract(self,word):
        lis = []
        state = "new"

        for i in word:

            if (i==' '):
                lis.append(i)
                state = "new"
            
            elif (state=="new"):
                lis.append(i)
                state = "old"
            
            elif (state=="old"):
                if i in self.gunintham:
                    lis[-1] += i
                    state = "new"
                elif (i==self.ik):
                    lis[-1] += i
                    state = "unknown"
                else:
                    lis.append(i)
                    state = "old"
            
            else:
                if i in self.achulu:
                    lis.append(i)
                    state = "old"
                elif (i=='\u200c'):
                    state = "old"
                else:
                    lis[-1] += i
                    state = "old"
        return lis
    