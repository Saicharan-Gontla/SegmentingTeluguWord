# mode = 1 considers the entire complex gunintham as a single letter
# mode = 2 conisders the complex gunintham as two letters
# These two modes are explained clearly with an example in the Readme file. Pls go through it if u have any doubts.


class Segment:
    gunintham = ['ా', 'ి', 'ీ', 'ు', 'ూ', 'ృ', 'ౄ', 'ె', 'ే', 'ై', 'ొ', 'ో', 'ౌ', 'ఁ', 'ం', 'ః']
    achulu = ['అ', 'ఆ', 'ఇ', 'ఈ', 'ఉ', 'ఊ', 'ఋ', 'ౠ', 'ఎ', 'ఏ', 'ఐ', 'ఒ', 'ఓ', 'ఔ', 'అం', 'అః']
    abnormal_gunintham = ['ఁ', 'ం', 'ః']
    ik = '్'

    def extract(self,word,mode = 1):
        lis = []
        state = "new"

        for i in word:

            if (i==' '):
                lis.append(i)
                state = "new"
            
            if (i in self.abnormal_gunintham and mode==1):
                lis[-1]+=i
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
    