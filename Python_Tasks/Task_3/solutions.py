# Q1. Find the Frequency of Each Word in a Sentence
def word_frequency(sentence):
    result = {}

    for word in sentence.split():
        result[word] = result.get(word, 0) + 1

    return result


# Q2. Find the Frequency of Each Character in a Word
def character_frequency(word):
    result = {}

    for char in word:
        result[char] = result.get(char, 0) + 1

    return result


# Q3. Find the First Non-Repeating Character
def first_non_repeating_character(word):
    counts = character_frequency(word)

    for char in word:
        if counts[char] == 1:
            return char

    return None


# Q4. Check Whether Two Strings Are Anagrams
def are_anagrams(s1, s2):
    return character_frequency(s1) == character_frequency(s2)


# Q5. Find the First Repeating Character
def first_repeating_character(text):
    seen = set()

    for char in text:
        if char in seen:
            return char

        seen.add(char)

    return None


# Q6. Move All Zeros to the End
def move_zeros_to_end(nums):
    non_zeros = [num for num in nums if num != 0]
    zeros = [num for num in nums if num == 0]

    return non_zeros + zeros


# Q7. Find the Second Highest Distinct Number
def second_highest_distinct(nums):
    unique_nums = sorted(set(nums), reverse=True)

    if len(unique_nums) < 2:
        return None

    return unique_nums[1]


# Q8. Remove Duplicates Without Changing Order
def remove_duplicates(nums):
    result = []
    seen = set()

    for num in nums:
        if num not in seen:
            result.append(num)
            seen.add(num)

    return result


# Q9. Find the Missing Number from 1 to N
def find_missing_number(nums, n):
    expected_sum = n * (n + 1) // 2

    return expected_sum - sum(nums)


# Q10. Find Two Numbers Whose Sum Equals a Target
def two_sum_first_pair(nums, target):
    for j in range(len(nums)):
        for i in range(j):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]

    return []


# Q11. Find the Number Closest to Zero
def closest_to_zero(nums):
    if not nums:
        return None

    return min(nums, key=lambda x: (abs(x), -x))


# Q12. Find Common Elements Between Two Lists
def common_elements(list1, list2):
    values = set(list2)
    result = []
    seen = set()

    for item in list1:
        if item in values and item not in seen:
            result.append(item)
            seen.add(item)

    return result


# Q13. Rotate a List to the Right by K Positions
def rotate_right(nums, k):
    if not nums:
        return []

    k = k % len(nums)

    if k == 0:
        return nums.copy()

    return nums[-k:] + nums[:-k]


# Q14. Find the Maximum Sum of Two Consecutive Elements
def max_consecutive_sum(nums):
    return max(
        nums[i] + nums[i + 1]
        for i in range(len(nums) - 1)
    )


# Q15. Find All Unique Pairs Whose Sum Equals a Target
def all_pairs_sum(nums, target):
    pairs = set()

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pair = tuple(sorted((nums[i], nums[j])))
                pairs.add(pair)

    return [list(pair) for pair in sorted(pairs)]