



将 API 序列映射到目标API序列摘要
- API encoder 用rnn 模型去读这个API 序列 

采用经典的注意力机制：

 The hidden s-tate of the encoder is updated according to the API and theprevious hidden state

 通过考虑先前的隐藏状态h t-1，将源语言的单词映射为隐藏状态h t。

encoder：
上一个状态+ 此时新进来的一个单词 变成下一个状态。

decoder:
预测$dt$使用上下文的vector和过去预测过的单词 d1 到 d t-1 
也等于 g(d t-1, s t, C t)
