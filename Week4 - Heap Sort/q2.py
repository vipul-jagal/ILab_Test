# You have two order books ( ask order book and bid order book), where you will have to store all your orders.
# There can be two types of orders, ask order (sell) and bid orders (buy orders). Write a function to accomplish below functions.
# you have given a list of orders which will have both bid and ask orders. You have to add those orders in the order book.
# AddToOrderBook ( orders_list, AskOrderBook, BidOrderBook) -> returns both modified order books.
# you have given market ask and bid prices, by the help of which you have to execute the orders. executing the bid order that are higher than the given market ask value and the ask order that are lesser than the given market bid value.
# ExecuteOrders( marketAskPrice, marketBidPrice, AskOrderBook, BidOrderBook) -> list of ordered executed and modified order books.
# Assume every order amount should be 1 i.e. you can only buy one stock or sell one stock per order. Write a logic behind every function using the function that you have created in the above function, i.e. try to find a solution of the problem using heap concepts.



import heapq

# Function to add orders to the order book
def addToOrderBook(orders_list, ask_order_book, bid_order_book):
    for order in orders_list:
        price, order_type = order
        if order_type == 'Ask':
            heapq.heappush(ask_order_book, price)
        elif order_type == 'Bid':
            heapq.heappush(bid_order_book, -price)
    return ask_order_book, bid_order_book

# Function to execute orders based on market prices
def executeOrders(marketAskPrice, marketBidPrice, ask_order_book, bid_order_book):
    executed_orders = []
    modified_ask_order_book = []
    modified_bid_order_book = []

    # Execute Bid orders with prices higher than or equal to marketAskPrice
    while bid_order_book and -bid_order_book[0] >= marketAskPrice:
        executed_orders.append(('Bid', -heapq.heappop(bid_order_book)))

    # Execute Ask orders with prices lower than or equal to marketBidPrice
    while ask_order_book and ask_order_book[0] <= marketBidPrice:
        executed_orders.append(('Ask', heapq.heappop(ask_order_book)))

    # Reconstruct the modified order books
    while bid_order_book:
        modified_bid_order_book.append(-heapq.heappop(bid_order_book))
    while ask_order_book:
        modified_ask_order_book.append(heapq.heappop(ask_order_book))

    return executed_orders, modified_ask_order_book, modified_bid_order_book

# Example usage:
ask_order_book = []
bid_order_book = []

orders_list = [(100, 'Bid'), (105, 'Bid'), (95, 'Ask'), (98, 'Ask')]
ask_order_book, bid_order_book = addToOrderBook(orders_list, ask_order_book, bid_order_book)

marketAskPrice = 97
marketBidPrice = 102

executed_orders, modified_ask_order_book, modified_bid_order_book = executeOrders(marketAskPrice, marketBidPrice, ask_order_book, bid_order_book)

print("Executed Orders:", executed_orders)
print("Modified Ask Order Book:", modified_ask_order_book)
print("Modified Bid Order Book:", modified_bid_order_book)
