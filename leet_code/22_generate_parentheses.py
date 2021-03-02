# -----------------------------------------
# Original
# -----------------------------------------
# def generateParenthesis(n):
#     combinations = []
#     for pair_count in range(1, n + 1):
#         if pair_count == 1:
#             combinations = ['()']
#         else:
#             store_dict = {}
#             for combination in combinations:
#                 for index in range(0, len(combination) + 1):
#                     if index == 0:
#                         new_combination = '()' + combination
#                     elif index == len(combination):
#                         new_combination = combination + '()'
#                     else:
#                         new_combination = combination[:index] + '()' + combination[index:]
#
#                     if store_dict.get(new_combination):
#                         continue
#                     else:
#                         store_dict[new_combination] = True
#
#             combinations = list(store_dict.keys())
#
#     return combinations

# -----------------------------------------
# Backtracking
# -----------------------------------------
def backtrack(output_array, current_string, open_bracket_count, close_bracket_count, pair_count):
    if len(current_string) == pair_count * 2:
        output_array.append(current_string)
    else:
        if open_bracket_count < pair_count:
            output_array = backtrack(output_array, current_string + '(', open_bracket_count + 1, close_bracket_count, pair_count)
        if close_bracket_count < open_bracket_count:
            output_array = backtrack(output_array, current_string + ')', open_bracket_count, close_bracket_count + 1, pair_count)

    return output_array

def generateParenthesis(n):
    return backtrack([], '', 0, 0, n)
