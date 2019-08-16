import unittest

from tamu_io.seq import parse

NUMBER_BIALLELIC_ALLOWED = 1


class TestSequenceParse(unittest.TestCase):


    def test__locate_snp_idx_zero(self):
        sequence_string = "MAATCGA"
        actual_idx = parse._locate_snp_idx(sequence_string)
        expected_idx = 0
        self.assertEqual(actual_idx, expected_idx)

    def test__locate_snp_idx_last(self):
        sequence_string = "GGGR"
        actual_idx = parse._locate_snp_idx(sequence_string)
        expected_idx = 3
        self.assertEqual(actual_idx, expected_idx)


    def test__locate_snp_idx_last(self):
        sequence_string = "GTACATYAA"
        actual_idx = parse._locate_snp_idx(sequence_string)
        expected_idx = 6
        self.assertEqual(actual_idx, expected_idx)

    def test__locate_snp_idx_not_found(self):
        sequence_string = "GGG"
        actual_idx = parse._locate_snp_idx(sequence_string)
        expected_idx = -1
        self.assertEqual(actual_idx, expected_idx)


    def test__change_index_nucleotide(self):
        sequence_string = "GGG"
        idx = 1
        new_char = 'K'
        actual = parse._change_index_nucleotide(sequence_string, idx, new_char)
        expected = "GKG"
        self.assertEqual(actual, expected)

    def test__change_index_nucleotide_first(self):
        sequence_string = "GGG"
        idx = 0
        new_char = 'K'
        actual = parse._change_index_nucleotide(sequence_string, idx, new_char)
        expected = "KGG"
        self.assertEqual(actual, expected)

    def test__change_index_nucleotide_last(self):
        sequence_string = "GGG"
        idx = 2
        new_char = 'K'
        actual = parse._change_index_nucleotide(sequence_string, idx, new_char)
        expected = "GGK"
        self.assertEqual(actual, expected)

