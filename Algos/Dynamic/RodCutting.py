
from cmath import inf

class Solution (object):

  def cut_rods_top_down (self, prices, rod_length): 
    """Returns a list of optimal prices for cutting rods up to a rod length of n
    Inputs: 
    - prices: List of integers containing the price for wood of length i
    - rod_length: integer representing the maximum desired length of a rod
    Returns: 
    - optimal_prices: List of integers representing the optimal price for a rod of length i
    """

    optimal_prices = [0] * (rod_length + 1)
    self.cut_rods_top_down_helper (prices, rod_length, optimal_prices)
    return optimal_prices
    
  def cut_rods_top_down_helper (self, prices, rod_length, optimal_prices):
    """Returns the optimal price for cutting a rod with length rod_length and prices
    Inputs: 
    - prices: List of integers containing the price for wood of length i
    - rod_length: integer representing the length of the desired rod
    Returns: 
    - best_price: integer representing the best price for a rod of length rod_length
    """
    # rod's price in optimal prices list 
    if optimal_prices[rod_length] > 0: 
      return prices[rod_length]

    # rod_length is zero
    elif rod_length ==  0: 
      return 0
    
    # compute optimal price
    else: 
      best_price = prices[rod_length]
      for i in range(1, rod_length): 
        cur_price = self.cut_rods_top_down_helper (prices, rod_length-i, optimal_prices) + self.cut_rods_top_down_helper (prices, i, optimal_prices)
        best_price = max(best_price, cur_price)

      optimal_prices[rod_length] = best_price
      return best_price
  
  def cut_rods_bottom_up (self, prices): 
    """Returns a list of optimal prices for cutting rods up to a rod length of n
    Inputs: 
    - prices: List of integers containing the price for wood of length i
    - optimal_prices: List of integers representing the optimal price for a rod of length i
    """
    optimal_prices = []
    
    for i in range(len(prices)):
      # set best price to price of whole rod 
      optimal_prices.append(prices[i])
      best_price = prices[i]
      # check for better prices
      for j in range(i): 
        best_price = max(best_price, optimal_prices[i-j] + optimal_prices[j])
      # add best price 
      optimal_prices[i] = best_price
    
    return optimal_prices

def test (prices, answers): 
  Sol = Solution()

  optimal_prices = Sol.cut_rods_top_down (prices, len(prices) - 1) 
  for i in range(len(optimal_prices)): 
    assert optimal_prices[i] == answers[i]

  optimal_prices = Sol.cut_rods_bottom_up(prices)
  for i in range(len(optimal_prices)): 
    assert optimal_prices[i] == answers[i]

def main(): 
  Sol = Solution()

  # Test Case 1
  prices = [0, 1, 5, 8, 9, 10, 17, 17, 20]
  answers = [0, 1, 5, 8, 10, 13, 17, 18, 22]
  test(prices, answers)

  # Test Case 2
  prices = [0, 1, 3, 4, 5, 7, 9, 10, 11]
  answers = [0, 1, 3, 4, 6, 7, 9, 10, 12]
  test(prices, answers)

  print("All Test Cases Passed!")
  

if  __name__ == "__main__": 
  main() 
