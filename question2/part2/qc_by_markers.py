import matplotlib.pyplot as plt
from question1 import part3_driver_markers_statistics
from question2.part2 import plot, hardcoded_variables
import pandas as pd


def missing_data_by_marker_culmative(marker_df):
    successful_genotyped_series = marker_df[
        hardcoded_variables.FRACTION_FAILED_COL_NAME]
    plot_title = "Cumulative: Number of Markers by Fraction of Missing Data"
    plot_x_title = "Missing Data Fraction"
    plot_y_title = "\n\nCumulative\n n/nTotal"
    plot.create_plot_hist_cumulative_no_fixed_bins(
        successful_genotyped_series,
        plot_title, plot_x_title,
        plot_y_title)
    plt.show()


def missing_data_by_marker(marker_df):
    part3_driver_markers_statistics.single_var_stats(marker_df,
                                                     hardcoded_variables.FRACTION_FAILED_COL_NAME)
    missing_data_fraction_series = marker_df[
        hardcoded_variables.FRACTION_FAILED_COL_NAME]
    plot_title = "Number of Markers by Fraction of Missing Data"
    plot_x_title = "Missing Data Fraction"
    plot_y_title = "n"
    num_bins = 13
    plot.create_plot_hist_no_fixed_bins(missing_data_fraction_series,
                                        plot_title, plot_x_title, plot_y_title,
                                        num_bins)
    plt.show()


def heterozygous_data_by_marker(marker_df):
    part3_driver_markers_statistics.single_var_stats(marker_df,
                                                     hardcoded_variables.FRACTION_HETEROZYGOUS_COL_NAME)
    heterozygous_fraction_series = marker_df[
        hardcoded_variables.FRACTION_HETEROZYGOUS_COL_NAME]
    plot_title = "Number of Markers by Fraction of Heterozygous "
    plot_x_title = "Heterozygous Fraction"
    plot_y_title = "n"
    num_bins = 13
    plot.create_plot_hist_no_fixed_bins(heterozygous_fraction_series,
                                        plot_title, plot_x_title, plot_y_title,
                                        num_bins)

    plt.show()


def return_bad_markers_failed(df):
    filtered_failed_markers_df = df.loc[
        df[
            hardcoded_variables.FRACTION_FAILED_COL_NAME] > hardcoded_variables.MARKER_FRACTION_FAILED_FILTER]

    return filtered_failed_markers_df


def return_bad_markers_heterozygous(df):
    filtered_heterozygous_markers_df = df.loc[df[hardcoded_variables.FRACTION_HETEROZYGOUS_COL_NAME] >
                                              hardcoded_variables.MARKER_FRACTION_HETEROZYGOUS_FILTER]

    return filtered_heterozygous_markers_df


def return_bad_markers(marker_failed_df):
    filtered_failed = return_bad_markers_failed(marker_failed_df)
    filtered_heterozygous = return_bad_markers_heterozygous(marker_failed_df)
    bad_markers_df = pd.concat([filtered_failed, filtered_heterozygous])

    return bad_markers_df


def statistics_markers(marker_df):
    missing_data_by_marker(marker_df)
    # culmative graph does not offer any new insight
    # missing_data_by_marker_culmative(marker_df)

    heterozygous_data_by_marker(marker_df)
