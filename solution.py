import re
c='bbabbababababbbbab'
w='bab'

def answer(chunk,word):
    new = ''
    result = []
    cc = set(chunk)
    ww = set(word)
    if cc==ww and len(word)==3:
        def inner(chunk,word):

            if chunk.find(word)!=-1:
                occ = [m.start() for m in re.finditer('(?='+word+')', chunk)]
                for o in occ:
                    new = chunk[:o]+chunk[o+len(word):]
                    #print (new)
                    inner(new,word)
            else:
                #print (chunk)
                result.append(chunk)
                return chunk
        inner(chunk,word)
        result.sort()
        return result[0]
    else:
        def inner(chunk,word):
            if chunk.find(word)!=-1:
                begin = chunk.replace(word,'',1)
                return inner(begin,word)
            else:
                return chunk
        result = []
        result.append(inner(chunk,word))
        result.append(inner(chunk[::-1],word[::-1])[::-1])
        result.sort()
        return result[0]

print (answer(c,w))
#print (result)
