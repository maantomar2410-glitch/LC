class Solution:

    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        time = 0

        while tickets[k] > 0:
            min_val = min(x for x in tickets if x > 0)

            if tickets[k] == min_val:
                for i in range(len(tickets)):
                    if tickets[i] > 0:  
                        if i <= k:
                            time += min_val  
                        else:
                            time += (min_val - 1)  

                tickets[k] = 0 
                break

            else:
                active_len = sum(1 for x in tickets if x > 0)
                time += min_val * active_len

                for i in range(len(tickets)):
                    if tickets[i] > 0:
                        tickets[i] -= min_val

        return time