def get_patterns(patterns_string):
    patterns = []
    pattern = ''
    pattern_cursor = 0
    while pattern_cursor < len(patterns_string):
        if pattern_cursor + 1 < len(patterns_string) and patterns_string[pattern_cursor + 1] == '*':
            if len(pattern) > 0:
                patterns.append(pattern)
            patterns.append(f"{patterns_string[pattern_cursor]}*")
            pattern = ''
            pattern_cursor += 2
            continue
        pattern += patterns_string[pattern_cursor]
        pattern_cursor += 1
    if len(pattern) > 0:
        patterns.append(pattern)

    simplified_patterns = []
    tmp_stored_patterns = []
    for pattern_index in range(0, len(patterns)):
        pattern = patterns[pattern_index]

        if '*' in pattern:
            if '.*' in tmp_stored_patterns:
                continue
            else:
                if pattern == '.*':
                    tmp_stored_patterns = ['.*']
                elif len(tmp_stored_patterns) == 0:
                    tmp_stored_patterns.append(pattern)
                elif pattern != tmp_stored_patterns[-1]:
                    tmp_stored_patterns.append(pattern)
        else:
            if len(tmp_stored_patterns) > 0:
                simplified_patterns += tmp_stored_patterns
                tmp_stored_patterns  = []
            simplified_patterns.append(pattern)
    if len(tmp_stored_patterns) > 0:
        simplified_patterns += tmp_stored_patterns

    return simplified_patterns

def sub_s_matched_non_asterisk_pattern(sub_s, pattern):
    if len(sub_s) != len(pattern):
        return False

    matched = False
    for char_index, char in enumerate(sub_s):
        if char != pattern[char_index] and pattern[char_index] != '.':
            return False
        else:
            matched = True

    return matched

def sub_s_matched_indexes_for_asterisk_sign_pattern(start_index, end_index, sub_s, pattern):
    matched_indexes_lists = []
    if pattern[0] == '.':
        end_index = min(end_index + 1, start_index + len(sub_s))
        return [list(range(start_index, end_index))]
    else:
        matched_indexes_list = []
        for sub_s_index in range(0, len(sub_s)):
            if sub_s_index + start_index > end_index:
                break

            if sub_s[sub_s_index] == pattern[0]:
                matched_indexes_list.append(sub_s_index + start_index)
            elif len(matched_indexes_list) > 0:
                matched_indexes_lists.append(matched_indexes_list)
                matched_indexes_list = []

        if len(matched_indexes_list) > 0:
            matched_indexes_lists.append(matched_indexes_list)

    return matched_indexes_lists

def get_pattern_index_matchable_s_indexes_lists_mapping(s, patterns):
    pattern_index_matchable_s_indexes_lists_mapping = {}

    # get possible matched indexes of non-asterisk sign patterns
    s_cursor = 0
    for pattern_index, current_pattern in enumerate(patterns):
        pattern_index_matchable_s_indexes_lists_mapping[pattern_index] = []
        if '*' in current_pattern:
            continue

        pattern_matched = False
        while s_cursor < len(s):
            sub_s_start_index = s_cursor
            sub_s_end_index   = s_cursor + len(current_pattern)
            sub_s = s[sub_s_start_index:sub_s_end_index]
            if sub_s_matched_non_asterisk_pattern(sub_s, current_pattern):
                pattern_index_matchable_s_indexes_lists_mapping[pattern_index].append(list(range(sub_s_start_index, sub_s_end_index)))
                pattern_matched = True

                sub_s_start_index += 1
                sub_s_end_index   += 1
                while s_cursor < len(s):
                    if sub_s_matched_non_asterisk_pattern(s[sub_s_start_index:sub_s_end_index], current_pattern):
                        pattern_index_matchable_s_indexes_lists_mapping[pattern_index].append(list(range(sub_s_start_index, sub_s_end_index)))
                    sub_s_start_index += 1
                    sub_s_end_index   += 1
                    s_cursor += 1

                s_cursor = pattern_index_matchable_s_indexes_lists_mapping[pattern_index][0][-1] + 1
                break
            else:
                s_cursor += 1
        if s_cursor >= len(s) and not pattern_matched:
            return None

    # get possible matched indexes of asterisk sign patterns
    for pattern_index in pattern_index_matchable_s_indexes_lists_mapping:
        if len(pattern_index_matchable_s_indexes_lists_mapping[pattern_index]) == 0:
            start_index = 0
            end_index = len(s)

            for pattern_index_2 in pattern_index_matchable_s_indexes_lists_mapping:
                if '*' in patterns[pattern_index_2]:
                    continue
                if pattern_index_2 < pattern_index:
                    start_index = pattern_index_matchable_s_indexes_lists_mapping[pattern_index_2][0][-1] + 1
                elif pattern_index_2 > pattern_index:
                    end_index = pattern_index_matchable_s_indexes_lists_mapping[pattern_index_2][-1][0]
                    break

            pattern_index_matchable_s_indexes_lists_mapping[pattern_index] = sub_s_matched_indexes_for_asterisk_sign_pattern(start_index, end_index, s[start_index:end_index], patterns[pattern_index])

    return pattern_index_matchable_s_indexes_lists_mapping

