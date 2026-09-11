class Solution:
    # section::section-20::start
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False

        ref = { '}':'{', ')':'(', ']':'['}
        stack = []
        for p in s:
            if p in ref.values():
                stack.append(p)
            else:
                if not stack or stack.pop() != ref[p]:
                    return False

        # towards end stack muct be empty
        if len(stack) != 0:
            return False

        return True
    # section::section-20::end


    # section::decodeString::start
    # s = "2[abc]3[cd]ef", 3[a2[c]] nested
    def decodeString(self, s: str) -> str:
        print("=============== decodeString ============================")
        stack = []
        for c in s:
            if c != ']':  # could be out of these 2, -->  alpha-numeric or '['
                print("")
                stack.append(c) # 2[abc --> will have 2 part : `2` and `abc`, separated by [
            else: # ']'
                print("\nEncountered `]` ending bracket..." , end= "")
                chars = ''; nxt = ''

                # STEP-1 : find chars after '['
                print("\n\t1. Popped char till starting bracket: ", end= " ")
                while True and stack:
                    nxt = stack.pop()
                    if nxt == '[': break
                    else:  chars =  nxt + chars
                print(chars, end= "")

                # STEP-2 : find product before '['
                print("\n\t2. Get multiplier: ", end= " ")
                product = ''
                while True and stack:
                    nxt = stack.pop()
                    if nxt.isdigit():
                        product = nxt + product
                    elif nxt.isalpha() or nxt == '[':
                        stack.append(nxt)
                        break
                print(product)

                # prepare result
                print(f"\t >> {product} * {chars} = {int(product) * chars}")
                product = int(product) * chars # 2 * abc
                for char in product : stack.append(char) # put back to stack

            for i in stack: print(f"{i}", end = ", ")

        res = "".join(x for x in stack)
        print(f"\n⭐final result: {res}")
        return res
    # section::decodeString::end

    # ==================================
    # section::section-32::start
    def longestValidParenthesis(self, s: str) -> int:
        print(f"\n=============== longestValidParentheses {s} ============================")
        pass

    # section::section-32::end

# =========================
# TEST
# =========================
def isvalidParenthesis_test():
    Solution().isValid("()[]{}")

def decodeString_test():
    Solution().decodeString("2[abc]3[cd]ef")
    Solution().decodeString("3[a]2[bc]")
    Solution().decodeString("3[a2[c]]")
    Solution().decodeString("10[a]")

def longestValidParenthesis_test():
    Solution().longestValidParenthesis("())))")
    Solution().longestValidParenthesis("((()()())")
    Solution().longestValidParenthesis("()())()")

if __name__ == "__main__":
    #isvalidParenthesis_test()
    #decodeString_test()
    longestValidParenthesis_test()

# ==============================
#  Console output
# ==============================



# section::decodeStringConsole::start
"""
    3, 
3, [, 
3, [, a, 
3, [, a, 2, 
3, [, a, 2, [, 
3, [, a, 2, [, c, 
Encountered ] ending bracket... 
	1. Popped char till starting bracket: c
	2. Get multiplier:  2
	 >> 2 * c = cc
3, [, a, c, c, 
Encountered ] ending bracket... 
	1. Popped char till starting bracket: acc
	2. Get multiplier:  3
	 >> 3 * acc = accaccacc
a, c, c, a, c, c, a, c, c, 
⭐final result: accaccacc
"""
# section::decodeStringConsole::end