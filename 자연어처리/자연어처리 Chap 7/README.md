# 6. AR의 GPT, AE의 BERT, seq2seq의 BART

## 트랜스포머 이후 역사 살펴보기

![A%20Survey%20of%20Large%20Language%20Models%20fig%203.png](A%20Survey%20of%20Large%20Language%20Models%20fig%203.png)
![Large%20Language%20Models%20fig%2024.png](Large%20Language%20Models%20fig%2024.png)

- 위 그림은 2023년에 발표된 LLM survey 논문의 타임라인 삽화
  - 파라미터나 10B 이상이고 결과 리포트가 개방된 모델만 선정했으며 arXiv 제출 날짜 기준 정렬
    - 관련 논문이 없다면 가장 먼저 발표됐던 날짜 기준으로 설정
  - 노랑색은 모델 체크포인트에 접근할 수 있는 것들
  - 참고로 이 논문은 124페이지 분량
- 아래 그림은 2024년 발표된 LLM survey 논문의 타임라인 삽화
  - 언어 모델의 한계를 부순 상징적인 작업들을 BERT, GPT, Transformer에 해당하는 행으로 배치
  - 스페이드 문양은 모델과 접근법 모두 제시, 다이아몬드 문양은 접근법만 제시
- Transformer가 등장한 이후 디코더만 채용한 모델인 GPT가 2018년, 인코더만 채용한 모델인 BERT가 2019년 등장
  - 단순히 연구를 위한 아키텍처로써 유명했으나 2022년 말 ChatGPT가 대중에 전면 등장하면서 주목도와 발전속도가 이전과 달라짐
  - 이번 스터디의 남은 챕터는 GPT, BERT, BART를 묶어서 보고 나머지 LLM을 두 번에 나눠 소개

## GPT-1

### 등장배경

- 논문의 Introduction에서는 자연어처리에 대한 지도학습과 비지도학습을 비교
  - 지도학습을 위한 대규모 데이터가 부족하며 구축하자니 시간이 오래걸림
  - 또한 지도학습이 가능해도 [[Word2Vec]], [[Glove]] 등의 비지도학습 방식으로 사전학습된 단어 임베딩을 사용하는 것이 성능을 향상시켰음
- 언어 모델의 준지도 학습, 비지도 학습에 있어 다음과 같은 어려움이 있음
  - 전이학습에 유용한 텍스트 rerpesentation을 학습하기 위해선 어떤 objective가 가장 효과적인가
  - 이전의 연구들은 특정 task만을 위한 접근이 주로 이뤄짐
- GPT-1은 비지도 사전학습-fine tuning의 조합을 통해 준지도학습 접근을 제시
  - 비지도 사전학습은 language modeling objective를 사용해 라벨링 되지 않은 대규모 데이터로 훈련
  - fine tuning은 목표하는 task에 대한 지도학습 objective를 사용
- **이를 보이기 위해 transformer를 사용**

### 아키텍처

![GPT%20fig%201.png](GPT%20fig%201.png)

#### Unsupervised pre-training

- 주어진 토큰 $U={u_1, \cdots, u_n}$와 맥락 윈도우 크기 k에 대해 아래의 likelihood(우도)를 최대화
  - 파라미터들은 SGD로 훈련

$$
L_1(U)=\sum_ilogP(u_i|u_{i-k},\cdots,u_{i-1};\Theta)
$$

- 토큰의 맥락 벡터 $U_c=\{u_{-k},\cdots,u_{-1}\}$, layer의 수 n, 토큰 임베딩 행렬 $W_e$, 위치 임베딩 행렬 $W_p$에 대해 아래와 같은 분포가 도출됨

$$
\begin{align}
&h_0=U_cW_e+W_p
\\&h_l=transformer\_block(h_{l-1})\forall i \in [1,n]
\\&P(u)=softmax(h_nW_e^T)
\end{align}
$$

#### Supervised fine-tuning

- 데이터 셋은 라벨 y와 sequence $x^1,\cdots,x^m$으로 구성
- 최종 출력 $h_l^m$에 대해 y는 다음과 같이 예측함

$$
P(y|x^1,\cdots,x^m)=softmax(h_l^mW_y)
$$

