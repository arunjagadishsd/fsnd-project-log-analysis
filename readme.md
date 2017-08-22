# Read Me
## Introduction:
This is a program to retrieve analytics data from a news website such as popular authors, popular articles and errors.
## Function
There is a file named newsdb.py, it's the file that will retrieve the analytics data from the news website.

## Technologies Required:
* Python 3
* Virtual Box
* Vagrant
#### How to install Python 3:
* Visit this [link](https://www.python.org/downloads/) and download and install the latest version of python 3.
* To check the instalation open a terminal or cmd and type `python --version`. This will display the version of python else check your installation again.
#### How to install Virtual Box:
* Visit this [link](https://www.virtualbox.org/wiki/Downloads  "link") and dowload the latest verion of virtual box.
#### How to install Vagrant:
* Visit this [link](https://www.vagrantup.com/downloads.html  "link") and dowload the latest verion of vagrant.


### Using The Terminal
* You can download and unzip this file: [FSND-Virtual-Machine.zip](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip) This will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder.

* Alternately, you can use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm.

* Either way, you will end up with a new directory containing the VM files. Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory:
* From your terminal, inside the vagrant subdirectory, run the command vagrant up. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.

* When vagrant up is finished running, you will get your shell prompt back. At this point, you can run vagrant ssh to log in to your newly installed Linux VM!

* Next, download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

* To load the data, use the command `psql -d news -f newsdata.sql`.

## Views Present
There are two views:
* no_of_requests (This view is to get the total no of views in a particular day.)
* no_of_errors (This view is to get the total no of errors in a particular day.)

#### To The Views Needed :
* Go to vagrant folder in terminal
* Type `vagrant up` then `vagrant ssh` and `psql news`
* Type the following SQL Commands
```sql
CREATE VIEW no_of_requests as
SELECT count(status) as no_of_views, CAST(time as date)
FROM log
GROUP BY CAST(time as date);
```
```sql
CREATE VIEW no_of_errors as
SELECT count(status) as error_codes, CAST(time as date)
FROM log
WHERE NOT status ILIKE '200%'
GROUP BY CAST(time as date);
```


## Operating Instruction
* Go to vagrant folder in terminal
* Type `vagrant up` then `vagrant ssh`
* Navigate to the project folder using `cd` then Type `python newsdb.py`
