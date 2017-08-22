# Read Me
## Introduction:
This is a program to retrieve analytics data from a news website such as popular authors, popular articles and errors.
## Function
There is a file named newsdb.py, it's the file that will retrieve the analytics data from the news website.
## Views Present
There are two views:
* no_of_requests
* no_of_errors
### no_of_requests:
This view is to get the total no of views in a particular day.
#### To Create this view :
```sql
CREATE VIEW no_of_requests as
SELECT count(status),CAST(time as date)
FROM log
GROUP BY CAST(time as date);
```
### no_of_errors:
This view is to get the total no of errors in a particular day.
#### To Create this view :
```sql
CREATE VIEW no_of_errors as
SELECT count(status) as error_codes, CAST(time as date)
FROM log
WHERE NOT status ILIKE '200%'
GROUP BY CAST(time as date);
```


## Operating Instruction
### Using The Terminal
* Go to the folder in terminal type `python newsdb.py`

### Using the python IDLE:
* Open the newsdb.py file
* Then select run from the idle menu
* click `Run Module` from the dropdown list.