- 다음과 같은 objective를 최대화

$$

L_2(C)=\sum_{(x,y)}logP(y|x^1,\cdots,x^m)
$$

- 보조적인 objective를 사용하면 지도학습된 모델의 일반화 능력을 개선해주고 수렴을 가속하켜 fine-tuning을 도움

$$
L_3(C)=L_2(C)+\lambda L_1(C)
$$

#### Task-specific input transformations

- 시작 토큰은 \<s\>, 끝 토큰은 \<e\>, 텍스트 쌍을 사용하는 경우 이를 구분하는 delimiter 토큰 $을 사용

#### 모델 정보

##### 사전 학습

- 비지도 학습에7천 개의 출판되지 않은 책들dls BooksCorpus, ELMo에 사용된 1B 단어 벤치마크 사용
- 12개의 decoder layer
- 768차원과 12개 head의 masked self-attention head
- FFNN은 3072차원
- Adam 옵티마이저, 최대 학습률은 2.5e-4
  - 0에서 첫 2000번째 업데이트까지 선형적으로 증가하다가 cos 속도로 0으로 줄임
- 배치 크기 64, 100 epoch, 최대 512 토큰을 BPE로 사전 구축
- LayerNorm을 위한 파라미터는 $N(0,0.02)$
- residual connection, embedding, attention에 0.1 dropout 적용
- 수정된 L2 규제 적용(w=0.01)
- 활성화 함수는 GELU
- positional embedding은 transformer에서 사용한 파형이 아닌 위치 임베딩 사용

##### fine-tuning

- 사전학습에서 사용한 하이퍼 파라미터 세팅을 그대로 사용
- classifier의 drop out은 0.1
- 학습률은 6.25e-5, 배치크기는 32, epoch는 3
- 선형 학습률 감쇠를 사용
- $\lambda$는 0.5

### 코드

```python
from transformers import AutoModel, AutoTokenizer

gpt_model = AutoModel.from_pretrained("openai-community/openai-gpt")
gpt_tokenizer = AutoTokenizer.from_pretrained("openai-community/openai-gpt")

# Pipeline과 Trainer를 이용한 fine-tuning과 text generation task
from transformers import AutoTokenizer, AutoModel, TrainingArguments, Trainer
from datasets import Dataset

# 모델과 토크나이저 로드
model_name = 'openai-community/openai-gpt'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# 파인튜닝을 위한 데이터 준비
train_texts = ["첫 번째 문장입니다.", "두 번째 문장입니다."]  # 예시 텍스트

# 데이터셋 생성
train_dataset = Dataset.from_dict({'text': train_texts})

def preprocess_function(examples):
    inputs = tokenizer(examples['text'], truncation=True, padding='max_length', max_length=128)
    inputs['labels'] = inputs['input_ids'].copy()
    return inputs

tokenized_train = train_dataset.map(preprocess_function, batched=True)

# 트레이닝 설정
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=8,
    learning_rate=5e-5
)

# 트레이너 생성
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_train,
    data_collator=lambda data: {
        'input_ids': torch.stack([f['input_ids'] for f in data]),
        'attention_mask': torch.stack([f['attention_mask'] for f in data]),
        'labels': torch.stack([f['labels'] for f in data])
    }
)

# 필요한 라이브러리 임포트
import torch

# 모델 파인튜닝
trainer.train()

# 파인튜닝된 모델로 텍스트 생성
input_text = "생성할 시작 문장"
input_ids = tokenizer.encode(input_text, return_tensors='pt')
output = model.generate(input_ids, max_length=50, num_return_sequences=1)
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)

# Pytorch를 이용한 fine-tuning과 text generation task
from torch.utils.data import DataLoader, Dataset

# 데이터셋 준비
texts = ["미세 조정에 사용할 첫 번째 문장.", "두 번째 문장 추가."]
tokenizer = OpenAIGPTTokenizer.from_pretrained('openai-gpt')

class TextDataset(Dataset):
    def __init__(self, texts, tokenizer):
        self.input_ids = []
        for text in texts:
            encoded = tokenizer.encode(text, add_special_tokens=True)
            self.input_ids.append(torch.tensor(encoded))

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return self.input_ids[idx]

dataset = TextDataset(texts, tokenizer)
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

# 모델 로드
model = OpenAIGPTLMHeadModel.from_pretrained('openai-community/openai-gpt')

# 옵티마이저 설정
optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)

# 트레이닝 루프
model.train()
for epoch in range(3):
    for batch in dataloader:
        outputs = model(batch, labels=batch)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
    print(f"Epoch {epoch+1} 완료, 손실: {loss.item()}")

# 모델 저장
model.save_pretrained('./fine-tuned-gpt1')
tokenizer.save_pretrained('./fine-tuned-gpt1')

# 저장된 모델과 토크나이저 로드
model = OpenAIGPTLMHeadModel.from_pretrained('./fine-tuned-gpt1')
tokenizer = OpenAIGPTTokenizer.from_pretrained('./fine-tuned-gpt1')

# 텍스트 생성 함수 정의
def generate_text(prompt, max_length=50):
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    output = model.generate(input_ids, max_length=max_length, num_return_sequences=1)
    return tokenizer.decode(output[0], skip_special_tokens=True)

# 텍스트 생성 예시
prompt = "미세 조정된 모델을 사용하여 생성된 텍스트:"
generated_text = generate_text(prompt)
print(generated_text)

# Pre-training은 생략
```

