class OddNumber(object):
    def sumOdd(self,n):
        odd_numbers = []
        for number in range(n*2):
            if number % 2 != 0 and len(odd_numbers)!=n:
                odd_numbers.append(number)
                
        total_sum = sum(odd_numbers)
        return total_sum
                
tt=OddNumber()
print(tt.sumOdd(5))


# optimal solution
# class OddNumber:
#     def sumOdd(self, n):
#         return n * n

# # Example usage:
# tt = OddNumber()
# print(tt.sumOdd(3))  # Output: 9
            
            
        