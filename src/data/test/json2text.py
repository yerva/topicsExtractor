import simplejson as json
import codecs

user='pirroh'#'imph0enix'
fin=user+'.json'
fout=codecs.open(user+'.txt',errors='ignore',mode='w',encoding='ascii')

jsonStr = ""
for l in open(fin):
    jsonStr += l.strip().replace('\\n',' ')

jsonObj = json.loads(jsonStr)

for l in jsonObj:
    print l['text']
    fout.write(l['text']+'\n')
