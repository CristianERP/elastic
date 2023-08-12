import src.production_ing_full
import src.production_ing_incremental
import src.prices_ing_full
import src.prices_ing_incremental
import argparse
from index_constants import production, prices


def main():
    parser = argparse.ArgumentParser(description="Script de indexación.")
    parser.add_argument(
        "--mode",
        "-m",
        choices=["FULL", "INCREMENTAL"],
        required=True,
        help="Modo de ingesta (FULL o INCREMENTAL).",
    )
    parser.add_argument(
        "--index",
        "-i",
        choices=[prices, production],
        required=True,
        help="Index a ingestar",
    )
    args = parser.parse_args()

    mode = args.mode
    index = args.index

    if mode == "FULL" and index == production:
        src.production_ing_full.main()
    elif mode == "INCREMENTAL" and index == production:
        src.production_ing_incremental.main()
    elif mode == "FULL" and index == prices:
        src.prices_ing_full.main()
    elif mode == "INCREMENTAL" and index == prices:
        src.prices_ing_incremental.main()


if __name__ == "__main__":
    main()