### GPT-2

#### 등장배경

### GPT-3

### GPT-4

## BERT

### 등장배경

- GPT의 단방향성에 이의를 제기
  - 문장 단위 task에 적합할지 몰라도 질의응답 등의 토큰 단위 task는 양방향성 맥락이 중요
  - 그렇다고 ELMo 등의 feature 기반으로 순방향과 역방향을 독립적으로 학습시켜 합치는 모델이 좋은 성능을 보이진 않음
- 즉 GPT가 사용했던 pre-training과 fine-tuning 방식이 복잡한 모델의 필요성을 줄이면서 양방향 맥락을 참조토록 하는 deep bidirectional Transformer 형식을 취해 SOTA를 달성
  - BERT의 특징인 Masked Language Modeling으로 모델의 단방향성을 상당 부분 극복

### 아키텍처

![Bert%20Fig%201.png](Bert%20Fig%201.png)

- [[ELMo]], [[GPT-1]] 등에서 보인 사전 학습-finet tuning이 큰 효과를 보이면서 transformer 이후로 많은 LLM들이 이 방식을 채택
  - 그림에서 볼 수 있듯이 출력 layer만 제외하고 보면 같은 구조를 사용
  - 서로 다른 downstream task에 사전학습된 모델의 파라미터를 사용하면서도 fine tuning을 통해 모든 파라미터들을 각 task에 맞게 조정

#### Pre-training BERT

- BooksCorpus, 영문 위키피디아 사용
  - 위키피디아는 문단에서만 단어를 추출, 2500M 단어 분량
  - 긴 연속 sequence를 추출 할 때 문장 수준의 corpus보다는 문서 수준의 corpu를 사용하는 것이 더 중요하다고 함

##### Masked LM

- 전체 토큰의 15%를 무작위로 masking하고 이들만 예측
  - 이중 80%는 \[MASK\]로, 10%는 무작위 토큰으로 대체하며 10%는 변하지 않음
  - 이에 대한 Cross Entropy Loss를 사용
- 양방향으로 학습되는 효과를 얻을 수 있지만 fine tuning 중에 \[MASK\] 토큰이 등장하지 않기 때문에 사전학습과 불일치 할 수 있다는 문제점이 있음

##### Next Sentence Prediction

- 한 문장 쌍을 줄 때 절반은 두 문장이 연결된 문장, 절반은 두 문장이 서로 연결되지 않은 문장
  - 이 학습 정보는 CLS 토큰에 담기며 최종적인 예측 정확도는 97~98%
  
#### 모델 정보

##### 사전 학습

- BERT_base(L=12, H=768, A=12, 전체 파라미터=110M)과 BERT_large(L=24, H=1024, A=16, 전체 파라미터=340M)를 제시
  - L은 layer 수, H는 hideen layer의 차원 수, A는 head의 수
  - BERT_base는 GPT와 비교하기 위한 목적의 설정
