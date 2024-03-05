"""
Support Vector Machine (SVM)은 지도 학습 알고리즘 중 하나로, 데이터를 분류하거나 회귀 분석하는 데 사용됩니다. 
주로 분류 문제에 적용되며, 데이터를 두 개 이상의 클래스로 나누는 데 사용됩니다. 
SVM은 데이터의 고차원 공간에서 최적의 결정 경계를 찾아내어 분류를 수행합니다.

SVM의 주요 아이디어는 다음과 같습니다:

1. 마진 최대화(Margin Maximization): SVM은 결정 경계와 클래스 사이의 마진(데이터와 결정 경계 사이의 거리)을 최대화하는 것을 목표로 합니다. 이는 분류 오류를 최소화하고 일반화 성능을 향상시키는데 도움이 됩니다.
2. 서포트 벡터(Support Vectors): SVM은 결정 경계와 가장 가까운 데이터 포인트들을 서포트 벡터라고 합니다. 이들은 결정 경계를 찾는 데 있어서 주요한 역할을 합니다.
3. 커널 트릭(Kernel Trick): SVM은 커널 함수를 사용하여 데이터를 고차원 공간으로 매핑하여 비선형 문제를 해결할 수 있습니다. 이를 통해 복잡한 패턴을 학습할 수 있습니다.
"""

from sklearn import svm

# XOR의 계산 결과 데이터 --- (※1)
# XOR >> 두 값이 다르면 1, 같으면 0
xor_data = [
    #P, Q, result
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

# 학습을 위해 데이터와 레이블 분리하기 --- (※2)
data = []
label = []
for row in xor_data:
    p = row[0]
    q = row[1]
    r = row[2]
    data.append([p, q])
    label.append(r)

# print(data)  # [[0, 0], [0, 1], [1, 0], [1, 1]]
# print(label) # [0, 1, 1, 0]
    
# 데이터 학습시키기 --- (※3)
clf = svm.SVC() # SVC는 Support Vector Classifier의 약자로, SVM(Support Vector Machine) 알고리즘을 사용하여 분류 문제를 해결하는 머신 러닝 모델
clf.fit(data, label) # 데이터와 레이블을 훈련시킵니다.

# 데이터 예측하기 --- (※4)
pre = clf.predict(data) 
print(" 예측결과:", pre) # [0 1 1 0]

# 결과 확인하기 --- (※5)
ok = 0; total = 0
for idx, answer in enumerate(label):
    p = pre[idx]
    if p == answer: ok += 1
    total += 1
    
print("정답률:", ok, "/", total, "=", ok/total)
