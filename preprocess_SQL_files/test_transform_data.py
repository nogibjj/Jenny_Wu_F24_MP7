from transform_data import transform

"""This file takes the csv data and converts it into a database/.db file"""


def test_transform():
    transform_result = transform(dataset="data/nypd_shooting.csv",
    db_name="nypd_shooting.db",
    table_name="nypd_shooting")
    assert transform_result is not None


if __name__ == "__main__":
    test_transform()