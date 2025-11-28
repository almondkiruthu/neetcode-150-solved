class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        
        hand.sort()
        # Build the freq dict of the card numbers
        count = {}
        for i in range(n):
            if hand[i] in count:
                count[hand[i]] += 1
            else:
                count[hand[i]] = 1

        for i in range(n):
            card = hand[i]

            # Only use available cards as starting point
            if count[card]:

                # Consume card immediately
                count[card] -= 1
                
                # Skip the 0, group
                for j in range(1, groupSize):
                    nextCard = card + j
                    # get the nexcard freq, else initialize it to zero
                    if nextCard in count and count[nextCard] > 0:
                        count[nextCard] -= 1
                    else:
                        return False
        return True


            