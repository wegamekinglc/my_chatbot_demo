# RASA NLU Engine for Customer Service Chatbot

## Prerequisite

* Python package dependency

```bash
$ pip install requirements.txt
```

* Pre-trained MITIE Wordrep model

```bash
Link：https://pan.baidu.com/s/1kNENvlHLYWZIddmtWJ7Pdg
Pwd ：p4vx
```
and the downloaded `total_word_feature_extractor_chi.dat` should be placed under the folder `./models`.

## Training Model

* Data preparation

```bash
$ cd ./utilities
$ python prepare_data.py
```

* Training

under the project root folder:

```bash
$ rasa train nlu --nlu data/customer_service.json
```
if everything is ok, the model should be placed as:

```bash
./models/nlu-yyyymmdd-xxxxxx.tar.gz
```

## Run the NLU Robot

* Shell/Command line

You can try out the robot directly from shell:
```bash
$ rasa shell nlu
2019-07-30 19:09:12 INFO     rasa.nlu.components  - Added 'MitieNLP' to component cache. Key 'MitieNLP-D:\dev\github\my_chatbot_demo\models\total_word_feature_extractor_zh.dat'.
2019-07-30 19:09:12 INFO     rasa.nlu.tokenizers.jieba_tokenizer  - Loading Jieba User Dictionary at C:\Users\wegam\AppData\Local\Temp\tmpvg25w9n7\nlu\component_1_JiebaTokenizer\jieba_userdict.txt
Building prefix dict from the default dictionary ...
Loading model from cache C:\Users\wegam\AppData\Local\Temp\jieba.cache
Loading model cost 0.765 seconds.
Prefix dict has been built succesfully.
NLU model loaded. Type a message and press enter to parse it.
Next message:
```
Now in the terminal you can type in any sentence you want to check the meaning, e.g.:
```
Next message: 你好
```

the returning message will look like these:
```bash
{
  "intent": {
    "name": "greet",
    "confidence": 0.9850282806343889
  },
  "entities": [],
  "intent_ranking": [
    {
      "name": "greet",
      "confidence": 0.9850282806343889
    },
    {
      "name": "general",
      "confidence": 0.01167282607058015
    },
    {
      "name": "introduction",
      "confidence": 0.0019278976271873416
    },
    {
      "name": "malfunction",
      "confidence": 0.0009351545539076577
    },
    {
      "name": "accessories",
      "confidence": 0.00036510564792836413
    },
    {
      "name": "function",
      "confidence": 7.073546600757265e-05
    }
  ],
  "text": "你好"
}
```

* Python

There are some examples directly run in python scripts. They are under `examples` and can be run as, e.g.:
```bash
$ python examples/1. example_101.py
```
