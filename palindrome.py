def isPalindrome(s: str) -> bool:
    cleaned = []
    for ch in s:
        if ch.isalnum():
            cleaned.append(ch.lower())
    
    left = 0

    right = len(cleaned) - 1

    while left < right:
          if cleaned[left] != cleaned[right]:
               return False
          
          left += 1
          right -= 1

    return True

def main():
     for s in ["race car", "HANNAH", "radar", "A man, a plan, a canal, Panama"]:
          if isPalindrome(s):
               print(s, "is a Palindrome")
          else:
               print(s, "ain't no Palindrome, u suck!")

if __name__ == "__main__":
     main()
