from tamu_io import constants


def _locate_snp_idx(seq):
    ind = next((i for i, ch in enumerate(seq) if
                ch in constants.BIALLELIC_NUCLEIC_CODES), -1)
    return ind


def _change_index_nucleotide(seq, idx, new_char):
    return seq[:idx] + new_char + seq[idx + 1:]


def _update_sequences_new_allele(seq, snp_idx):
    biallelic_char = seq[snp_idx]
    nucleotide_list_list = constants.NUCLEIC_DICT[biallelic_char]
    seq_allele_1 = _change_index_nucleotide(seq, snp_idx,
                                            nucleotide_list_list[0])
    seq_allele_2 = _change_index_nucleotide(seq, snp_idx,
                                            nucleotide_list_list[1])
    return seq_allele_1, seq_allele_2


def parse_sequence(seq):
    snp_idx = _locate_snp_idx(seq)
    (seq_allele_1, seq_allele_2) = _update_sequences_new_allele(seq, snp_idx)
    return seq_allele_1, seq_allele_2, len(seq), snp_idx
