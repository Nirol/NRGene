import pandas as pd
import read_write

# INPUT CSV FILE STRUCTURE:
# col 0 = Marker name
# col 1 =  Marker ID
# col 2 Marker allele 1
# col 3 Marker allele 2
# col 4 Sequence allele 1
# col 5 Sequence allele 2
# col 6 Marker length
# col 7 SNP position

_USED_COLUMNS = [0, 4, 5]
_FASTA_SEQUENCE_LINE_LENGTH = 80


def cut_seq_length_recursive(allele_fasta, allele_seq):
    sequence_length = len(allele_seq)
    if sequence_length <= _FASTA_SEQUENCE_LINE_LENGTH:
        allele_fasta.append(allele_seq)
    else:
        allele_fasta.append(allele_seq[:_FASTA_SEQUENCE_LINE_LENGTH])
        cut_seq_length_recursive(allele_fasta,
                                 allele_seq[_FASTA_SEQUENCE_LINE_LENGTH:])


def _append_row_to_fasta_files(allele1_fasta, allele2_fasta, df_row):
    fasta_description_line = ">" + df_row['marker_name']
    allele1_fasta.append(fasta_description_line)
    allele2_fasta.append(fasta_description_line)
    cut_seq_length_recursive(allele1_fasta, df_row['allele_1'])
    cut_seq_length_recursive(allele2_fasta, df_row['allele_2'])


if __name__ == '__main__':
    allele_1_fasta = []
    allele_2_fasta = []
    marker_data_df = pd.read_csv("output/part1/marker_data.csv",
                                 usecols=_USED_COLUMNS,
                                 names=["marker_name", "allele_1", "allele_2"])
    for index, row in marker_data_df.iterrows():
        _append_row_to_fasta_files(allele_1_fasta, allele_2_fasta, row)
    read_write.write_part2_fasta_files(allele_1_fasta, allele_2_fasta)