def isMatch(s, p):
    patterns = get_patterns(p)
    pattern_index_matchable_s_indexes_lists_mapping = get_pattern_index_matchable_s_indexes_lists_mapping(s, patterns)
    if pattern_index_matchable_s_indexes_lists_mapping is None:
        return False

    last_s_cursor = len(s) - 1
    s_cursor = len(s) - 1
    for pattern_index in range(len(patterns) - 1, -1, -1):
        pattern = patterns[pattern_index]
        matchable_s_indexes_lists = pattern_index_matchable_s_indexes_lists_mapping[pattern_index]

        # Find indexes_list contains current s_cursor
        target_s_indexes_list = None
        for matchable_s_indexes in matchable_s_indexes_lists[::-1]:
            if s_cursor in matchable_s_indexes:
                target_s_indexes_list = matchable_s_indexes

        if target_s_indexes_list is None:
            if '*' in pattern:
                continue
            else:
                # check if it's able to skip previous asterisk sign pattern
                if pattern_index + 1 < len(patterns):
                    prev_pattern = patterns[pattern_index + 1]
                    if '*' in prev_pattern:
                        matchable_s_indexes_lists = pattern_index_matchable_s_indexes_lists_mapping[pattern_index]
                        for matchable_s_indexes in matchable_s_indexes_lists[::-1]:
                            if last_s_cursor in matchable_s_indexes:
                                target_s_indexes_list = matchable_s_indexes

                        if target_s_indexes_list:
                            s_cursor = target_s_indexes_list[0] - 1
                            continue

                return False

        # Move s_cursor
        last_s_cursor = s_cursor
        s_cursor = target_s_indexes_list[0] - 1

    return s_cursor == -1

