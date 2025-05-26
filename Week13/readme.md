## 머신러닝 이해

#### 1. 확률, 확률뷴포, 중심극한정리, 조건부확률
- 머신러닝은 중심극한정리(공리)를 바탕으로한 가설검저, 신뢰구간 등을 취급하지 않는다
#### 2. Gaussian Naive Model
- 판별모델과 생성모델(discriminative vs generative model)을 이해
- https://jakevdp.github.io/PythonDataScienceHandbook/05.05-naive-bayes.html
> - In machine learning, generative models and discriminative models represent two distinct approaches to learning from data. Generative models aim to model the underlying distribution of data, while discriminative models focus on directly learning the decision boundaries between classes or categories. Essentially, generative models try to understand how the data is structured, while discriminative models focus on making predictions based on the data's characteristic
> - 💡 비유적으로 설명하자면:
>> - Generative Model은 "어떤 사람이 어떤 말을 했을지를 상상할 수 있는 능력" → 즉, 전체 상황을 이해하고 재현할 수 있음
>> - Discriminative Model은 "그 사람이 스팸인지 아닌지를 빠르게 판단하는 능력" → 즉, 정확하게 구분하는 데 집중함
#### 3. KDE(Kernel Density Estimation)
- 비지도학습
- "현재 KDE 모델이 입력 데이터 X를 얼마나 잘 설명하는가"를 나타내는 전체 로그 우도이며, 값이 클수록 모델이 데이터 분포에 더 잘 맞는다는 의미
- bandwidth를 parameter로 튜닝하여 어떤 bandwidth가 입력데이터를 가장 잘 그럴 듯하게 표현해 주고있는지?
- 산출식으로는 total_log_likelihood = kde.score(X) 가 가장 큰 bandwidth를 결정하여야 함
#### 4. GAN, autoencoder 모댈
