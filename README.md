# bleu4 和 Rouge

### bleu4

Bleu源于文章BLEU: a Method for Automatic Evaluation of Machine Translation，Bleu4是最大n-gram取4时候的值。

此代码集成了几种常用的bleu4计算方法，包括：CodeBert BLEU, Google BLEU, nltk BLEU组件以及文章《A Transformer-based Approach for Source Code Summarization》（以下简称tbcs）中的bleu实现方法。

tbcs-bleu的代码源自于https://github.com/wasiahmad/NeuralCodeSum ，是文章《A Transformer-based Approach for Source Code Summarization》的代码

### Rouge

Rouge源于文章：ROUGE: A Package for Automatic Evaluation of Summaries.

此代码集成了TbCS的rouge计算代码以及python rouge库的计算。

## 运行方法
 `python eval.py reference_file_path hypothesis_file_path` 
