import argparse
from config import *
import src.eia.production_ing_full
import src.eia.production_ing_incremental
import src.eia.prices_ing_full
import src.eia.prices_ing_incremental
import src.rrc.well_ing_full
import src.rrc.field_ing_full
import src.rrc.general_ing_dsv
from index_constants import (
    production,
    prices,
    wells,
    fields,
    district,
    county,
    og_county,
    og_county_lease,
    og_district,
    og_field,
    og_field_data,
    og_operator,
    og_operator_data,
    well_xy,
)
from index_props import (
    county_sett,
    district_sett,
    og_county_sett,
    og_district_sett,
    og_field_sett,
    og_field_data_sett,
    og_operator_sett,
    og_operator_data_sett,
)


def main():
    parser = argparse.ArgumentParser(description="Script de indexación.")
    parser.add_argument(
        "--mode",
        "-m",
        choices=["FULL", "INCREMENTAL"],
        required=False,
        help="Modo de ingesta (FULL o INCREMENTAL).",
    )
    parser.add_argument(
        "--index",
        "-i",
        choices=[
            production,
            prices,
            wells,
            fields,
            district,
            county,
            og_county,
            og_county_lease,
            og_district,
            og_field,
            og_field_data,
            og_operator,
            og_operator_data,
            well_xy,
        ],
        required=True,
        help="Index a ingestar",
    )
    args = parser.parse_args()

    mode = args.mode
    index = args.index

    if mode == "FULL" and index == production:
        src.eia.production_ing_full.main()
    elif mode == "INCREMENTAL" and index == production:
        src.eia.production_ing_incremental.main()
    elif mode == "FULL" and index == prices:
        src.eia.prices_ing_full.main()
    elif mode == "INCREMENTAL" and index == prices:
        src.eia.prices_ing_incremental.main()
    elif index == wells:
        src.rrc.well_ing_full.main()
    elif index == fields:
        src.rrc.field_ing_full.main()
    elif index == county:
        src.rrc.general_ing_dsv.main(index, county_sett)
    elif index == district:
        src.rrc.general_ing_dsv.main(index, district_sett)
    elif index == og_county:
        src.rrc.general_ing_dsv.main(index, og_county_sett)
    elif index == og_county_lease:
        src.rrc.general_ing_dsv.main(index)
    elif index == og_district:
        src.rrc.general_ing_dsv.main(index, og_district_sett)
    elif index == og_field:
        src.rrc.general_ing_dsv.main(index, og_field_sett)
    elif index == og_field_data:
        src.rrc.general_ing_dsv.main(index, og_field_data_sett)
    elif index == og_operator:
        src.rrc.general_ing_dsv.main(index, og_operator_sett)
    elif index == og_operator_data:
        src.rrc.general_ing_dsv.main(index, og_operator_data_sett)


if __name__ == "__main__":
    main()
