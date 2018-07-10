import pycountry
import mysqlConnector

# class Country:
#     def getCountry(self, email):

with mysqlConnector.db() as db_obj:
    cur = db_obj.select("SELECT * FROM `papersCleanEmailCopy` WHERE `email` LIKE '%@%' ORDER BY `id` ASC")
    returnValue = []

    for row in cur:
        id = row["id"]
        email = row["email"]
        suffix = email.split(".")[-1]

        ## US universities special case
        if suffix == "edu":
            suffix = "us"
            ## Get specific university suffix option
            # suffix = email.split("@")[1].split(".")[0]

        try:
            country = pycountry.countries.get(alpha_2=suffix.upper())
        except:
            continue

        data_dict = {
            'id': id,
            'email': email,
            'suffix': suffix,
            'country': country.name,
        }
        returnValue.append(data_dict)

    for value in returnValue:
        cur.execute("UPDATE `papersCleanEmailCopy` SET `country` = %s WHERE id = %s ", (value["country"], value["id"]))
