How to run on Windows:

1. Download all files
2. In a terminal: cd <FILEPATH_OF_DOWNLOADED_FILES>
3. python main.py
4. Follow the prompts in the console

The program takes in the data from data.json, so to test different scenarios, replace the contents of data.json with different data.

- The data.json is not validated as part of the program, so if there is invalid data, such as having "quantityOnHand": "Abc", then it won't work. This also holds true for the productIds being entered to process - they must be integers.
- "Unfulfillable", "Pending", and "Fulfilled" order statuses are case-sensitive. If necessary, we could easily just change the string comparisons to be case-insensitive with the .capitalize method.
- The quantities of each product in an order are modified based on how many products they can be given. If there's only enough stock to partially fill an order, then that order will reserve whatever is left in stock.
   - This means that if there are not enough products in stock to fully satisfy Order#1123, but it would have been enough for Order#1124, then both orders will be marked as 'Unfulfillable'.
   - This behaviour is how I interpreted this AC: 'If an order cannot be fulfilled the order is changed to status “Unfulfillable” to be flagged for review **but other orders within the order run are processed**.' But in out of scope, it says: 'if the stock is not available to fulfil an order, **then order should not be processed**'. In a working environment, I would ask for clarification on what should be done, but I have assumed that this is the expected behaviour for this assessment.
   - In other words, I took **but other orders within the order run are processed** to mean that the other products within an order should be processed, and not to mean that we should just abandon that order.
- Orders are fulfilled in priority of "orderId". This was done assuming that the id generator increments after each order has been placed. Perhaps sorting by "dateCreated", and then by "orderId" (for orders placed with the same timestamp) would be how we should fulfill orders if this assumption is inaccurate.
- For the purposes of the coding challenge, a lot of information from the json is unused. I have left them in for now.
