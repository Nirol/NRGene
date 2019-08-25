# INPUT CSV FILE STRUCTURE:
# col 0 = Marker name
# col 1 =  Marker ID
# col 2 Marker allele 1
# col 3 Marker allele 2
# col 4 Sequence allele 1
# col 5 Sequence allele 2
# col 6 Marker length
# col 7 SNP position
import pandas as pd
from question2 import clean_genotype_data
from tamu_io import constants

NUCLEIC_DICT = {'K': ['G', 'T'], 'M': ['A', 'C'], 'R': ['A', 'G'],
                'S': ['C', 'G'], 'W': ['A', 'T'], 'Y': ['C', 'T']}


def read_part1_result_bysample_csv():
    sample_df = pd.read_csv("output/part1/samples_part1_genotyping_result.csv")
    return sample_df


def part1_read_marker_data_csv():
    _USED_COLUMNS = [1, 2, 3]
    marker_data = pd.read_csv("data/marker_data.csv",
                              usecols=_USED_COLUMNS,
                              names=["marker_name", "allele_1", "allele_2"])
    return marker_data


def part2_read_marker_data_csv():
    _USED_COLUMNS = [1, 4, 5]
    marker_data = pd.read_csv("data/marker_data.csv",
                              usecols=_USED_COLUMNS,
                              names=["marker_name", "allele_1_seq",
                                     "allele_2_seq"])
    return marker_data


def read_samples_csv():
    samples_genotyping = pd.read_csv(
        "data/GT_AH_DiversityAnalysisDataforCottonGen.csv",
        encoding="ISO-8859-1", index_col=0)
    genotype_df_no_commas = samples_genotyping.replace(',', ' ', regex=True)
    return genotype_df_no_commas


# creating dictonary of list of valid nucleotides for each marker
# key= marker name, value= list of valid nucleotides (including biallleic nuc )
def _update_alleles_dict(marker_data_df, markers_alleles_dict, row1_name, row2_name):
    for index, row in marker_data_df.iterrows():
        allele_list = [row[row1_name], row[row2_name]]
        for biallelic_nuc, allele_represented_list in NUCLEIC_DICT.items():
            if allele_list == allele_represented_list:
                allele_list.append(biallelic_nuc)
                markers_alleles_dict[row["marker_name"]] = allele_list


def set_marker_dict_part1():
    marker_df = part1_read_marker_data_csv()
    markers_alleles_dict = dict()
    _update_alleles_dict(marker_df, markers_alleles_dict, "allele_1", "allele_2")
    return markers_alleles_dict


def regenerate_part1_samples_df():
    markers_alleles_dict = set_marker_dict_part1()
    genotype_df = read_samples_csv()
    removed_unfound_markers_and_set_fail_genotype_df = clean_genotype_data.scan_invalid_genotypes(
        genotype_df, markers_alleles_dict, report_bad_marers_genotypes=False)

    return removed_unfound_markers_and_set_fail_genotype_df


def parse_allele_freq_value_count(value_count_series):
    dna_nuc_count = 0
    biallelic_nuc_count = 0
    failed_count = 0
    for key_value_list in value_count_series.iteritems():
        nuc = key_value_list[0]
        freq = key_value_list[1]
        if nuc in constants.DNA_CODES:
            dna_nuc_count = dna_nuc_count + freq
        elif nuc in constants.BIALLELIC_NUCLEIC_CODES:
            biallelic_nuc_count = biallelic_nuc_count + freq
        elif nuc == "failed" or nuc == "myfailed":
            failed_count = failed_count + freq
        else:
            print("UNKOWN NUCLEOTIC FOUND=%s" % nuc)
    return dna_nuc_count, biallelic_nuc_count, failed_count



