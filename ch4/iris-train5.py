"""
데이터 영역 
Sepal Length : 꽃받침 길이
Sepal Width : 꽃받침 너비
Petal Length : 꽃잎 길이
Petal Width : 꽃잎 너비

레이블 영역 
Name : 학명
"""


from sklearn import svm, metrics
import random, re

import pickle

# 붓꽃의 CSV 데이터 읽어 들이기 --- (※1)
csv = []
with open('iris.csv', 'r', encoding='utf-8') as fp:
    
    # 한 줄씩 읽어 들이기
    for line in fp:
        line = line.strip()    # 줄바꿈 제거, 5.1,3.5,1.4,0.2,Iris-setosa
        cols = line.split(',') # 쉼표로 자르기, ['5.1', '3.5', '1.4', '0.2', 'Iris-setosa' 
        
        # 문자열 데이터를 숫자로 변환하기
        fn = lambda n : float(n) if re.match(r'^[0-9\.]+$', n) else n
        cols = list(map(fn, cols))
        csv.append(cols)

# 가장 앞 줄의 헤더 제거
del csv[0] # [[5.1, 3.5, 1.4, 0.2, 'Iris-setosa'],,,]

# 데이터 셔플하기(섞기) --- (※2)
random.shuffle(csv) # [[5.5, 3.5, 1.3, 0.2, 'Iris-setosa']...]

# 학습 전용 데이터와 테스트 전용 데이터 분할하기(2:1 비율) --- (※3)
total_len = len(csv)
train_len = int(total_len * 2 / 3)

train_data = []
train_label = []
test_data = []
test_label = []
for i in range(total_len):
    data  = csv[i][0:4]
    label = csv[i][4]
    if i < train_len:
        train_data.append(data)
        train_label.append(label)
        
    else:
        test_data.append(data)
        test_label.append(label)

# 데이터를 학습시키고 예측하기 --- (※4)
clf = svm.SVC()
clf.fit(train_data, train_label)

# 객체 저장
with open('model.pkl', 'wb') as f:
    pickle.dump(clf, f)