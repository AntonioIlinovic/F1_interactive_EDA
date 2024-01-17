from common.utils.utils import DatasetName, load_dataset
import plotly.express as px


def get_histogram_distribution(dataset_name: DatasetName, column_name: str):
    """
    This function will return a histogram distribution for a given dataset and column name.
    :param dataset_name: dataset name. It will load necessary dataframe using this parameter
    :param column_name: of a column in the dataset
    :return:
    """
    df = load_dataset(dataset_name)
    fig = px.histogram(df, x=column_name, marginal='box', hover_data=df.columns)
    return fig
