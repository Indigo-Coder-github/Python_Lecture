# 1. 통계적 언어처리

## One-Hot Encoding

## Bag of Words(BoW)

## Term Frequency

- BoW가 이진방식이 아닌 단어의 빈도로 접근했음에도 문서나 corpus 내 단어들의 중요도를 고려하지 못했다는 한계
  - 한 단어가 특정 문서에 관련이 있는지를 알아낸다면 corpus에서 중요성을 가질 것임
- 그 연관성이라는 것이 corpus와 개별 문서 내 쿼리 키워드의 발생에 근거할 수 있음
- Term Frequency는 문서 내 단어의 빈도를 계산
  - 단순히 세는 것은 잘못된 결과를 줄 수 있음
    - 예를 들어 문서 A가 150 단어, B가 백만 단어인데 house라는 단어가 A에서는 50번, B에서는 1000번 나타났다면 B보단 A에서 더 중요한 단어일 것 같지만 단순히 세기만 했다면 A에서 더 중요할 것이라고 착각
  - 그래서 일반적으로 문서의 전체 단어 수로 나눈 Normalized 버전이 주로 사용됨
- 문서-단어 행렬에서 행은 문장이나 단어를, 열은 고유 단어를 나타내며 각 값은 Normalized Term Frequency로 문서에서 중요도로 계산됨
  - 문서와 쿼리 간, 문서 간 유사도를 계산(코사인 유사도 등)이 가능해짐

### Cosine Similarity

- 두 문서 벡터를 x, y라고 했을 때
$$cos(x,y)= {xy\over||x||||y||}={\sum xy \over \sqrt {\sum x^2} \sqrt {\sum y^2}}$$
- 1일수록 가까우며 각도가 작고 길이나 양에 무관하게 문서 간 유사한 단어를 사용하고 비슷한 내용임을 암시
  - 그러나 0이라고 해서 완전히 내용이 다른 것을 의미하지 않음
  - 같은 주제라도 다른 단어 집합을 사용했을 수도 있기 때문
  - 이런 문제접점은 단어의 의미론을 파악하는 것으로 word embedding 벡터 등에서 해결됨
- 빈도 계산은 독립적으로 고려된다는 점, 유사도가 증가하려면 비슷한 비율로 정확히 같은 단어가 발생해야 한다는 점은 이전의 접근법들과 다를 바 없어서 단어의 의미론적 측면을 고려하는데 실패(유사어, 반의어, 추론 등)
  - BoW나 One-Hot Encoding에 비해 문서 내 단어들의 상대적 중요도를 더 찾을 뿐임

### 코드

```python
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

example_docs = ["동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세 무궁화 삼천리 화려강산 대한사람 대한으로 길이 보전하세",
                "남산위에 저 소나무 철갑을 두른 듯 바람서리 불변함은 우리 기상일세 무궁화 삼천리 화려강산 대한사람 대한으로 길이 보전하세",
                "가을하늘 공활한데 높고 구름 없이 밝은 달은 우리 가슴 일편단심일세 무궁화 삼천리 화려강산 대한사람 대한으로 길이 보전하세",
                "이 기상과 이 맘으로 충성을 다하여 괴로우나 즐거우나 나라 사랑하세 무궁화 삼천리 화려강산 대한사람 대한으로 길이 보전하세"]

vectorizer = CountVectorizer(lowercase=True, preprocessor=None, tokenizer=None,
                             stop_words=None,token_pattern='(?u)\\b\\w+\\b', ngram_range=(1, 1),
                            min_df=1, max_df=1.0, max_features=None,
                            vocabulary=None, binary=False)

dtm = vectorizer.fit_transform(example_docs)
print(dtm.toarray())
print(vectorizer.inverse_transform(dtm))
print(vectorizer.get_feature_names_out(), vectorizer.vocabulary_)

preprocessed_example_docs = ["동해물 과 백두산 이 마르 고 닳 도록 하느님 이 보우 하 사 우리나라 만세 무궁화 삼천 리 화려강산 대한 사람 대한 으로 길이 보전 하 세",
                "남산 위 에 저 소나무 철갑 을 두 른 듯 바람서리 불변 함 은 우리 기상 일세 무궁화 삼천 리 화려강산 대한 사람 대한 으로 길이 보전 하 세",
                "가을 하늘 공활 한 데 높 고 구름 없 이 밝 은 달 은 우리 가슴 일편단심 일세 무궁화 삼천 리 화려강산 대한 사람 대한 으로 길이 보전 하 세",
                "이 기상 과 이 맘 으로 충성 을 다 하 여 괴로 우 나 즐거 우 나 나라 사랑 하세 무궁화 삼천리 화려강산 대한 사람 대한 으로 길이 보전 하 세"]
vectorizer = CountVectorizer()
dtm = pd.DataFrame(data=dtm.vectorizer.fit_transform(preprocessed_example_docs),
                   columns=vectorizer.get_feature_names_out())
for row in df.itertuples(index=False):
    for row_index in range(len(row)):
        if row[row_index] > 0: print(f"{df.columns[row_index]}:{row[row_index]}")
```

