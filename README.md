## Furman Now!: Serverside ##

Furman Now! relies heavily on the gathering of information from various on-campus sources to keep information up-to-date and correct for students.
These scrapers, and the classes that are used to augment them, are the main ways that this information is gathered. 

Most scrapers (though as of 3/2/2023, not all) are built by extending the `Scraper` abstract class. `Scraper` requires a child class to implement the `_pull(self)`
helper funciton, which is then accessed by running the `tryPull()` function on an initialized verion of the class. `tryPull()` returns a list of `Insertable` 
objects. If the `Scraper` fails, the instance records it internally, and can be checked using the `didFail()` method. 

Most dataclasses extend the `Insertable`, `Selectable`, and/or `Clearable` abstract classes, which allow for easier insertion into a specified table. 
Extending the former (and most used) of these classes requires the implementation of `insertInto(table)`. Each of these is a descendant of `Queriable`, which helps to handle database queries.

The scrapers run on the Furman CS Department servers' `cronjob` at varying intervals, from every ~20 seconds for `ShuttleScraper` to once a week for `HoursScraper`. 
