def create_plot_hist_no_fixed_bins(data_series, plot_title, plot_x_title,
                                   plot_y_title, num_bins):
    ax = data_series.plot.hist(rot=0, color='mediumvioletred',
                               alpha=0.8,
                               title=plot_title, bins=num_bins,
                               figsize=(8, 4), logy=True)
    x_multiplier = 1.05
    for p in ax.patches:
        ax.annotate(str(int(p.get_height())),
                    (p.get_x() * x_multiplier, p.get_height() * 1.005))
        x_multiplier = x_multiplier - 0.0003
    ax.set_ylabel(plot_y_title, labelpad=20, weight='bold', size=10,
                  rotation=0)
    ax.set_xlabel(plot_x_title, labelpad=20, weight='bold',
                  size=10,
                  rotation=0)
    return ax


def create_plot_hist_cumulative_no_fixed_bins(data_series, plot_title,
                                              plot_x_title,
                                              plot_y_title):
    ax = data_series.plot.hist(cumulative=True, density=5, bins=20, rot=0,
                               color='mediumvioletred',
                               alpha=0.8,
                               title=plot_title,
                               figsize=(12, 6))
    ax.set_ylabel(plot_y_title, labelpad=35, weight='bold', size=10,
                  rotation=0)
    ax.set_xlabel(plot_x_title, labelpad=20, weight='bold',
                  size=10,
                  rotation=0)
    return ax
