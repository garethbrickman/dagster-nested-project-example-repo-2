from dagster import asset

@asset
def my_asset():
    return 5
