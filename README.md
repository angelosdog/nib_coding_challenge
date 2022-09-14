How to run on Windows:

1. Download all files
2. In a terminal: cd <FILEPATH_OF_DOWNLOADED_FILES>
3. python main.py

The program takes in the data from data.json, so to test different scenarios, replace the contents of data.json with different data.

- The data.json is not validated as part of the program, so if there is invalid data, such as having "quantityOnHand": "Abc", then it won't work.
- "Unfulfillable", "Pending", and "Fulfilled" order statuses are case-sensitive, I left it this way, but if necessary, we could easily just change the string comparisons to be case-insensitive with the .capitalize method.
- Orders are fulfilled in priority of "orderId". This was done assuming that the id generator increments after each order has been placed. Perhaps sorting by "dateCreated", and then by "orderId" (for orders placed with the same timestamp) would be how we should fulfill orders if this assumption is inaccurate.
