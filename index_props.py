price_sett = {
    "mappings": {
        "properties": {
            "period": {
                "type": "date",
                "format": "yyyyMM",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "product": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "product-name": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "units": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "value": {"type": "float"},
        }
    }
}

county_sett = {
    "mappings": {
        "properties": {
            "COUNTY_FIPS_CODE": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "COUNTY_NAME": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "COUNTY_NO": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "DISTRICT_NAME": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "DISTRICT_NO": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "ONSHORE_ASSC_CNTY_FLAG": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "ON_SHORE_FLAG": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
        }
    }
}

district_sett = {
    "mappings": {
        "properties": {
            "DISTRICT_NAME": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "DISTRICT_NO": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "OFFICE_LOCATION": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "OFFICE_PHONE_NO": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
        }
    }
}

og_county_sett = {
    "mappings": {
        "properties": {
            "CNTY_COND_ENDING_BAL": {
                "type": "long",
            },
            "CNTY_COND_LIMIT": {
                "type": "long",
            },
            "CNTY_COND_PROD_VOL": {
                "type": "long",
            },
            "CNTY_COND_TOT_DISP": {
                "type": "long",
            },
            "CNTY_CSGD_GAS_LIFT": {
                "type": "long",
            },
            "CNTY_CSGD_LIMIT": {
                "type": "long",
            },
            "CNTY_CSGD_PROD_VOL": {
                "type": "long",
            },
            "CNTY_CSGD_TOT_DISP": {
                "type": "long",
            },
            "CNTY_GAS_ALLOW": {
                "type": "long",
            },
            "CNTY_GAS_LIFT_INJ_VOL": {
                "type": "long",
            },
            "CNTY_GAS_PROD_VOL": {
                "type": "long",
            },
            "CNTY_GAS_TOT_DISP": {
                "type": "long",
            },
            "CNTY_OIL_ALLOW": {
                "type": "long",
            },
            "CNTY_OIL_ENDING_BAL": {
                "type": "long",
            },
            "CNTY_OIL_PROD_VOL": {
                "type": "long",
            },
            "CNTY_OIL_TOT_DISP": {
                "type": "long",
            },
            "COUNTY_NAME": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "COUNTY_NO": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "CYCLE_MONTH": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "CYCLE_YEAR": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "CYCLE_YEAR_MONTH": {
                "type": "date",
                "format": "yyyyMM",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "DISTRICT_NAME": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "DISTRICT_NO": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "OIL_GAS_CODE": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
        }
    }
}

og_district_sett = {
    "mappings": {
        "properties": {
            "CYCLE_MONTH": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "CYCLE_YEAR": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "CYCLE_YEAR_MONTH": {
                "type": "date",
                "format": "yyyyMM",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "DISTRICT_NAME": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "DISTRICT_NO": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "DIST_COND_PROD_VOL": {
                "type": "long",
            },
            "DIST_CSGD_PROD_VOL": {
                "type": "long",
            },
            "DIST_GAS_PROD_VOL": {
                "type": "long",
            },
            "DIST_OIL_PROD_VOL": {
                "type": "long",
            },
        }
    }
}

og_field_sett = {
    "mappings": {
        "properties": {
            "CYCLE_MONTH": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "CYCLE_YEAR": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "CYCLE_YEAR_MONTH": {
                "type": "date",
                "format": "yyyyMM",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "DISTRICT_NAME": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "DISTRICT_NO": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "FIELD_COND_PROD_VOL": {
                "type": "long",
            },
            "FIELD_CSGD_PROD_VOL": {
                "type": "long",
            },
            "FIELD_GAS_PROD_VOL": {
                "type": "long",
            },
            "FIELD_NAME": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "FIELD_NO": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "FIELD_OIL_PROD_VOL": {
                "type": "long",
            },
        }
    }
}

og_field_data_sett = {
    "mappings": {
        "properties": {
            "CREATE_BY": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "CREATE_DT": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "DISTRICT_NAME": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "DISTRICT_NO": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "FIELD_CLASS": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "FIELD_H2S_FLAG": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "FIELD_MANUAL_REV_FLAG": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "FIELD_NAME": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "FIELD_NO": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "G_COMMENTS": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "G_COUNTY_NO": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "G_DERIVED_RULE_TYPE_CODE": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "G_DISCOVERY_DT": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "G_DONT_PERMIT": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "G_NOA_MAN_REV_RULE": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "G_OFFSHORE_CODE": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "G_RESCIND_DT": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "G_SALT_DOME_FLAG": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "G_SCHED_REMARKS": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "MODIFY_BY": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "MODIFY_DT": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "O_COMMENTS": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "O_COUNTY_NO": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "O_DERIVED_RULE_TYPE_CODE": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "O_DISCOVERY_DT": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "O_DONT_PERMIT": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "O_NOA_MAN_REV_RULE": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "O_OFFSHORE_CODE": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "O_RESCIND_DT": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "O_SALT_DOME_FLAG": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "O_SCHED_REMARKS": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "WILDCAT_FLAG": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
        }
    }
}

og_operator_sett = {
    "mappings": {
        "properties": {
            "CYCLE_MONTH": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "CYCLE_YEAR": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "CYCLE_YEAR_MONTH": {
                "type": "date",
                "format": "yyyyMM",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "OPERATOR_NAME": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "OPERATOR_NO": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "OPER_COND_PROD_VOL": {
                "type": "long",
            },
            "OPER_CSGD_PROD_VOL": {
                "type": "long",
            },
            "OPER_GAS_PROD_VOL": {
                "type": "long",
            },
            "OPER_OIL_PROD_VOL": {
                "type": "long",
            },
        }
    }
}

og_operator_data_sett = {
    "mappings": {
        "properties": {
            "CREATE_BY": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "CREATE_DT": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "EFILE_EFFECTIVE_DT": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "EFILE_STATUS_CODE": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "FA_OPTION_CODE": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "MODIFY_BY": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "MODIFY_DT": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "OPERATOR_NAME": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "OPERATOR_NO": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "OPERATOR_SB639_FLAG": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "OPERATOR_TAX_CERT_FLAG": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "P5_LAST_FILED_DT": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "P5_STATUS_CODE": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
            "RECORD_STATUS_CODE": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
            },
        }
    }
}
