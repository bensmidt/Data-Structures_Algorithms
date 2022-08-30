

class Solution (object): 

    def length_longest_substring(self, s): 
        """Returns the length of the longest substring in string s that doesn't have repeating characters
        Input
        - s: a string
        Returns
        - longest_substring: a string that is the longest substring in s without repeating characters
        """

        if len(s) == 0: 
            return ""

        char_idcs = {}
        longest_substring = ""
        start = 0
        end = 0

        while end < len(s): 
            # found repeat character
            if s[end] in char_idcs: 

                # check previous substring was the largest
                if (end - start) > len(longest_substring): 
                    longest_substring = s[start:end]

                # remove all characters before and including the first occurence of the character
                while start < end: 
                    char = s[start]
                    del char_idcs[char]

                    # found first occurence, break
                    if char == s[end]: 
                        start += 1
                        break
                    start += 1

            # add character to dictionary and keep moving window
            elif s[end] not in char_idcs: 
                char_idcs[ s[end] ] = 1
                end += 1
        
        # check if final substring is longest
        if (end - start) > len(longest_substring): 
                    longest_substring = s[start:end]
    
        return longest_substring


def test(s, ans): 
    Sol = Solution()
    longest_substring = Sol.length_longest_substring(s)
    assert longest_substring == ans

def main(): 
    test("abcabcbb", "abc")
    test("bbbbb", "b")
    test("b", "b")
    test("", "")
    test("pwwkew", "wke")
    print("Passed All Test Cases!")

if __name__ == "__main__": 
    main()
            