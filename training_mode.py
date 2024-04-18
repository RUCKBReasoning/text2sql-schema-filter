from schema_filter import filter_func

# for the training mode, we can simulate the filter process based on sql
data = {
    "text": "What are the names of all directors whose movies have been reviewed by Sarah Martinez?",
    "sql": "SELECT DISTINCT movie.director FROM rating JOIN movie ON rating.mid  =  movie.mid JOIN reviewer ON rating.rid  =  reviewer.rid WHERE reviewer.name  =  'Sarah Martinez'",
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

def find_used_tables_and_columns(dataset):
    for data in dataset:
        sql = data["sql"].lower()
        data["table_labels"] = []
        data["column_labels"] = []
        
        for table_info in data["schema"]["schema_items"]:
            table_name = table_info["table_name"]
            data["table_labels"].append(1 if table_name.lower() in sql else 0)
            data["column_labels"].append([1 if column_name.lower() in sql else 0 \
                for column_name in table_info["column_names"]])
    return dataset

dataset = [data]

dataset = find_used_tables_and_columns(dataset)

# remain up to 3 relavant tables in the database
num_top_k_tables = 3
# remain up to 3 relavant columns for each remained table
num_top_k_columns = 3

dataset = filter_func(
    dataset = dataset, 
    dataset_type = "train",
    sic = None,
    num_top_k_tables = num_top_k_tables,
    num_top_k_columns = num_top_k_columns
)

print(dataset)