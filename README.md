# Schema Filter for Text-to-SQL

Introducing our advanced Schema Filter, a bilingual (English and Chinese) model with 3 billion parameters, designed to enhance Text-to-SQL projects. This tool expertly identifies the most relevant database schemas—tables and columns—based on natural language queries.

## Why Use a Schema Filter?

1. **Database Complexity**: Ideal for databases with a vast array of tables and columns. Integrating a schema filter with your large language model (LLM) can reduce the context length of the database schema.
2. **Performance Enhancement**: Aids your text-to-SQL model by filtering out irrelevant schemas, reducing the load on LLM for schema linking tasks.

## Architecture Overview

The schema filter's architecture follows the cross-encoder design from [RESDSQL](https://arxiv.org/abs/2302.05965), with enhancements from our work in [CodeS](https://arxiv.org/abs/2402.16347) for ease of use. Originally based on RoBERTa-Large, we've upgraded to XLM-RoBERTa-XL for its 3.5 billion parameters and bilingual support, making it more suited for the schema-linking challenges.

## Training Data

We fine-tuned this schema filter using training sets from Spider, BIRD, and CSpider, ensuring a robust and versatile schema filter capable of handling diverse queries.

## Hardware Requirements

The schema filter's extensive parameter count (3.5 billion) necessitates at least 15GB of memory (GPU or CPU) for inference.

## Getting Started

1. **Clone Project**: Clone or download this project.
2. **Model Download**: Acquire our fine-tuned model `sic_merged.zip` from [quark netdisk](https://pan.quark.cn/s/418c417127ae) or [google drive](https://drive.google.com/file/d/1xzNvv5h-ZjhjOOZ-ePv1xg_n3YbUNLWi/view?usp=sharing) and then unzip it in the root of this project.
3. **Usage Examples**: Consult `eval_mode.py` for running the model without SQL input, predicting relevance scores for tables and columns based on queries using the trained model. Use `training_mode.py` for a guided experience with ground-truth SQL, simulating the schema filtering process.

To integrate the schema filter into your text-to-SQL system properly, your data needs to be organized as follows:

- `text`: The natural language question.
- `sql`: The corresponding SQL query; this can be left as an empty string when in evaluation mode.
- `schema`: The structure detailing the database schema.
- `schema.schema_items.table_name`: The name of the table in the database.
- `schema.schema_items.table_comment`: A descriptive comment for the table, which is necessary if the table name is not self-explanatory. Otherwise, this can be left as an empty string.
- `schema.schema_items.column_names`: The names of the columns in the table.
- `schema.schema_items.column_comments`: A descriptive comment for each column, is required only if the column name could be confusing. If clarity is not an issue, this can also be an empty string.

Here is an example of how your data should be formatted:

```json
{
    "text": "List the names of directors whose films have received reviews from Sarah Martinez.",
    "sql": "SELECT DISTINCT movie.director FROM rating JOIN movie ON rating.mid = movie.mid JOIN reviewer ON rating.rid = reviewer.rid WHERE reviewer.name = 'Sarah Martinez'",
    "schema": {
        "schema_items": [
            {
                "table_name": "movie",
                "table_comment": "",
                "column_names": ["mid", "title", "year", "director"],
                "column_comments": ["movie id", "", "", ""]
            },
            ...
        ]
    }
}
```

In the provided example scripts, you can adjust the `num_top_k_tables` and `num_top_k_columns` parameters. These define the number of tables and columns, respectively, that will be retained after schema filtering.

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
