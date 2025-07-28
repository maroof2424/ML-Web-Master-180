

def main():
    # Task 1 
    def generatr_even(start:int,end:int)-> list[int]:
        even_number = []
        for i in range(start,end):
            if i % 2 == 0:
                even_number.append(i)
        return even_number
    # even_num = generatr_even(1,50)
    # for num in even_num:
    #     print(num) 
    # Task 2
    def extract_vowels(text: str) -> list[str]:
        vowels = "aeiouAEIOU"
        return [char for char in text if char in vowels]

    # sentence = input("\nEnter The Text: ")
    # print(extract_vowels(sentence))
    # Task 3
    def multiplication_table(n:int,to:int=10):
        return [n * i for i in range(1, to+1)]
    print(multiplication_table(12,10))
    # task 4
    def is_prime(n:int)->bool:
        if n < 2:
            return False
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    numbers = list(range(1, 51))
    prime_numbers = [num for num in numbers if is_prime(num)]
    print("\nPrime numbers from 1 to 50:", prime_numbers)
if __name__ == "__main__":
    main()