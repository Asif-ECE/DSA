class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0
        
        INF = sys.maxsize
        previous = [INF] * n
        current = [INF] * n
        previous[src] = 0
        
        for i in range(1, k + 2):
            current[src] = 0
            for flight in flights:
                previous_flight, current_flight, cost = flight

                if previous[previous_flight] < INF:
                    current[current_flight] = min(current[current_flight],
                                                  previous[previous_flight] + cost)
                    
            previous = current.copy()
            
        return -1 if current[dst] == INF else current[dst]
