from argparse import ArgumentParser

import numpy as np
import matplotlib.pyplot as plt


def main(args):
    if args.mode_positions == "uniform":
        means = np.linspace(start=0, stop=50, num=args.n_modes)
    elif args.mode_positions == "normal":
        means = np.random.randn(args.n_modes) * 50
    elif args.mode_positions == "skewed":
        n_left = int(0.8 * args.n_modes)
        n_right = args.n_modes - n_left
        means = np.concatenate([
            np.linspace(start=0, stop=10, num=n_left),
            np.linspace(start=10, stop=50, num=n_right)
        ], axis=0)

    points = np.concatenate([
        np.random.randn(args.n_points) + shift
        for shift in means
    ], axis=0)

    sample_means = [
        np.mean(np.random.choice(points, size=args.sample_size))
        for _ in range(args.n_samplings)
    ]

    fig, (points_ax, means_ax) = plt.subplots(2, figsize=(8, 8))
    
    points_ax.hist(points, bins=args.hist_bins)
    points_ax.set_title("Points")

    means_ax.hist(sample_means, bins=args.hist_bins)
    means_ax.set_title("Sample means")

    plt.show()


if __name__ == "__main__":
    parser = ArgumentParser("Multimodal CLT experiment")
    parser.add_argument("--n_modes", type=int, default=1, help="num of uniform distributions")
    parser.add_argument("--mode_positions", type=str, choices=["uniform", "skewed", "normal"], default="uniform", help="distribution of modes")
    parser.add_argument("--n_points", type=int, default=500, help="how many points each mode should get")
    parser.add_argument("--n_samplings", type=int, default=50, help="how many samples should take")
    parser.add_argument("--sample_size", type=int, default=100, help="size of one sample")
    parser.add_argument("--hist_bins", type=int, default=50, help="number of bins in histogram")
    main(parser.parse_args())
