import matplotlib.pyplot as plt
import pandas as pd
from question1 import part3_driver_markers_statistics
from question2.part2 import plot,hardcoded_variables


def missing_data_by_sample(samples_df):
    new_col_name = 'miss_data_by_sample'
    samples_df[new_col_name] = (1 - samples_df[hardcoded_variables.SUCCESS_MARKERS_COL_NAME])
    part3_driver_markers_statistics.single_var_stats(samples_df,
                                                     new_col_name)
    successful_genotyped_series = samples_df[new_col_name]
    plot_title = "Number of Samples  by Fraction of Missing Data"
    plot_x_title = "Missing Data Fraction"
    plot_y_title = "n"
    num_bins = 8
    plot.create_plot_hist_no_fixed_bins(successful_genotyped_series,
                                        plot_title, plot_x_title, plot_y_title,
                                        num_bins)
    plt.show()
    plot_title = "Cumulative: Samples Number by Fraction of Missing Data"
    plot_x_title = "Missing Data Fraction"
    plot_y_title = "\n\nCumulative\n n/nTotal"
    plot.create_plot_hist_cumulative_no_fixed_bins(successful_genotyped_series,
                                                   plot_title, plot_x_title,
                                                   plot_y_title)
    plt.show()


def sucessful_markers_by_sample(samples_df):
    part3_driver_markers_statistics.single_var_stats(samples_df,
                                                     hardcoded_variables.SUCCESS_MARKERS_COL_NAME)
    successful_genotyped_series = samples_df[hardcoded_variables.SUCCESS_MARKERS_COL_NAME]
    plot_title = "Number of Samples by Fraction of Successful Markers"
    plot_x_title = "Successful Marker Fraction"
    plot_y_title = "n"
    num_bins = 8
    plot.create_plot_hist_no_fixed_bins(successful_genotyped_series,
                                        plot_title, plot_x_title, plot_y_title,
                                        num_bins)
    plt.show()
    plot_title = "Cumulative: Number of Samples by Fraction of Successful Markers"
    plot_x_title = "Successful Marker Fraction"
    plot_y_title = "\n\nCumulative\n n/nTotal"
    plot.create_plot_hist_cumulative_no_fixed_bins(successful_genotyped_series,
                                                   plot_title, plot_x_title,
                                                   plot_y_title)
    plt.show()


def heterozygous_markers_by_sample(samples_df):
    part3_driver_markers_statistics.single_var_stats(samples_df,
                                                     hardcoded_variables.HETEROZYGOUS_MARKERS_COL_NAME)

    heterozygout_markers_series = samples_df[hardcoded_variables.HETEROZYGOUS_MARKERS_COL_NAME]
    plot_title = "Number of Samples by Fraction of Heterozygous Markers"
    plot_x_title = "Heterozygous Marker Fraction"
    plot_y_title = "n"
    num_bins = 10
    plot.create_plot_hist_no_fixed_bins(heterozygout_markers_series, plot_title
                                        , plot_x_title, plot_y_title, num_bins)
    plt.show()


def return_bad_samples_failed(samples_df):
    filtered_sample_df = samples_df.loc[
        samples_df[hardcoded_variables.SAMPLES_SUCCESS_MARKERS_COL_NAME] <
        hardcoded_variables.SAMPLES_FRACTION_SUCCESS_MARKERS_FILTER]
    return filtered_sample_df


def return_bad_samples_heterozygous(df):
    filtered_heterozygous_samples_df = df.loc[df[hardcoded_variables.SAMPLES_HETEROZYGOUS_COL_NAME] >
                                              hardcoded_variables.SAMPLES_FRACTION_HETEROZYGOUS_FILTER]
    return filtered_heterozygous_samples_df

#
# def return_unfiltered_samples(samples_df):
#     filtered_sample_df = samples_df.loc[
#         samples_df[
#             hardcoded_variables.SUCCESS_MARKERS_COL_NAME] >= hardcoded_variables.SAMPLES_FRACTION_SUCCESS_MARKERS_FILTER]
#     return filtered_sample_df
#

def report_filtered_samples(filtered_samples_df):
    df = filtered_samples_df.sort_values(by=[hardcoded_variables.SAMPLES_SUCCESS_MARKERS_COL_NAME])
    df.to_csv("./output/part2/filtered_samples.csv", sep=',', header=True,
              index=False)


def return_bad_samples(filtered_samples_df):
    filtered_failed = return_bad_samples_failed(filtered_samples_df)
    filtered_heterozygous = return_bad_samples_heterozygous(filtered_samples_df)
    bad_samples_df = pd.concat([filtered_failed, filtered_heterozygous ])

    return bad_samples_df
