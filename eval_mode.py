from schema_filter import filter_func, SchemaItemClassifierInference

# in the eval mode, you do not need to provide sql, 
# the relevant scores of tables and columns are predicted by the fine-tuned schema filter model based on the user's text (or question)
data = {
    "text": "What are the names of all directors whose movies have been reviewed by Sarah Martinez?",
    "sql": "",
    "schema": {
        "schema_items": [
            {
                "table_name": "movie",
                "table_comment": "",
                "column_names": [
                    "mid",
                    "title",
                    "year",
                    "director"
                ],
                "column_comments": [
                    "movie id",
                    "",
                    "",
                    ""
                ]
            },
            {
                "table_name": "reviewer",
                "table_comment": "",
                "column_names": [
                    "rid",
                    "name"
                ],
                "column_comments": [
                    "reviewer id",
                    ""
                ]
            },
            {
                "table_name": "rating",
                "table_comment": "",
                "column_names": [
                    "rid",
                    "mid",
                    "stars",
                    "ratingdate"
                ],
                "column_comments": [
                    "reviewer id",
                    "movie id",
                    "rating stars",
                    ""
                ]
            }
        ]
    }
}

dataset = [data]

# remain up to 3 relavant tables in the database
num_top_k_tables = 3
# remain up to 3 relavant columns for each remained table
num_top_k_columns = 3

# load fine-tuned schema filter
sic = SchemaItemClassifierInference("sic_merged")

dataset = filter_func(
    dataset = dataset, 
    dataset_type = "eval",
    sic = sic,
    num_top_k_tables = num_top_k_tables,
    num_top_k_columns = num_top_k_columns
)

print(dataset)