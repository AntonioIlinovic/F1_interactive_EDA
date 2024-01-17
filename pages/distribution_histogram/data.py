from common.utils.utils import DatasetName, load_dataset


def get_data_for_histogram_distribution(dataset_name):
    """
    Function returns data for histogram distribution and hover data.
    :param dataset_name:
    :return:
    """
    distribution_data = load_dataset(dataset_name)
    return distribution_data, distribution_data.columns
