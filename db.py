import mysqlConnector


class Db:
    def __init_(self):
        return

    def create(self):
        ## Creates database table and fields
        with mysqlConnector.db() as db_obj:
            cur = db_obj.select("CREATE TABLE `papers` ("
                                "  `id` int NOT NULL AUTO_INCREMENT,"
                                "  `search` varchar(256) CHARACTER SET utf8 NULL,"
                                "  `authors` varchar(1024) CHARACTER SET utf8 NULL,"
                                "  `year` int NULL,"
                                "  `title` varchar(1024) CHARACTER SET utf8 NULL,"
                                "  `source` varchar(1024) CHARACTER SET utf8 NULL,"
                                "  `summary` varchar(4096) CHARACTER SET utf8 NULL,"
                                "  `keywords` varchar(1024) CHARACTER SET utf8 NULL,"
                                "  `series` varchar(1024) CHARACTER SET utf8 NULL,"
                                "  `content` varchar(256) CHARACTER SET utf8 NULL,"
                                "  `url` varchar(1024) CHARACTER SET utf8 NULL,"
                                "  `email` varchar(1024) CHARACTER SET utf8 NULL,"
                                "  PRIMARY KEY (`id`)"
                                ") ENGINE=InnoDB")

    def savePage(self, data_array, search):
        ## Inserts values into database
        for data_dict in data_array:
            with mysqlConnector.db() as db_obj:
                db_obj.insert("papers", {
                    'search': search,
                    'authors': data_dict['authors'],
                    'year': data_dict['year'],
                    'title': data_dict['title'],
                    'source': data_dict['source'],
                    'summary': data_dict['summary'],
                    'keywords': data_dict['keywords'],
                    'series': data_dict['series'],
                    'content': data_dict['content'],
                    'url': data_dict['url'],
                    'email': data_dict['email'],
                })