- 배치 크기 256, 1M steps, batch 당 총 토큰 수는 128K

##### fine-tuning

- 사전학습에서 사용한 하이퍼 파라미터 세팅을 그대로 사용, 전체적으로 다음 범위에 해당
  - batch size 16, 32
  - lr (Adam) 5e-5, 3e-5, 2e-5
  - epochs 2, 3, 4
- drop out은 0.1

### 코드

```python
# 기본적인 예제 코드
from transformers import AutoModel, AutoTokenizer

bert_model = AutoModel.from_pretrained("google-bert/bert-base-cased")
bert_tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-cased")

# Pipeline과 Trainer를 이용한 fine-tuning과 sequence classification task
from transformers import pipeline
from transformers import BertForSequenceClassification, TrainingArguments, Trainer
from datasets import Dataset

# 파이프라인 생성
classifier = pipeline('text-classification', model='bert-base-multilingual-cased', tokenizer='bert-base-multilingual-cased')

# 예측할 텍스트
test_text = "예측할 문장입니다."

# 예측
prediction = classifier(test_text)
print(f"예측된 클래스: {prediction[0]['label']}, 점수: {prediction[0]['score']}")

# 파인튜닝을 위한 데이터 준비
train_texts = ["긍정적인 문장입니다.", "부정적인 문장입니다."]
train_labels = [1, 0]  # 예시 레이블

# 모델 로드
model = BertForSequenceClassification.from_pretrained('bert-base-multilingual-cased', num_labels=2)

# 토크나이저와 데이터셋 준비
tokenizer = classifier.tokenizer

# 데이터셋 생성
train_dataset = Dataset.from_dict({'text': train_texts, 'label': train_labels})

def preprocess_function(examples):
    return tokenizer(examples['text'], truncation=True, padding=True)

tokenized_train = train_dataset.map(preprocess_function, batched=True)

# 트레이닝 설정
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=8,
    learning_rate=5e-5
)

# 트레이너 생성
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_train
)

# 모델 파인튜닝
trainer.train()

# 파인튜닝된 모델을 파이프라인에 적용
classifier.model = model

# 새로운 문장으로 예측
new_text = "분석할 새로운 문장입니다."
new_prediction = classifier(new_text)
print(f"예측된 클래스: {new_prediction[0]['label']}, 점수: {new_prediction[0]['score']}")

# Pytorch를 이용한 fine-tuning과 sequence classification task
import torch
from torch.utils.data import DataLoader, Dataset
from transformers import BertTokenizer, BertForSequenceClassification

# 분류할 텍스트와 라벨
texts = ["첫 번째 문장입니다.", "두 번째 문장입니다."]
labels = [0, 1]  # 예: 부정=0, 긍정=1

# 토크나이저와 모델 로드
tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
model = BertForSequenceClassification.from_pretrained('bert-base-multilingual-cased', num_labels=2)

# 데이터셋 준비
class TextClassificationDataset(Dataset):
    def __init__(self, texts, labels, tokenizer):
        self.encodings = tokenizer(texts, truncation=True, padding=True)
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

dataset = TextClassificationDataset(texts, labels, tokenizer)
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

# 옵티마이저 설정
optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)

# 트레이닝 루프
model.train()
for epoch in range(3):
    for batch in dataloader:
        optimizer.zero_grad()
        outputs = model(**batch)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
    print(f"Epoch {epoch+1} 완료, 손실: {loss.item()}")

# 모델 저장
model.save_pretrained('./fine-tuned-bert')
tokenizer.save_pretrained('./fine-tuned-bert')

# 저장된 모델과 토크나이저 로드
model = BertForSequenceClassification.from_pretrained('./fine-tuned-bert')
tokenizer = BertTokenizer.from_pretrained('./fine-tuned-bert')

# 예측 함수 정의
def predict(text):
    model.eval()
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()
    return predicted_class

# 예측 예시
test_text = "예측할 문장입니다."
prediction = predict(test_text)
print(f"예측된 클래스: {prediction}")

# Pre-training은 생략
```

## BART

### 등장배경

### 아키텍처

### 코드

```python
```