## Term Frequency Inverse Document Frequency(TF-IDF)

- Normalized Term Frequency가 문서 내 단어들의 상대적 중요도를 나타낼 뿐이지 한 단어가 각 문서에서 어느 정도의 중요도를 나타내는지는 알 수 없음
  - 더하여 일반적인 단어들이 문서 상에 많이 나타나기 때문에 Normalized Term Frequency는 전부 높은 유사도 점수를 나타낼 것이고 군집화할 것임
- Inverse Document Frequency(IDF)는 특정 집합에 속한 문서들의 고유한 단어들(토픽이나 개념)에 중요도나 가중치를 줘서 문서를 쉽게 구분하고 분류하도록 함
  - 군집화하려는 문서에 고유하지 않은 단어를 고려할 때 유사도 점수에 간접적으로 패널티를 주는 방식
$$IDF_i=log{N\over df_i}$$
- corpus 내 문서들의 전체 수의에 대한 단어가 나타나는 문서들의 수의 비율
  - N은 corpus 내 전체 문서의 수, $df_i$는 단어 $t_i$를 포함하는 문서의 수
- IDF는 Normalized Term Frequency와 다르게 corpus에서 자주 발생하고 고유하지 않은 유사한 단어를 벡터 간 공유한다면 유사도가 감소
- i번째 단어에 대한 j번째 문서의 TF-IDF는 다음과 같음
  - sklearn에서는 zero division 문제와 log의 0이 정의되지 않는 것을 위해 1을 더함
$$ tf_{i,j}idf_i=tf_{i,j}(log{1+N\over1+df_i}) $$
- TF-IDF는 한 문서 내 한 단어의 중요를 corpus 내 나머지 문서와의 상대적 중요도를 알려줌
  - 문서 벡터를 분류하고 주목하는데 중요한 단어 가중치를 암묵적으로 임베딩하고 업스케일링하며 이를 통해 문서 내 토픽과 개념을 밝힐 수 있음
    - 즉, 문서에서 중요한 단어를 집중과 선택하여 corpus의 문서들을 구분하는데 도움을 줄 수 있음
  - 정보 검색, 텍스트 분류 등에서 응용됨
- 이전의 접근법들보다 정확도가 상승했지만 다음과 같은 문제점
  - 고차원 희소행렬 및 이로 인한 차원 축소 필요
  - 유의어인데 글자가 달라 벡터 공간에서 서로 가깝지 않은 벡터일 수 있음 혹은 서로 가까운 벡터가 비슷한 의미가 아닐 수 있음
- 상기한 문제점 때문에 Okapi BM25 등의 SOTA TF-IDF 방식일지라도 유의어를 연결하거나 반의어를 떨어트리는데 실패할 수도 있음
  - Okapi BM25는 rank-bm25라는 라이브러리를 통해 제공하고 있으며 아래와 같은 수식
    - $f(q_i,D)$는 문서 D에 있는 단어 $q_i$의 빈도, $|D|$는 문서 D의 길이, $avgdl$은 문서들의 평균 길이
    - $k_1$과 $b$는 하이퍼파라미터로 각각 $[1.2, 2.0]$, $0.75$로 선택됨
    - $n(q_i)$는 단어 $q_i$가 포함된 문서의 수, $N$은 전체 문서 수

$$ score(D,Q)=\sum_{i=1}^n  ln({N-n(q_i)+0.5\over n(q_i)+0.5}+1)({f(q_i,D)(k_1+1)\over f(q_i,D)+k_1(1-b+b{|D|\over avgdl})})$$

### 코드

- CountVectorizer를 적용한 행렬을 TfidfTransoformer에 넣은 결과와 TfidfVectorizer를 적용한 결과는 동치

```python
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
# 위 CountVectorizer 코드에서 인스턴스 생성부분만 바꾸면 똑같이 작동
```

# Latent Dirichlet Allocation (LDA)

