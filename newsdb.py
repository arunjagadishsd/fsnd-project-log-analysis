import psycopg2


def top_articles():
    """
    * This function is to get the top articles of all the time
    """
    db_connect = psycopg2.connect("dbname=news")
    cursor = db_connect.cursor()
    query_1 = """
        SELECT articles.title, count(log.path) as view_counts
        FROM articles, log
        WHERE articles.slug = replace(log.path,'/article/','')
        GROUP BY articles.title
        order by view_counts desc
        limit 3;
        """
    cursor.execute(query_1)
    results = cursor.fetchall()
    print "\nThe Top 3 Articles Are:\n"
    for i, j in results:
        print '"{}" - {}'.format(i, j)
    db_connect.close()


def top_authors():
    """
    * This function is to get the top authors of all the time
    """
    db_connect = psycopg2.connect("dbname=news")
    cursor = db_connect.cursor()
    query_2 = """
    SELECT authors.name, count(log.path) as view_counts
    FROM articles, log, authors
    WHERE articles.slug = replace(log.path,'/article/','')
    AND articles.author = authors.id
    GROUP BY authors.name
    order by view_counts desc;
        """
    cursor.execute(query_2)
    results = cursor.fetchall()
    print("\nThe Authors sorted based on views:\n")
    for i, j in results:
        print('{} - {}'.format(i, j))
    db_connect.close()


def errors():
    """
    * This function is to get the top errors in each day
    """
    db_connect = psycopg2.connect("dbname=news")
    cursor = db_connect.cursor()
    query_2 = """
    SELECT no_of_errors.time,(cast(no_of_errors.error_codes as float)/
        cast(no_of_requests.no_of_views as float))*100
    FROM no_of_requests, no_of_errors
    WHERE no_of_requests.time = no_of_errors.time
    AND (cast(no_of_errors.error_codes as float)/
        cast(no_of_requests.no_of_views as float))*100 > 1;
        """
    cursor.execute(query_2)
    results = cursor.fetchall()
    print "\nThe day with error more than 1 percentage:\n"
    for i, j in results:
        print '{} - {}%'.format(i, round(j, 1))
    db_connect.close()


top_articles()
top_authors()
errors()
