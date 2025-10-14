class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert binary strings to integers, sum them, then convert back to binary
        sum_decimal = int(a, 2) + int(b, 2)
        return bin(sum_decimal)[2:]  # bin() returns a string like '0b101', so we skip '0b'

# Example Usage:
sol = Solution()
print(sol.addBinary("11", "1"))      # Output: "100"
print(sol.addBinary("1010", "1011")) # Output: "10101"
