#defining silent auctionn 
def silent_auction(bids1):
    highestBid = 0
    winner = ""
    #now we need a for loop for reading name and value from bids dictionary
    for names, values in bids1.items():
        if values > highestBid or ( values == highestBid and bids1[winner] > values):
            print("Previous higest bid:",highestBid)
            print("Previous winner", winner)
            #assigning the highest bid
            highestBid = values
            print("current higest bid:", highestBid)
            #assingning the winner
            winner = names
            print("current winner's name:", winner)
    return winner,highestBid



#defining main
def main():
    try:    
        #take input for number of participants.
        N = int(input("Number of participants"))
        #defining a dictinary
        bids = {}
        #making a loop to take iputs for names and values to stroe in the dictionary
        for _ in range(N):
            #take input from the user for the name and value and storeing in the dictionaery in a name value pair
            name = input("Enter name:").strip()
            value = int(input("Enter your bid amount:").strip())
            #storing in dictionary as name value pair
            bids[name]=value

        #calling silent auction function
        NameOfAuctionWinner,WinnerBid = silent_auction(bids)
        #print the winners name
        print("Winner name:",NameOfAuctionWinner)
        print("winner Bid:",WinnerBid)

    except ValueError:
        print("Enter a valid input") 



#calling main and using == because this is a compareasion
if __name__ == "__main__":
    main()