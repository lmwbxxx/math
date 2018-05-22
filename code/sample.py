import json,logging,pickle
logging.basicConfig(format='%(asctime)s : %(levelname)s : '
                           '%(message)s', datefmt='%H:%M:%S',level=logging.INFO)
robotid = set()
user_review_count = {}
user_reviews = {}
i=0
with open(r'C:\Users\wx950\Desktop\math\dataset\review.json','rb') as review_data:
    for line in review_data:
        if i%1000==0: print (i)
        i+=1
        if i>100000: break
        info = json.loads(line)
        user_id = info['user_id']
        text = info['text']
        date = info['date']

        if user_id not in user_reviews:
            user_reviews[user_id] = [text]
        else:
            user_reviews[user_id].append(text)

        if (user_id, date) in user_review_count:
            user_review_count[(user_id, date)] += 1
            if user_review_count[(user_id, date)]>5:
                robotid.add(user_id)
        else:
            user_review_count[(user_id, date)] = 1
logging.info('total number of robotid: %d',len(robotid))

fake_review=set()
real_review=set()
for user in user_reviews:
    if user in robotid and len(fake_review)<=2000:
        fake_review=fake_review.union(user_reviews[user])
    if user not in robotid and len(real_review)<=8000:
        real_review=real_review.union(user_reviews[user])
    if len(fake_review)>=2000 and len(real_review)>=8000:
        break

logging.info('%d,%d',len(real_review),len(fake_review))
with open(r'fake','wb') as o:
    pickle.dump(fake_review,o)
with open(r'real', 'wb') as o:
    pickle.dump(real_review, o)
with open(r'robotid', 'wb') as o:
    pickle.dump(robotid, o)
