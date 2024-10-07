# 5. Transformer의 등장

## 등장배경

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)에서 제시한 아키텍처
- RNN은 긴 입력에 취약하다는 점, 병렬 연산이 불가능하다는 점이 한계
  - LSTM이 획기적으로 개선했으나 아키텍처적으로 근본적인 문제가 존재
- CNN은 RNN보다도 긴 입력에 취약하다는 점, 입력이나 출력의 길이에 비례하여 복잡도가 증가한다는 점이 한계
- attention 메커니즘은 시퀀스의 길이에 무관하게 사용할 수 있지만 RNN이나 CNN 모델의 요소로만 사용하고 있음
  - transformer는 앞선 한계를 극복하기 위해 attention을 적극적으로 도입한 최초의 모델
  - 특히, 병렬화를 위한 multi-head attention과 의존성 문제 해결을 위한 self attention 메커니즘을 제시

## 아키텍처

### 전체

![(transformer%20abstract%20structure.png](transformer%20abstract%20structure.png)![The%20Transformer-model%20architecture.pn](The%20Transformer-model%20architecture.png)

- 아주 큰 틀에서 봤을 때는 왼쪽과 같은 seq2seq 구조
- 다음과 같은 알고리즘으로 진행
  0. 임베딩된 입력 데이터, 임베딩된 출력 데이터에 각각 positional encoding한 벡터를 합함
  1. 입력 임베딩은 6개의 encoder layer를 거친 뒤 그 출력을 각 decoder layer에 전달
  2. 출력 임베딩은 6개의 decoder layer를 거치며 layer를 거칠 때마다 encoder의 출력도 입력으로 받음
  3. 최종적으로 입력 데이터에 대한 출력 데이터의 확률 분포 도출

### Positional Encoding

- Transofmrer는 입력 받은 sequence에 대한 위치 정보를 모르기 때문에 상대적이든 절대적이든 위치에 대한 정보를 주입해야 함
- Transformer은 positional encoding으로써 임베딩 행렬의 차원 $d_{model}$ 에 대하여 다음과 같은 수식을 사용

$$
\begin{align}
PE_{(pos,2i)}=sin({pos\over10000^{{2i\over d_{model}}}})\\
PE_{(pos,2i+1)}=cos({pos\over10000^{{2i\over d_{model}}}})
\end{align}
$$

- 동일한 주기를 가지지만 짝수라면 sin 함수를, 홀수라면 cos 함수를 사용
  - positional encoding으로 주기함수를 사용한 이유에 대해 논문에서는 상대적 위치를 통해 attention이 가능하다는 것을 허용하고 매우 긴 sequence에 대해서도 유연성을 가지기 위함이라고 설명
  - 논문에서 이에 대한 내용을 자세히 설명하지 않으며 [해당 블로그 포스팅에서 설명을 잘하는 것 같아 링크로 대체](https://www.blossominkyung.com/deeplearning/transfomer-positional-encoding)
- 아래와 같은 그래프 형태로 나타남
![positional encoding graph.png](positional%20encoding%20graph.png)

![The Transformer-model%20architecture_numbering.png](The%20Transformer-model%20architecture_numbering.png)

### Encoder

- 왼쪽 그림의 왼쪽 부분(Inputs 이후에 진행되는 layer들)이 encoder
- encoder는 다음과 같은 알고리즘으로 진행
  1. 먼저 임베딩된 입력 값을 Q, K, V로 입력(Q, K, V는 모두 동일)
  2. 입력된 Q, K, V는 multi-head self attention layer를 거침
  3. 2의 결과와 원래의 입력을 더하여 layer normalization을 거치는 residual connection을 진행
  4. 3의 결과는 position-wise fully connected feed-forward network를 거침
  5. 4의 결과와 3의 결과를 더하여 layer normalization을 거치는 residual connection을 진행
  6. 1~5를 6번 반복한 후의 출력은 Decoder의 K와 V로 들어감
  
### Decoder

- 오른쪽 부분(Outputs 이후에 진행되는 layer들)이 decoder
- decoder는 다음과 같은 알고리즘으로 진행
  1. 먼저 임베딩된 입력 값을 Q, K, V로 입력(Q, K, V는 모두 동일)
  2. 입력된 Q, K, V는 masked multi-head self attention layer를 거침
  3. 2의 결과와 원래의 입력을 더하여 layer normalization을 거치는 residual connection을 진행
  4. 3의 결과는 Q가 되고 encoder의 출력을 K와 V로 하여 multi-head attention layer를 거침
  5. 4의 결과와 3의 결과를 더하여 layer normalization을 거치는 residual connection을 진행
  6. 5의 결과는 position-wise fully connected feed-forward network를 거침
  7. 6의 결과와 5의 결과를 더하여 layer normalization을 거치는 residual connection을 진행
  8. 1~7을 6번 반복한 후에 Linear와 Softmax layer를 거쳐 확률을 출력

### Attention

![(left) Scaled Dot-Product Attention. (right) Multi-Head Attention consists of several attention layers running in parallel.png]((left)%20Scaled%20Dot-Product%20Attention.%20(right)%20Multi-Head%20Attention%20consists%20of%20several%20attention%20layers%20running%20in%20parallel.png)

- Encoder 2, Decoder 2, Decoder 4에 해당하는 내용
- Attention layer는 다음과 같은 두 가지 방식으로 나뉨

#### Multi-Head Attention

- 입력을 Query, Key, Value인 3가지로 나눠서 입력
- 각각은 Linear layer를 거치며 hidden layer의 차원 수가 multi head 수로 나눈 차원 수로 축소됨
  - Transformer는 hidden layer의 차원 수가 512, multi head attention이 8개이기 때문에 Query, Key, Value의 차원 수가 모두 64로 축소됨
- 각각의 head에는 Q, K, V에 대한 가중치 행렬이 있고 입력 벡터에 가중치 행렬을 곱해 Q, K, V를 생성 및 업데이트
  - 이후 concat layer도 이 layer에 대한 가중치 행렬이 있고 업데이트 되며 다음과 같은 수식으로 표현

$$
MultiHead(Q,K,V)=Concat(head_1,\cdots,head_h)W^O\\
where\, head_i=Attention(QW_i^Q,KW_i^K,VW_i^V)\\
W_i^Q \in \mathbb{R}^{d_{model}\times d_k}, W_i^K \in \mathbb{R}^{d_{model}\times d_k},W_i^V \in \mathbb{R}^{d_{model}\times d_v}, W^O \in \mathbb{R}^{hd_v\times d_{model}}
$$

##### Encoder의 Multi-Head Self Attention

- Q, K, V 모두 encoder 내 이전 layer의 출력으로 각 토큰이 이전 layer의 모든 토큰을 참조할 수 있음

##### Decoder의 Masked Multi-Head Self Attention

- decoder는 Encoder의 Self Attention과 다르게 자기회귀라는 속성을 유지하기 위해선 토큰의 다음부터 끝에 해당하는 위치에 음의 무한대 혹은 0을 곱하는 masking out을 scaled dot-product attention의 softmax 함수를 거치기 전에 적용
  - 하삼각행렬의 곱셈은 닫혀있음

##### Encoder-Decoder의 Multi-Head Attention

- encoder의 self attention처럼 각 토큰이 모든 토큰을 참조할 수 있으면서 encoder와 decoder의 attention을 계산

#### Scaled Dot-Product Attention

- Scaled Dot-Product Attention에 해당하는 그림은 아래의 수식을 풀어 쓴 것
  - Mask(opt.)부분은 padding mask 등으로 인해 불필요한 부분을 0으로 처리하기 위해 사용
  - 각 attetion layer에 대해서 출력하는 hidden layer의 차원 수는 64

$$
Attention(Q,K,V)=softmax({QK^T\over\sqrt{d_k}})V
$$

- 모든 attention layer를 concatenation하면 출력하는 hideen layer의 차원 수는 512

### Residual Connection & Layer Normalization

- Encoder 3, Encoder 5, Decoder 3, Decoder 5, Decoder 7에 해당하는 내용
- $LayerNorm(x+Sublayer(x))$
  - 과적합을 막기 위해서 sub layer의 출력과 입력을 더하는 방식
    - sub layer는 Layer Norm을 적용하기 전의 출력된 layer로 Multi-Head Attention이나 Position-wise Feed-Forward Networks
    - ResNet이 이 방식을 사용한 대표적인 CNN
  - 이후 Layer Normalization을 적용
    - 기존에는 한 batch에서 각 feature에 대해 정규화를 적용하는 [[Batch Normalization]]을 많이 사용했음
      - 즉, 평균과 분산이 한 feature에 대하여 모든 데이터에 대해 계산됨
      - 그러나 RNN 계열 모델에서 시점마다 다른 데이터가 연속적으로 나온다는 점, batch의 기준이 모호하고 batch 크기에 의존적이라는 점에서 RNN 계열 모델에 부적합했음
    - Layer Normalization은 한 batch에서 각 data에 대해 정규화를 적용
      - 즉, 평균과 분산이 한 데이터에 대하여 모든 feature (hidden layer)에 대해 계산됨

### Position-wise Feed-Forward Networks

- Encoder 4, Decoder 6
- $FNN(x)=max(0,xW_1+b_1)W_2+b_2$
  - $xW_1+b_1$는 
  - max 함수는 ReLU에 해당함
  - x는 (seq, $d_{model}=512$), $W_1$은 $(d_{model}=512$, $d_{ff}=2048)$, $W_2$는 ($d_{ff}=2048$, $d_{model}=512$)

## 왜 self-attention인가?

### 1. 계산 복잡도 완화

![transformer%20table%201.png](transformer%20table%201.png)

- self attention layer가 RNN에 비해 모델 자체의 시간 복잡도가 작음, CNN은 k에 의해 RNN보다 비싸지만 separable convolution과 비교하면 경쟁력이 없음
  - 즉, sequence의 길이만 줄일 수 있다면 RNN, CNN보다도 짧은 시간에 끝낼 수 있으며 WordPiece, Byte-Pair 등의 SOTA 토큰화에서 많이 보이고 있음
  - 그러나 n을 줄이기 위해 시퀀스를 r만큼만 고려하는 것은 path length를 증가시키기 떄문에 향후 연구로 해결해야 할 과제

### 2. 병렬 연산

- O(1)을 병렬적으로 연산할 수 있음
  - 앞서 언급했듯이 RNN 계열이 병렬 연산이 불가능한 것을 해결

### 3. 장기 의존성

- 순전파와 역전파 신호가 통과할 네트워크의 길이가 짧을수록 장기 의존성을 학습하기 쉬워짐
- RNN은 n만큼의 연산을 진행해야만 의존성이 계산되지만 attention은 행렬연산으로써 의존성이 계산됨

### 4. Interpretability

- attention 분포를 통해 구문론적, 의미론적으로 해석 가능

## 훈련 세팅

### 데이터

- WMT 2014 영어-독어 450만 문장 쌍
  - byte-pair encoding으로 약 37K의 사전 구축
- WMT 2014 영어-불어 3600만 문장
  - 약 32K의 사전 구축

### 하드웨어

- NVIDIA P100 GPU 8개를 하나의 기계로 훈련
- 각 훈련 스텝 당 0.4초, 총 0.1M 스텝인 12시간 학습
  - 큰 모델은 스텝 당 1초, 총 0.3M 스텝인 3.5일 학습

### Optimizer

- Adam
  - $\beta_1=0.9$, $\beta_2=0.98$,$\epsilon=10^{-9}$
- 학습률은 아래와 같은 공식
  - warmup_steps는 4000
$$ lrate={1\over \sqrt {d_{model}}}min(step\_num^{-0.5},step\_num\cdot warmup\_steps^{-1.5}) $$

### Regularization

- Drop out은 0.1
  - sub layer의 출력에 drop out을 적용하고 Add & Layer Normalization을 진행
  - 또한 encoder와 decoder 모두에 전체적인 embedding을 진행한 이후 layer에 입력하기 전에 drop out을 적용
    - 토큰을 drop out 시킨다고 오해할 수 있으나 실제로는 vector 전체의 성분 중 drop out 비율만큼 탈락시킴
- label smoothing을 0.1로 적용
  - 다음과 같은 공식으로 이뤄지며 $\alpha$값이 0.1, K는 전체 클래스 수, $y_k$는 정답이면 1, 아니면 0

$$ y_k^{LS}=y_k(1-\alpha)+\alpha/K $$

## 코드

- Transformer의 output에 대한 입력은 shifted 되어 입력된다. ![자세한 것은 링크를 참조](https://github.com/sgrvinod/a-PyTorch-Tutorial-to-Transformers)

```python
import torch
from torch import nn
import torch.optim as optim

# Transformer 모델 정의
class TransformerModel(nn.Module):
    def __init__(self, input_dim, model_dim, num_heads, num_encoder_layers, num_decoder_layers, dim_feedforward, dropout):
        super(TransformerModel, self).__init__()
        self.transformer = nn.Transformer(
            d_model=model_dim,
            nhead=num_heads,
            num_encoder_layers=num_encoder_layers,
            num_decoder_layers=num_decoder_layers,
            dim_feedforward=dim_feedforward,
            dropout=dropout
        )
        self.input_embedding = nn.Embedding(input_dim, model_dim)
        self.output_embedding = nn.Embedding(input_dim, model_dim)
        self.fc_out = nn.Linear(model_dim, input_dim)
    
    def forward(self, src, tgt, src_mask=None, tgt_mask=None, src_key_padding_mask=None, tgt_key_padding_mask=None):
        src_emb = self.input_embedding(src)
        tgt_emb = self.output_embedding(tgt)
        memory = self.transformer.encoder(src_emb, src_mask, src_key_padding_mask)
        output = self.transformer.decoder(tgt_emb, memory, tgt_mask, None, tgt_key_padding_mask, None)
        output = self.fc_out(output)
        return output

# 입력 데이터 생성
src = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=torch.long)  # (batch_size, src_seq_len)
tgt = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.long)  # (batch_size, tgt_seq_len)

# 모델 초기화
input_dim = 10  # 단어 사전의 크기
model_dim = 512  # 모델 차원 수
num_heads = 8  # 멀티 헤드 어텐션의 헤드 수
num_encoder_layers = 6  # 인코더 레이어 수
num_decoder_layers = 6  # 디코더 레이어 수
dim_feedforward = 2048  # FFNN 차원 수
dropout = 0.1  # 드롭아웃 비율

model = TransformerModel(input_dim, model_dim, num_heads, num_encoder_layers, num_decoder_layers, dim_feedforward, dropout)

# 예측 수행
output = model(src, tgt)
print(output)
```
