
from question2 import read_data
from question2.part2 import qc_by_markers, qc_by_samples ,hardcoded_variables, report_bad_markers
import pandas as pd

from question2.part2.qc_by_samples import sucessful_markers_by_sample, \
    return_bad_samples, report_filtered_samples, return_unfiltered_samples


def qc_by_markers_main_function(marker_failed_df):
    qc_by_markers.statistics_markers(marker_failed_df)
    filtered_markers_df = qc_by_markers.return_bad_markers(marker_failed_df)
    report_bad_markers.report_filtered_markers(filtered_markers_df)

    #clean_good_samples_df = return_unfiltered_samples(samples_df)



def get_marker_fractions(marker_col, trans_df):
    marker_series = trans_df[marker_col]
    value_count = marker_series.value_counts()
    (dna_nuc_count, biallelic_nuc_count,
     failed_count) = read_data.parse_allele_freq_value_count(value_count)
    total_results = dna_nuc_count + biallelic_nuc_count + failed_count
    total_successfully_genotyped = dna_nuc_count + biallelic_nuc_count

    if total_successfully_genotyped is 0:
        fraction_heterozygous = 0
    else:
        fraction_heterozygous = biallelic_nuc_count / total_successfully_genotyped

    fraction_failed = round(failed_count / total_results,3)

    return fraction_failed, fraction_heterozygous



def _create_marker_failed_heterozygous_freq_df(samples_df):
    trans_df = samples_df.transpose()
    list_to_df = []
    # Skipping Entry and designation col by [2:]
    for col in trans_df.columns[2:]:
        marker_name = col
        fraction_failed, fraction_heterozygous = get_marker_fractions(col, trans_df)
        list_to_df.append([marker_name, fraction_failed, fraction_heterozygous  ])

    marker_failed_df = pd.DataFrame(list_to_df, columns=['Marker', hardcoded_variables.FRACTION_FAILED_COL_NAME, hardcoded_variables.FRACTION_HETEROZYGOUS_COL_NAME])
    return marker_failed_df



def qc_by_samples_main_function(samples_df):
    sucessful_markers_by_sample(samples_df)
    qc_by_samples.missing_data_by_sample(samples_df)
    qc_by_samples.heterozygous_markers_by_sample(samples_df)

    filtered_samples_df = return_bad_samples(samples_df)

    qc_by_samples.report_filtered_samples(filtered_samples_df)

    clean_good_samples_df = qc_by_samples.return_unfiltered_samples(samples_df)


if __name__ == '__main__':
    by_sample_part1_results_df = read_data.read_part1_result_bysample_csv()

    list_samples_to_keep = qc_by_samples_main_function(by_sample_part1_results_df)

    clean_samples_df_from_part_1 = read_data.regenerate_part1_samples_df()
    marker_failed_freq_df = _create_marker_failed_heterozygous_freq_df(clean_samples_df_from_part_1)
    qc_by_markers_main_function(marker_failed_freq_df)
