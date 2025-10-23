# 134. Gas Station
https://leetcode.com/problems/gas-station/description/?envType=study-plan-v2&envId=top-interview-150

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

### Example 1:

```
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
```

### Example 2:

```
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
```

### Constraints:

```
n == gas.length == cost.length
1 <= n <= 105
0 <= gas[i], cost[i] <= 104
```

## Code

```python
class Solution:
    def canCompleteCircuit(self, gas, cost):
        total_gas = 0
        total_cost = 0
        current_gas = 0
        start_index = 0

        # Traverse through all the stations
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            current_gas += (gas[i] - cost[i])

            # If current_gas goes negative, reset the start station
            if current_gas < 0:
                current_gas = 0
                start_index = i + 1  # New start station is the next one

        # If total gas is less than total cost, it's impossible to complete the circuit
        if total_gas < total_cost:
            return -1

        return start_index
```

### Explanation
When current_gas becomes negative: This means that starting from the current start_index to the current station i has exhausted our gas and we can't reach station i + 1. This is a crucial observation, because:

If we can’t make it from station start_index to station i, then we definitely cannot make it from any station between start_index and i to station i + 1. This is because starting from a station in this range (let's call it j) would only have less gas than starting from start_index. Thus, the only viable candidate for the next starting point is the station after i, i.e., i + 1.
Why resetting current_gas to 0 works:

When we reset current_gas to 0, we are essentially discarding any information about the route from start_index to i, because we've already concluded that it's impossible to continue from start_index. However, we don't need to re-evaluate those stations when we move our starting point forward because:

If starting from start_index didn't work, we know for sure that all stations from start_index to i (inclusive) cannot serve as valid starting points either. This is because of the nature of the problem: if we can't reach station i from start_index, then starting from any intermediate station between start_index and i won't work either — they will only have less gas, not more.
Why recalculating the entire circle is unnecessary:

Once we decide that a certain portion of the route (from start_index to i) is not viable, we move the start index forward to i + 1 and begin checking from that station. We can be sure that we only need to focus on this new range, because any prior station that failed to meet the requirements doesn't affect future calculations.
The important part here is that the total gas is still balanced with the total cost. We only reset current_gas when it's negative, but as long as the total gas is greater than or equal to the total cost after we complete the loop, we are guaranteed that there exists a solution. If starting from a new station works, we can successfully complete the circle.