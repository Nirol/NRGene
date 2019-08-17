from tamu_io.seq import validation,description
from question2.part2 import hardcoded_variables
from Bio import SeqIO


def report_filtered_markers_csv(filteredmdarkers_df):
    df = filteredmdarkers_df.sort_values(
        [hardcoded_variables.FRACTION_FAILED_COL_NAME, hardcoded_variables.FRACTION_HETEROZYGOUS_COL_NAME],
        ascending=[False, False])
    df.to_csv("./output/part2/filtered_markers.csv", sep=',', header=True,
              index=False)


def is_sequence_valid(sequence_string):
    sequence_errors = []
    validation.validate_sequence(sequence_string, sequence_errors)
    if len(sequence_errors) > 0:
        return False
    return True


def extract_sequence_info(description_line):
    description_data_list = description.parse_seq_description(description_line)
    marker_name = description_data_list[0]
    marker_id = description_data_list[1]
    return marker_name, marker_id


def search_in_filtered_markers(marker_id, df):
    for name in df['Marker']:
        if name == marker_id:
            return True
    return False


def write_filtered_markers_fasta_file(markers_fasta):
    with open("output/part2/filterd_markers.fasta", 'w') as fp:
        fp.write("\n".join(markers_fasta))


def report_filtered_markers(df):
    report_filtered_markers_csv(df)
    fasta_markers = []
    file_path = "data/TAMU_SNP63K_69997.fasta"

    for record in SeqIO.parse(file_path, "fasta"):
        seq_description = record.description
        sequence = record.seq
        if is_sequence_valid(sequence):
            marker_name, marker_id = extract_sequence_info(seq_description)
            if search_in_filtered_markers(marker_id, df):
                fasta_description_line = ">" + marker_name
                fasta_markers.append(fasta_description_line)
                fasta_markers.append(str(sequence))
    write_filtered_markers_fasta_file(fasta_markers)
