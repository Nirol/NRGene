import pandas as pd
import matplotlib.pyplot as plt

# INPUT CSV FILE STRUCTURE:
# col 0 = Marker name
# col 1 =  Marker ID
# col 2 Marker allele 1
# col 3 Marker allele 2
# col 4 Sequence allele 1
# col 5 Sequence allele 2
# col 6 Marker length
# col 7 SNP position

HEADLINE_COL_NAMES = ["marker_name", "marker_id", "allele_1", "allele_2",
                      "sequence_1", "sequence_2", "marker_length", "snp_idx"]


def create_bar_plot_custom_bins(marker_data_series, plot_title, plot_x_title,
                                plot_y_title, x_bins):
    out = pd.cut(marker_data_series, bins=x_bins)
    ax = out.value_counts(sort=False).plot.bar(rot=0, color='mediumvioletred',
                                               alpha=0.8,
                                               title=plot_title,
                                               figsize=(12, 6), logy=True)
    for p in ax.patches:
        ax.annotate(str(p.get_height()),
                    (p.get_x() * 1.005, p.get_height() * 1.01))
    ax.set_ylabel(plot_y_title, labelpad=20, weight='bold', size=16,
                  rotation=0)
    ax.set_xlabel(plot_x_title, labelpad=20, weight='bold', size=14)
    ax.set_xticklabels(
        [c for c in out.cat.categories])

    return ax


def plot_marker_length_bar_graph(marker_length_series):
    x_bins = [50, 84, 89, 90, 100, 101, 200, 201, 300, 301, 750, 1001]
    plot_title = "Number of Markers by Length"
    plot_x_title = "Length (bp)"
    plot_y_title = "n"
    ax = create_bar_plot_custom_bins(marker_length_series, plot_title,
                                     plot_x_title, plot_y_title, x_bins)
    # Fixing plot labels
    labels = [item.get_text() for item in ax.get_xticklabels()]
    labels[2] = '90'
    labels[4] = '101'
    labels[6] = '201'
    labels[8] = '301'
    labels[10] = '1001'
    ax.set_xticklabels(labels)

    plt.show()


def plot_snp_idx_bar_graph(marker_snp_idx_series):
    x_bins = [0, 29, 30, 49, 50, 75, 99, 100, 149, 150, 300, 499, 500]
    plot_title = "Number of Markers by SNP Location"
    plot_x_title = "SNP Location in Marker"
    plot_y_title = "n"

    ax = create_bar_plot_custom_bins(marker_snp_idx_series, plot_title,
                                     plot_x_title, plot_y_title, x_bins)

    #Fixing plot labels
    labels = [item.get_text() for item in ax.get_xticklabels()]
    labels[1] = '30'
    labels[3] = '50'
    labels[6] = '100'
    labels[8] = '150'
    labels[11] = '500'
    ax.set_xticklabels(labels)

    plt.show()


def single_var_stats(marker_name_series_df, var_name):
    marker_series = marker_name_series_df[var_name]
    print("************************************************")
    print("Single variable statistics for: %s" % var_name)
    print("Top 10 value counts:")
    print(marker_series.value_counts().head(10))
    print("Value counts divided to 10 bins (bins sorted by value count): ")
    print(marker_series.value_counts(bins=10))
    x_records = 15
    print("Top %s Largest records by %s " % (x_records, var_name))
    print(
        (marker_name_series_df.nlargest(30, var_name).to_string(index=False)))

    print("Top %s Smallest records by %s " % (x_records, var_name))
    print((marker_name_series_df.nsmallest(30, var_name).to_string(
        index=False)))

    print("%s mean:%s" % (var_name, marker_series.mean()))
    print("%s median:%s" % (var_name, marker_series.median()))
    print("************************************************")
    print('\n')


def analyze_marker_length(marker_df):
    marker_length_df = marker_df[["marker_name", "marker_length"]]
    single_var_stats(marker_length_df, "marker_length")

    marker_length_series = marker_df["marker_length"]
    plot_marker_length_bar_graph(marker_length_series)


def analyze_marker_snp_idx(marker_df):
    marker_snp_idx_df = marker_df[["marker_name", "snp_idx"]]
    single_var_stats(marker_snp_idx_df, "snp_idx")
    marker_snp_idx_series = marker_df["snp_idx"]
    plot_snp_idx_bar_graph(marker_snp_idx_series)


def analyze_marker_snp_freq(marker_df):
    total_df_length = len(marker_df)
    fraction_alleles = marker_df.groupby(['allele_1', 'allele_2']).size()
    percent_allels = fraction_alleles.round(2)

    ax = fraction_alleles.plot.bar(logy=True, figsize=(15, 7), rot=0,
                                   title="SNPs Alleles Frequencies")

    ax.set_ylabel("Freq", labelpad=20, weight='bold', size=10,
                  rotation=0)
    ax.set_xlabel("SNP Alleles", labelpad=20, weight='bold', size=10,
                  rotation=0)
    for p in ax.patches:
        ax.annotate(str(p.get_height()),
                    (p.get_x() * 1.05, p.get_height() * 1.005))

    plt.show()


if __name__ == '__main__':
    marker_data_df = pd.read_csv("output/part1/marker_data.csv",
                                 names=HEADLINE_COL_NAMES)
    analyze_marker_length(marker_data_df)
    analyze_marker_snp_idx(marker_data_df)
    analyze_marker_snp_freq(marker_data_df)

    # more ides:
    # cov between length and snp index
    # snp index of most common lenth and the the opposite
    # connection between allel and legnth
