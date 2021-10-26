from bson.json_util import dumps, loads
from datetime import datetime
from db_init import assistant_db, abonent_collection


import json
from datetime import datetime, timezone
from datetime import timedelta
from queries import create_abonent, delete_abonent, update_abonent, read_abonents


def query_by_range_of_dates(from_date, to_date):

    from_date = datetime.strptime(from_date, '%Y-%m-%d')
    to_date = datetime.strptime(to_date, '%Y-%m-%d')

    criteria = {"birthday": {"$gte": from_date, "$lte": to_date}}

    return json.loads(dumps(assistant_db.abonent_collection.find(criteria)))


if __name__ == "__main__":
    #   from_date = '1970-09-15'
    #    to_date = '2021-09-15'
    #    """from_date = datetime.strptime(from_date, '%Y-%m-%d')
    #    to_date = datetime.strptime(to_date, '%Y-%m-%d')"""#
    #
    #    # (query_by_range_of_dates(from_date, to_date))
    #    res = abonent_collection.find({"name": {$regex: / ar/}})
    #    print(json.loads(dumps(res)))

    """res = create_abonent(
        collection=abonent_collection,
        name="YYYYYYYY ХХХХ",
        address="TTT, TTT< gggggg",
        phones=["+380001122", "+12223344"],
        emails=["fff@aaa.bb.com"],
        note="test 1"
    )"""

    """    print("-" * 100)
    res = json.loads(dumps(abonent_collection.find(
        {"name": "Роксолана Дрозд"})))
    print(res)
    for r in res:
        a = r["_id"]
        print(type(a))
        print(r["_id"])
    print("-" * 100)"""
    # print(res)

    print("-" * 100)
    #print(abonent_collection.find_one({"name": "YYYYYYYY ХХХХ"}))
    #update_abonent(abonent_collection, abonent_collection.find_one({"name": "YYYYYYYY ХХХХ"})["_id"], name="BOBA")
    res = read_abonents(abonent_collection, name="BOBA")

    for r in res:
        print(r, type(r))
        print(r["name"])