print(f"isMatch('', '.*.*'):                                          correct: {isMatch('', '.*.*') == True}")
print(f"isMatch('', '.*.'):                                           correct: {isMatch('', '.*.') == False}")
print(f"isMatch('aa', 'a'):                                           correct: {isMatch('aa', 'a') == False}")
print(f"isMatch('aa', 'a*'):                                          correct: {isMatch('aa', 'a*') == True}")
print(f"isMatch('ab', '.*'):                                          correct: {isMatch('ab', '.*') == True}")
print(f"isMatch('aab', 'c*a*b'):                                      correct: {isMatch('aab', 'c*a*b') == True}")
print(f"isMatch('mississippi', 'mis*is*p*.'):                         correct: {isMatch('mississippi', 'mis*is*p*.') == False}")
print(f"isMatch('mississippi', 'mis*is*ip*.'):                        correct: {isMatch('mississippi', 'mis*is*ip*.') == True}")
print(f"isMatch('aaa', 'a*a'):                                        correct: {isMatch('aaa', 'a*a') == True}")
print(f"isMatch('aaa', 'a*aa'):                                       correct: {isMatch('aaa', 'a*aa') == True}")
print(f"isMatch('aaa', 'a*aaa'):                                      correct: {isMatch('aaa', 'a*aaa') == True}")
print(f"isMatch('aaa', 'a*aaaa'):                                     correct: {isMatch('aaa', 'a*aaaa') == False}")
print(f"isMatch('aaba', 'ab*a*c*a'):                                  correct: {isMatch('aaba', 'ab*a*c*a') == False}")
print(f"isMatch('aaa', 'a.a'):                                        correct: {isMatch('aaa', 'a.a') == True}")
print(f"isMatch('aaca', 'ab*a*c*a'):                                  correct: {isMatch('aaca', 'ab*a*c*a') == True}")
print(f"isMatch('bbbba', '.*a*a'):                                    correct: {isMatch('bbbba', '.*a*a') == True}")
print(f"isMatch('ab', '.*c'):                                         correct: {isMatch('ab', '.*c') == False}")
print(f"isMatch('ab', '.*..'):                                        correct: {isMatch('ab', '.*..') == True}")
print(f"isMatch('abbbcd', 'ab*bbbcd'):                                correct: {isMatch('abbbcd', 'ab*bbbcd') == True}")
print(f"isMatch('abbbcd', 'ab*bb.cd'):                                correct: {isMatch('abbbcd', 'ab*bb.cd') == True}")
print(f"isMatch('bbab', '.*ab'):                                      correct: {isMatch('bbab', '.*ab') == True}")
print(f"isMatch('bbbc', 'b*.'):                                       correct: {isMatch('bbbc', 'b*.') == True}")
print(f"isMatch('bbbb', 'b*.'):                                       correct: {isMatch('bbbb', 'b*.') == True}")
print(f"isMatch('bbbb', 'b*.*'):                                      correct: {isMatch('bbbb', 'b*.*') == True}")
print(f"isMatch('aaa', 'ab*ac*a'):                                    correct: {isMatch('aaa', 'ab*ac*a') == True}")
print(f"isMatch('bbba', '.*b'):                                       correct: {isMatch('bbba', '.*b') == False}")
print(f"isMatch('bccbbabcaccacbcacaa', '.*b.*c*.*.*.c*a*.c'):         correct: {isMatch('bccbbabcaccacbcacaa', '.*b.*c*.*.*.c*a*.c') == False}")
print(f"isMatch('bbcacbabbcbaaccabc', 'b*a*a*.c*bb*b*.*.*'):          correct: {isMatch('bbcacbabbcbaaccabc', 'b*a*a*.c*bb*b*.*.*') == True}")
print(f"isMatch('aasdfasdfasdfasdfas', 'aasdf.*asdf.*asdf.*asdf.*s'): correct: {isMatch('aasdfasdfasdfasdfas', 'aasdf.*asdf.*asdf.*asdf.*s') == True}")
print(f"isMatch('abbabaaaaaaacaa', 'a*.*b.a.*c*b*a*c*'):              correct: {isMatch('abbabaaaaaaacaa', 'a*.*b.a.*c*b*a*c*') == True}")
print(f"isMatch('cbaacacaaccbaabcb', 'c*b*b*.*ac*.*bc*a*'):           correct: {isMatch('cbaacacaaccbaabcb', 'c*b*b*.*ac*.*bc*a*') == True}")
print(f"isMatch('aabccbcbacabaab', '.*c*a*b.*a*ba*bb*'):              correct: {isMatch('aabccbcbacabaab', '.*c*a*b.*a*ba*bb*') == True}")
print(f"isMatch('bab', '..*'):                                        correct: {isMatch('bab', '..*') == True}")
print(f"isMatch('aacbb', 'a*.bb*'):                                   correct: {isMatch('aacbb', 'a*.bb*') == True}")
