_MARKER_NAME_PREFIX_LENGTH = len("marker_name=")
_MARKER_ID_LENGTH = 8
_ALLELE_1_IDX_FROM_END = -3
_ALLELE_2_IDX_FROM_END = -1
_INITIAL_DESCRIPTION_SPLIT = 2


def _parse_description_id(id):
    clean_id = id[-_MARKER_ID_LENGTH:]
    return clean_id


def _parse_description_name(name):
    clean_name = name[_MARKER_NAME_PREFIX_LENGTH:]
    return clean_name


def _parse_description_alleles(description_suffix):
    description_suffix.strip()
    allele_1 = description_suffix[_ALLELE_1_IDX_FROM_END]
    allele_2 = description_suffix[_ALLELE_2_IDX_FROM_END]
    return allele_1, allele_2


def parse_seq_description(description):
    id_raw, name_raw, description_suffix = \
        description.split(' ', _INITIAL_DESCRIPTION_SPLIT)
    marker_id = _parse_description_id(id_raw)
    marker_name = _parse_description_name(name_raw)
    alleles = _parse_description_alleles(description_suffix)
    description_data = (marker_name, marker_id, alleles[0], alleles[1])
    return description_data
