import pandas as pd
from question1.tamu_io import constants
import numpy as np
import matplotlib.pyplot as plt


def fill_sample_combination_col_df(df):
    columns = list(df)

    ans_Df = pd.DataFrame()

    for idx, col in enumerate(columns):
        for idx2, col2 in enumerate(columns[1+idx:]):
            ans_Df[col + ',' + col2] = np.where(
                (df[col].isin(constants.VALID_CHARS)) & (
                    df[col2].isin(constants.VALID_CHARS))
                , 1, 0)

    return ans_Df


def count_shared_markers_for_each_2_col(df, columns):
    fina_df = pd.DataFrame(columns=columns,
                           index=columns)
    for column in df:
        col1, col2 = column.split(",")
        count = df.groupby(column).size()
        fina_df[col1][col2] = count[1]
        fina_df[col2][col1] = count[1]

    return fina_df


def _write_output_csv_file(output_towrite):
    df = pd.DataFrame(data=output_towrite)
    df.to_csv("output/part3/sim_matrix.csv", sep=',', header=False,
              index=False)


# create new dataframe with combination of every 2 sample as columns
# each row represent one marker as in the original csv input data file
# for every marker ( row) fill a cell with 1 if the 2 samples combination
# represented by the column have valid char read on the marker
def create_sim_matrix(dataframe):

    samples_columns = list(dataframe)
    ans_df = fill_sample_combination_col_df(dataframe)

    sim_matrix_df = count_shared_markers_for_each_2_col(ans_df,samples_columns)
    # 2 metadata rows to remove
    markers_nmber = len(dataframe.index) - 2
    sim_matrix_df_div = sim_matrix_df/markers_nmber
    np.fill_diagonal(sim_matrix_df_div.values, 1)
    _write_output_csv_file(sim_matrix_df_div)

    # corr_df = sim_matrix_df.corr()
    # print(corr_df)
    # plt.matshow(corr_df)
    # plt.show()






