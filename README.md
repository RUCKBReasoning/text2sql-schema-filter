# Schema Filter for Text-to-SQL

Introducing our advanced Schema Filter, a bilingual (English and Chinese) model with 3 billion parameters, designed to enhance Text-to-SQL projects. This tool expertly identifies the most relevant database schemas—tables and columns—based on natural language queries.

## Why Use a Schema Filter?

1. **Database Complexity**: Ideal for databases with a vast array of tables and columns. Integrating a schema filter with your large language model (LLM) can reduce the context length of the database schema.
2. **Performance Enhancement**: Aids your text-to-SQL model by filtering out irrelevant schemas, reducing the load on LLM for schema linking tasks.

## Architecture Overview

The schema filter's architecture follows the cross-encoder design from [RESDSQL](https://arxiv.org/abs/2302.05965), with enhancements from our work in [CodeS](https://arxiv.org/abs/2402.16347) for ease of use. Originally based on RoBERTa-Large, we've upgraded to XLM-RoBERTa-XL for its 3.5 billion parameters and bilingual support, making it more suited for the schema-linking challenges.

## Training Data

We fine-tuned this schema filter using datasets from Spider, BIRD, and CSpider, ensuring a robust and versatile schema filter capable of handling diverse queries.

## Hardware Requirements

The schema filter's extensive parameter count (3.5 billion) necessitates at least 15GB of memory (GPU or CPU) for inference.

## Getting Started

1. **Model Download**: Acquire our fine-tuned model [here](https://pan.quark.cn/s/105f37342be1) and unzip it.
2. **Usage Examples**: Consult `eval_mode.py` for running the model without SQL input, predicting relevance scores for tables and columns based on queries using the trained model. Use `training_mode.py` for a guided experience with ground-truth SQL, simulating the schema filtering process.

This schema filter is a powerful addition to any text-to-SQL project, streamlining the process of linking natural language queries to the correct database schemas.

## Citation
If this project assists you, kindly reference the following paper:
```
@inproceedings{li2022resdsql,
  author = {Haoyang Li and Jing Zhang and Cuiping Li and Hong Chen},
  title = "RESDSQL: Decoupling Schema Linking and Skeleton Parsing for Text-to-SQL",
  booktitle = "AAAI",
  year = "2023"
}

@inproceedings{li2024codes,
  author = {Haoyang Li and Jing Zhang and Hanbing Liu and Ju Fan and Xiaokang Zhang and Jun Zhu and Renjie Wei and Hongyan Pan and Cuiping Li and Hong Chen},
  title = "CodeS: Towards Building Open-source Language Models for Text-to-SQL",
  booktitle = "SIGMOD",
  year = "2024"
}
```