import unittest

from tamu_io.seq import validation

NUMBER_BIALLELIC_ALLOWED = 1


class TestSequenceValidation(unittest.TestCase):

    def test__find_invalid_chars_nucleic(self):
        """
        Test that it can sum a list of integers
        """
        seq_char_set = {'A', 'C', 'T', 'G'}
        result_invalid_char_set = validation._find_invalid_chars(seq_char_set)
        self.assertEqual(len(result_invalid_char_set), 0)

    def test__find_invalid_chars_biallelic(self):
        """
        Test that it can sum a list of integers
        """
        seq_char_set = {'R', 'M', 'S', 'W', 'Y', 'K'}
        result_invalid_char_set = validation._find_invalid_chars(seq_char_set)
        self.assertEqual(len(result_invalid_char_set), 0)

    def test__find_invalid_chars_invalid1(self):
        """
        Test find_invalid_chars on various program logic invalid chars
        """
        seq_char_set = {'Z', 'U', 'A', 'C', 'T', 'G'}
        result_invalid_char_set = validation._find_invalid_chars(seq_char_set)
        expected_invalid_chat_set = ['U', 'Z']
        self.assertEqual(result_invalid_char_set, expected_invalid_chat_set)

    def test__find_invalid_chars_invalid2(self):
        """
        Test find_invalid_chars on various invalid fasta sequence chars
        """
        seq_char_set = {'\\', '@', '-', '_', ' ', '0', 'R', 'M', 'S', 'W', 'Y',
                        'K'}
        result_invalid_char_set = validation._find_invalid_chars(seq_char_set)
        expected_invalid_chat_set = sorted({'\\', '@', '-', '_', ' ', '0'})
        self.assertEqual(result_invalid_char_set, expected_invalid_chat_set)

    def test__find_invalid_chars_invalid_empty(self):
        """
        Test find_invalid_chars on empty set input
        """
        seq_char_set = {}
        result_invalid_char_set = validation._find_invalid_chars(seq_char_set)
        self.assertEqual(len(result_invalid_char_set), 0)

    def test__find_invalid_chars_occurrence0(self):
        seq = "ACTG"
        seq_char_set = set(seq)
        result_invalid_char_set = validation._find_invalid_chars_occurrence(
            seq_char_set, seq)
        expected_occurrence_list = []
        self.assertEqual(result_invalid_char_set, expected_occurrence_list)

    def test__find_invalid_chars_occurrence1(self):
        seq = "ACTGU"
        seq_char_set = set(seq)
        result_invalid_char_set = validation._find_invalid_chars_occurrence(
            seq_char_set, seq)
        expected_occurrence_list = [[4]]
        self.assertEqual(result_invalid_char_set, expected_occurrence_list)

    def test__find_invalid_chars_occurrence2(self):
        seq = "ACGTUACGTUACGTU"
        seq_char_set = set(seq)
        result_invalid_char_set = validation._find_invalid_chars_occurrence(
            seq_char_set, seq)
        expected_occurence_list = [[4, 9, 14]]
        self.assertEqual(result_invalid_char_set, expected_occurence_list)

    def test__find_invalid_chars_occurrence4(self):
        seq = "ACGTUACGTUACGTUzzz"
        seq_char_set = set(seq)
        result_invalid_char_set = validation._find_invalid_chars_occurrence(
            seq_char_set, seq)
        expected_occurence_list = [[4, 9, 14], [15, 16, 17]]
        self.assertEqual(result_invalid_char_set, expected_occurence_list)

    def test__build_error_massage_invalid_chars(self):
        seq = "ACGTUACGTUACGTUzzz"
        seq_char_set = set(seq)
        invalid_char_occurrence = validation._find_invalid_chars_occurrence(
            seq_char_set, seq)
        sequence_errors = []

        validation._build_error_massage_invalid_chars(
            sequence_errors, invalid_char_occurrence, seq)

        errors_list = ("Sequence contain an invalid character:",
                       "'U' - in positions:[4, 9, 14].",
                       "'z' - in positions:[15, 16, 17].")
        expected_error_msg = "\n".join(errors_list)
        self.assertEqual(sequence_errors[0], expected_error_msg)

    def test__is_char_type_valid(self):
        seq = "ACGTUACGTUACGTUzzz"
        sequence_errors = []
        validation._is_char_type_valid(seq, sequence_errors)

        error_headline = "Sequence contain an invalid character:"
        error_info_line1 = "'U' - in positions:[4, 9, 14]."
        error_info_line2 = "'z' - in positions:[15, 16, 17]."
        errors_list = (error_headline, error_info_line1, error_info_line2)
        expected_error_msg = "\n".join(errors_list)

        self.assertEqual(sequence_errors[0], expected_error_msg)


    def build_error_msg_for_testing(self, frequency_table):
        error_headline = "Sequence contain wrong number of biallelic characters!.\nExact number of biallelic characters expected = %s." % (
            NUMBER_BIALLELIC_ALLOWED)
        error_info_line1 = "Frequency of all biallelic characters in sequence:\n%s"%(frequency_table)
        errors_list = (error_headline, error_info_line1)
        expected_error_msg = "\n".join(errors_list)
        return expected_error_msg


    def test__build_error_massage_biallelic(self):
        frequency_table = {'K': 5, 'S': 0, 'W': 0, 'R': 1, 'Y': 0, 'M': 3}
        sequence_errors = []
        validation._build_error_massage_biallelic(frequency_table,
                                                sequence_errors)
        expected_error_msg = self.build_error_msg_for_testing(frequency_table)
        self.assertEqual(sequence_errors[0], expected_error_msg)

    def test__build_error_massage_biallelic_false_error(self):
        frequency_table = {'K': 0, 'S': 0, 'W': 0, 'R': 0, 'Y': 0, 'M': 1}
        sequence_errors = []
        validation._build_error_massage_biallelic(frequency_table,
                                                sequence_errors)

        self.assertNotEqual(sequence_errors[0], [])

    def test__is_single_biallelic_validate_no_error(self):
        frequency_table = {'K': 0, 'S': 0, 'W': 0, 'R': 0, 'Y': 0, 'M': 1}
        sequence_errors = []
        validation._is_single_biallelic_validate(frequency_table,
                                               sequence_errors)
        self.assertEqual(len(sequence_errors), 0)


    def test__is_single_biallelic_zero_bia(self):
        frequency_table = {'K': 0, 'S': 0, 'W': 0, 'R': 0, 'Y': 0, 'M': 0}
        sequence_errors = []
        validation._is_single_biallelic_validate(frequency_table,
                                               sequence_errors)
        expected_error_msg = self.build_error_msg_for_testing(frequency_table)
        self.assertEqual(sequence_errors[0], expected_error_msg)

    def test__is_single_biallelic_negative_bia(self):
        frequency_table = {'K': -5, 'S': 0, 'W': 0, 'R': 0, 'Y': 0, 'M': 0}
        sequence_errors = []
        validation._is_single_biallelic_validate(frequency_table,
                                               sequence_errors)
        expected_error_msg = self.build_error_msg_for_testing(frequency_table)
        self.assertEqual(sequence_errors[0], expected_error_msg)

    def test_validate_sequence_gaps1(self):
        sequence_string = "AC--GT"
        sequence_errors = []
        validation.validate_sequence(sequence_string, sequence_errors)
        #print(sequence_errors)
        self.assertEqual(len(sequence_errors), 2)

    def test_validate_sequence_gaps2(self):
        sequence_string = "_AC__G-T-"
        sequence_errors = []
        validation.validate_sequence(sequence_string, sequence_errors)
        #print(sequence_errors)
        self.assertEqual(len(sequence_errors), 2)

    def test_validate_sequence_space(self):
        sequence_string = "AC GT"
        sequence_errors = []
        validation.validate_sequence(sequence_string, sequence_errors)
        #print(sequence_errors)
        self.assertEqual(len(sequence_errors), 2)

    def test_validate_sequence_space_bia(self):
        sequence_string = "AC GTR"
        sequence_errors = []
        validation.validate_sequence(sequence_string, sequence_errors)
        # print(sequence_errors)
        self.assertEqual(len(sequence_errors), 1)

    def test__is_sequence_valid_none(self):
        sequence_string = None
        sequence_errors = []
        validation._is_sequence_valid(sequence_string,sequence_errors)
        print(sequence_errors[0])
        expected_error_msg = "Sequence is empty!."
        self.assertEqual(sequence_errors[0], expected_error_msg)

    def test__is_sequence_valid_none(self):
        sequence_string = ""
        sequence_errors = []
        validation._is_sequence_valid(sequence_string, sequence_errors)
        print(sequence_errors[0])
        expected_error_msg = "Sequence is empty!."
        self.assertEqual(sequence_errors[0], expected_error_msg)