- [[A Survey of Text Representation and Embedding Techniques in NLP|논문]]에서는 Feature Trasformation 방법으로 나오고 있음
- 기본적인 가정은 문서는 하나 이상의 숨겨진 토픽에 대해 랜덤한 혼합으로 표현되며 각 토픽은 단어들에 대한 분포로 특징됨
  - 알고리즘은 문서 내 토픽들의 가중치나 확률들과 한 토픽 내 단어들의 가중치들은 디리클레 확률 분포를 따른다는 가정에서 출발

## 용어 정의

- 단어는 사전 $\{1,\cdots, V\}$에 있으며 one-hot encoding 방식으로 벡터화됨
- 문서는 N개의 단어가 시퀀스를 이루는 $w=(w_1, \cdots, w_n)$
- corpus는 문서 M개의 집합인 $D=\{w_1, \cdots, w_M\}$

## 수식

- corpus D에 대하여 각 문서 w에 대한 생성과정은 아래를 따름
  1. $N\sim Poisson(\xi)$
  2. $\theta \sim Dir(\alpha)$
  3. 각 문서 N은 다음과 같이 구성됨
    3.1. 토픽 $z_n \sim Multinomial(\theta)$
    3.2. 단어 $w_n$은 토픽 $z_n$에 대한 조건부 다항분포 확률인 $p(w_n|z_n,\beta)$
- 다음과 같은 가정이 내포되어 있음
  1. 디리클레 분포의 차원 k(토픽 변수 z의 차원 수)는 알려져 있고 고정된 수
  2. 단어 분포는 $k \times V$ 차원의 행렬 $\beta$로 나타나며 $\beta_{ij}=p(w^j=1|z^i=1)$로 고정됨
  3. 푸아송 분포는 그다지 중요하지 않으며 현실적으로 문서 길이 분포 등이 더 필요할 수도 있음
    3.1. 또한 N은 변수를 생성하는 다른 모든 데이터와는 독립적($\theta, z$)

![LDA](A%20Survey%20of%20Topic%20Models%20in%20Text%20Classification%20fig%202.png)

### 다항분포/디리클레 분포

- 다항분포는 가능한 모든 경우의 수 k와 각각에 대한 확률 $p_k$에 대해 n번의 시행에서 i번째 값이 $x_i$번 나타날 확률밀도

$$p(x_1,\cdots,x_k;n,p_1,\cdots,p_k)={n!\over \prod_i x_i!}\prod_i p^{x_i}$$

- 디리클레분포는 모든 요소가 양수이고 그 합이 1인 실수 벡터에 대해 다음과 같이 정의

$$f(x_1,\cdots,x_k;\alpha_1,\cdots,\alpha_k)={1\over B(\alpha)}\prod_ix_i^{\alpha_i-1}$$
$$B(\alpha)={\prod_i\Gamma(\alpha_i)\over \Gamma(\sum\alpha_i)}$$

### 코드

```python
from gensim.models import LdaModel
from gensim.corpora.dictionary import Dictionary
from sklearn.decomposition import LatentDirichletAllocation
import tomotopy as tp

example_docs = ["동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세 무궁화 삼천리 화려강산 대한사람 대한으로 길이 보전하세",
                "남산위에 저 소나무 철갑을 두른 듯 바람서리 불변함은 우리 기상일세 무궁화 삼천리 화려강산 대한사람 대한으로 길이 보전하세",
                "가을하늘 공활한데 높고 구름 없이 밝은 달은 우리 가슴 일편단심일세 무궁화 삼천리 화려강산 대한사람 대한으로 길이 보전하세",
                "이 기상과 이 맘으로 충성을 다하여 괴로우나 즐거우나 나라 사랑하세 무궁화 삼천리 화려강산 대한사람 대한으로 길이 보전하세"]

num_topics = 5
example_docs = [i.split() for i in example_docs]

#tomotopy
tomotopy_lda = tp.LDAModel(k=num_topics)
for document in example_docs:
    tomotopy_lda.add_doc(document)
tomotopy_lda.train()
print(tomotopy_lda.get_topic_words(num_topics-1))

#gensim
dic = Dictionary(example_docs)
corpus = dic.doc2bow()
gensim_model = LdaModel(corpus=corpus, id2word=dic, num_topics=num_topics)
print(gensim_model.print_topics(num_words=5))

#sklearn
sklearn_model = LatentDirichletAllocation(num_topics)
sklearn_model.fit_transform(X) #X는 CountVectorizer나 TfidfTransformer 등을 적용한 DTM
```
