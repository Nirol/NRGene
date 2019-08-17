import pandas as pd


def _write_output_csv_file(output_towrite):
    df = pd.DataFrame(data=output_towrite)
    df.to_csv("output/part1/sim_matrix.csv", sep=',', header=False,
              index=False)
    df.to_csv("output/part2/sim_matrix.csv", sep=',', header=False,
              index=False)


def _write_excluded_sequences(excluded_sequences_output):
    output_file = open("output/part1/excluded_sequences.txt", 'w+')
    for msg in excluded_sequences_output:
        msg.replace('"', "")
        output_file.write(msg)
        output_file.write('\n')
    output_file.close()


def _write_excluded_marker_names(error_markers_names):
    with open("output/part1/error_markers_names.csv", 'w+',
              encoding="utf-8") as fp:
        fp.write("\n".join(error_markers_names))


def part1_print_sequence_error_msg(seq_description, sequence_errors,
                                   excluded_seq,
                                   error_markers_names):
    headline = "The marker:%s\n was excluded due to the following errors:\n" % (
        seq_description)
    complete_error_msg = (
            headline + "{}".format(', '.join(sequence_errors)) + "\n")
    #adding complete marker error msg to excluded_seq file:
    excluded_seq.append(complete_error_msg)
    error_markers_names.append(seq_description)


def write_part1_output_files(output, excluded_sequences, error_markers_names):
    _write_excluded_sequences(excluded_sequences)
    _write_excluded_marker_names(error_markers_names)
    _write_output_csv_file(output)


def write_part2_fasta_files(allele_1_fasta_towrite, allele_2_fasta_towrite):
    with open("output/part2/allele_1_sequences.fasta", 'w') as fp:
        fp.write("\n".join(allele_1_fasta_towrite))
    with open("output/part2/allele_2_sequences.fasta", 'w') as fp:
        fp.write("\n".join(allele_2_fasta_towrite))
