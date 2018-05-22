import gensim,logging,pickle,re
logging.basicConfig(format='%(asctime)s : %(levelname)s : '
                           '%(message)s', datefmt='%H:%M:%S',level=logging.INFO)

model = gensim.models.KeyedVectors.load_word2vec_format \
    (r"C:\Users\wx950\Desktop\math\GoogleNews-vectors-negative300.bin", binary=True)

di={}
real_word=[]
fake_word=[]
with open('fake','rb') as r:
    fake=pickle.load(r)
with open('real','rb') as r:
    real=pickle.load(r)
for sentence in fake:
    resentence=re.sub('[^A-Z a-z0-9]+', '', sentence)
    word=resentence.split(' ')
    newsentence=[]
    for w in word:
        if w is '': continue
        if w in model:
            di[w]=model[w]
            newsentence.append(w)
    fake_word.append(newsentence)

for sentence in real:
    resentence=re.sub('[^A-Z a-z0-9]+', '', sentence)
    word=resentence.split(' ')
    newsentence=[]

    for w in word:
        if w is '': continue
        if w in model:
            di[w]=model[w]
            newsentence.append(w)
    real_word.append(newsentence)

with open('w2v','wb') as o:
    pickle.dump(di,o)
with open('realword','wb') as o:
    pickle.dump(real_word,o)
with open('fakeword','wb') as o:
    pickle.dump(fake_word,o)