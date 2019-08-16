DNA_CODES = {'A', 'C', 'T', 'G'}
BIALLELIC_NUCLEIC_CODES = {'K', 'M', 'R', 'S', 'W', 'Y'}
NUMBER_BIALLELIC_ALLOWED = 1
MULTIALLELIC_NUCLEIC_CODES = {'B', 'D', 'H', 'N', 'U', 'V'}
VALID_CHARS = DNA_CODES.union(BIALLELIC_NUCLEIC_CODES)
NUCLEIC_DICT = {'K': ['G', 'T'], 'M': ['A', 'C'], 'R': ['A', 'G'],
                'S': ['C', 'G'], 'W': ['A', 'T'], 'Y': ['C', 'T']}
