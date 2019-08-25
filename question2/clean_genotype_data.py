from question2.part2 import hardcoded_variables


def write_bad_markers(not_found_markers):
    with open(
            "output/part1/excluded_markers_from_question1_in_samples_file.csv",
            'w',
            encoding="utf-8") as fp:
        fp.write("\n".join(not_found_markers))


def write_bad_genotipes(error_genotipe_list):
    with open("output/part1/failed_genotypings.csv", 'w',
              encoding="utf-8") as fp:
        fp.write("\n".join(error_genotipe_list))


def _delete_bad_markers(genotyping_df, not_found_markers):
    samples_genotyping_df_removed_markers = genotyping_df.drop(
        not_found_markers[1:], axis=0)
    return samples_genotyping_df_removed_markers


def _validate_nuc_marker(marker_name, nuc, markers_alleles_dict,
                         not_found_markers):
    is_genotype_fail = False
    if marker_name in markers_alleles_dict:
        valid_nuc_list_for_marker = markers_alleles_dict[marker_name]
        if nuc not in valid_nuc_list_for_marker:
            is_genotype_fail = True

    else:
        if marker_name not in not_found_markers:
            not_found_markers.append(marker_name)
    return is_genotype_fail


def _scan_invalid_genotypes(samples_genotyping_df, marker_allele_dict,
                              marker_name):
    valid_nuc_list_for_marker = marker_allele_dict[marker_name]
    valid_nuc_list_for_marker.append('failed')
    samples_genotyping_df[marker_name] = samples_genotyping_df[
        marker_name].apply(
        lambda x: "myfailed" if x not in valid_nuc_list_for_marker else x)


def report_failed_genotypes(df, marker_name, genotype_fail):
    genotypes_fails_df = df[df[marker_name] == "myfailed"]
    sample_list = list(genotypes_fails_df.index.values)
    for sample in sample_list:
        genotype_fail.append("%s, %s" % (marker_name, sample))


def remove_bad_markers(df, unfound_markers):
    if hardcoded_variables.DELETE_BAD_MARKERS_BASED_ON_PART1:
        samples_genotyping_df_removed_markers = _delete_bad_markers(
            df,
            unfound_markers)
        return samples_genotyping_df_removed_markers
    else:
        return df


def scan_invalid_genotypes(genotyping_df, marker_allele_dict,
                           report_bad_marers_genotypes=True):
    trans_df = genotyping_df.transpose()
    columns = list(trans_df)
    not_found_markers = ["Marker_In_Samples_File_Not_Found_"]
    genotype_fail = ["Marker, Sample"]
    # skipping metadata first 2 cols
    for col in columns[2:]:
        marker_name = col
        if marker_name in marker_allele_dict:
            _scan_invalid_genotypes(trans_df, marker_allele_dict,
                                      marker_name)
            report_failed_genotypes(trans_df, marker_name, genotype_fail)
        else:
            not_found_markers.append(marker_name)

    if report_bad_marers_genotypes:
        write_bad_genotipes(genotype_fail)
        write_bad_markers(not_found_markers)

    edited_genotyping_df = trans_df.transpose()
    # deleting bad markers based on part1 analysis
    return remove_bad_markers(edited_genotyping_df, not_found_markers)
