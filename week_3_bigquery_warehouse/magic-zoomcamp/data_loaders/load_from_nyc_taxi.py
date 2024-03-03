import pyarrow.parquet as pq
from io import BytesIO
import requests

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """

    month = kwargs['month']

    source_url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-{month}.parquet"
    # Download the file using requests
    response = requests.get(source_url)
    parquet_file = BytesIO(response.content)

    # Read the Parquet file from the downloaded content
    table = pq.read_table(parquet_file)

    # Convert the table to a Pandas DataFrame if needed
    df = table.to_pandas()

    # Now you can work with the DataFrame or the Arrow table as needed
    return df

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
