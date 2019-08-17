import unittest

import part2_driver_write_alleles_fasta_files

NUMBER_BIALLELIC_ALLOWED = 1


class TestPart2CreateFasta(unittest.TestCase):

    def test__cut_seq_length_recursive_lines_num(self):
        inlength_sequences = []
        sequence = "x" * (80*5 + 3)
        part2_driver_write_alleles_fasta_files._cut_seq_length_recursive(inlength_sequences, sequence)
        self.assertEqual(len(inlength_sequences), 6)

    def test__cut_seq_length_recursive_remainder(self):
        inlength_sequences = []
        sequence = "x" * (80*5 + 3)
        part2_driver_write_alleles_fasta_files._cut_seq_length_recursive(inlength_sequences, sequence)
        self.assertEqual(len(inlength_sequences[5]), 3)

    def test__cut_seq_length_recursive_short(self):
        inlength_sequences = []
        sequence = "x" * 5
        part2_driver_write_alleles_fasta_files._cut_seq_length_recursive(
            inlength_sequences, sequence)
        self.assertEqual(len(inlength_sequences), 1)

    def test__cut_seq_length_recursive_short2(self):
        inlength_sequences = []
        sequence = "x" * 5
        part2_driver_write_alleles_fasta_files._cut_seq_length_recursive(
            inlength_sequences, sequence)
        self.assertEqual(len(inlength_sequences[0]), 5)