from question2 import read_data, clean_genotype_data
import time
_HEADLINE_CSV_OUTPUT = ["Sample Name", "Sample ID (entry)",
                        "Sample description (designation)",
                        "Fraction of markers successfully genotyped",
                        "Fraction of heterozygous genotypes"]


def _get_meta_data(df, colmn):
    sample_name = colmn
    entry = df.loc["Entry", colmn]
    designation = df.loc["Designation", colmn]
    return sample_name, entry, designation


def compute_fractions(value_count):
    (dna_nuc_count, biallelic_nuc_count,
     failed_count) = read_data.parse_allele_freq_value_count(value_count)

    total_results = dna_nuc_count + biallelic_nuc_count + failed_count

    total_successfully_genotyped = dna_nuc_count + biallelic_nuc_count
    if total_results == 0:
        fraction_successfully_genotyped=0
    else:
        fraction_successfully_genotyped = total_successfully_genotyped / total_results

    if total_successfully_genotyped == 0:
        fraction_heterozygous=-1
    else:
        fraction_heterozygous = biallelic_nuc_count / total_successfully_genotyped

    return round(fraction_successfully_genotyped, 3), round(
        fraction_heterozygous, 3)


def _get_fraction_markers(df, colmn):
    col_series = df[colmn]
    # skipping first 2 metadata rows with [2:]
    value_count = col_series[2:].value_counts()
    fraction_successfully_genotyped, fraction_heterozygous = compute_fractions(
        value_count)
    return str(fraction_successfully_genotyped), str(fraction_heterozygous)


def _write_csv_file(output_list):
    with open("output/part1/samples_part1_genotyping_result.csv", 'w',
              encoding="utf-8") as fp:
        fp.write("\n".join(output_list))


def _build_csv_file(clean_df):
    output_file = [",".join(_HEADLINE_CSV_OUTPUT)]
    for col in clean_df.columns[:]:
        metadata_list = _get_meta_data(clean_df, col)
        fractions_list = _get_fraction_markers(clean_df, col)
        output_row_list = metadata_list + fractions_list
        csv_output_row = ",".join(output_row_list)
        output_file.append(csv_output_row)
    _write_csv_file(output_file)




if __name__ == '__main__':
    start = time.time()
    #creating dictionary for markers valid nucleotide bases.
    #dictionary keys = marker name, value = list of valid nucleotides.
    markers_alleles_dict = read_data.set_marker_dict_part1()
    end = time.time()
    print("time taken to build markers allele dict = %s "% (end - start))
    genotype_df = read_data.read_samples_csv()
    read_sample_csv_time = time.time()
    print("time taken read sample csv = %s "% (read_sample_csv_time - end))
    samples_genotyping_df_removed_invalid_genotypes = clean_genotype_data.scan_invalid_genotypes(
        genotype_df, markers_alleles_dict)

    clean_genotype_data_time = time.time()
    print("time clean geno data = %s "% (clean_genotype_data_time - read_sample_csv_time))
    _build_csv_file(samples_genotyping_df_removed_invalid_genotypes)
