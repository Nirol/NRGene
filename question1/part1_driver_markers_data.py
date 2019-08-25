from Bio import SeqIO
from tamu_io.seq import parse, validation, description
import read_write


def load_fasta_file(file):
    with open(file, 'r') as content_file:
        content = content_file.read()
    return content


def parse_seq_description(description_string):
    return description.parse_seq_description(description_string)


def is_sequence_valid(seq_description, sequence_string, excluded_seq,
                      error_marker_names):
    sequence_errors = []
    validation.validate_sequence(sequence_string, sequence_errors)
    if len(sequence_errors) > 0:
        read_write.part1_print_sequence_error_msg(seq_description,
                                                  sequence_errors,
                                                  excluded_seq,
                                                  error_marker_names)
        return False
    return True


def parse_seq(sequence_string):
    return parse.parse_sequence(sequence_string)


def merge_marker_data_lists(description_data_list, seq_data_list, output_list):
    complete_seq_row = description_data_list + seq_data_list
    output_list.append(complete_seq_row)


def extract_sequence_info(description_line, sequence_line, output_list):
    description_data_list = parse_seq_description(description_line)
    sequence_data_list = parse_seq(sequence_line)
    merge_marker_data_lists(description_data_list, sequence_data_list,
                            output_list)


def read_parse_data():
    file_path = "data/TAMU_SNP63K_69997.fasta"
    script_out = []
    excluded_sequ = []
    error_markers = []

    for record in SeqIO.parse(file_path, "fasta"):
        description_ = record.description
        sequence = record.seq
        if is_sequence_valid(description_, sequence, excluded_sequences,
                             error_markers_names):
            extract_sequence_info(description_, sequence, script_output)

    return script_output, excluded_sequences, error_markers_names


# script_output = required output markers data csv.
# excluded_sequences = List of problems for each excluded marker
# error_markers_names = csv file of excluded markers full sequence description

if __name__ == '__main__':
    script_output, excluded_sequences, error_markers_names = read_parse_data()
    read_write.write_part1_output_files(script_output, excluded_sequences,
                                        error_markers_names)
