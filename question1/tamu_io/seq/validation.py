from tamu_io import constants


def _find_invalid_chars(sequence_char_set):
    invalid_chars = {char for char in sequence_char_set if
                     char not in constants.VALID_CHARS}
    return sorted(invalid_chars)


def _find_invalid_chars_occurrence(sequence_char_set, sequence):
    invalid_chars = _find_invalid_chars(sequence_char_set)
    occurrence_list_per_char = []
    if len(invalid_chars) > 0:
        occurrence_list_per_char = [[i for i, letter in enumerate(sequence)
                                     if letter == char] for char in
                                    invalid_chars]
    return occurrence_list_per_char


def _build_error_massage_invalid_chars(sequence_errors,
                                       invalid_chars_occurrence, sequence):
    head_error_massage = "Sequence contain an invalid character:"
    occurrence_error_list = [head_error_massage]
    for char_occurrence_list in invalid_chars_occurrence:
        occurrence_error_list.append("\'%s\' - in positions:%s." %
                                     (sequence[char_occurrence_list[0]],
                                      char_occurrence_list))

    invalid_occurrence_errors_msgs = '\n'.join(
        str(msg) for msg in occurrence_error_list)
    sequence_errors.append(invalid_occurrence_errors_msgs)


def _is_char_type_valid(sequence, sequence_errors):
    char_set = set(sequence)
    # check if valid_chars set contains all elements of sequence_char_set
    is_invalid_seq = not all(
        char in constants.VALID_CHARS for char in char_set)
    if is_invalid_seq:
        invalid_chars_occurrence = _find_invalid_chars_occurrence(char_set,
                                                                  sequence)
        _build_error_massage_invalid_chars(sequence_errors,
                                           invalid_chars_occurrence, sequence)


def _build_error_massage_biallelic(frequency_table, sequence_errors):
    error_msg = "Marker sequence contain wrong number of biallelic characters!"
    error_msg_biallelic_freq = "Biallelic characters frequency in sequence:%s" % (
        frequency_table)
    final_error_msg = "\n".join((error_msg, error_msg_biallelic_freq))
    sequence_errors.append(final_error_msg)


def _is_single_biallelic_validate(frequency_table, sequence_errors):
    biallelic_count = 0
    for char, freq in frequency_table.items():
        biallelic_count = biallelic_count + freq

    if biallelic_count != constants.NUMBER_BIALLELIC_ALLOWED:
        _build_error_massage_biallelic(frequency_table, sequence_errors)


def get_biallelic_frequency_table(sequence):
    frequency_table = {char: sequence.count(char) for char in
                       constants.BIALLELIC_NUCLEIC_CODES}
    return frequency_table


def _is_single_biallelic(sequence, sequence_errors):
    biallelic_frequency_table = get_biallelic_frequency_table(sequence)
    _is_single_biallelic_validate(biallelic_frequency_table, sequence_errors)


def _is_sequence_valid(sequence, sequence_errors):
    if not sequence:
        empty_string_error_msg = "Sequence is empty!."
        sequence_errors.append(empty_string_error_msg)


def validate_sequence(sequence, sequence_errors):
    _is_sequence_valid(sequence, sequence_errors)
    _is_char_type_valid(sequence, sequence_errors)
    _is_single_biallelic(sequence, sequence_errors)


def clean_data(data):
    data.replace('\n', '')
    return data
