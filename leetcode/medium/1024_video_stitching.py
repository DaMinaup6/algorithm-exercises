# -----------------------------------------
# My Solution: Greedy
#
# Time  Complexity: O(n^2 + nlog(n))
# Space Complexity: O(n)
# -----------------------------------------
# n := len(clips)
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        if time == 0:
            return 0

        clips.sort()
        if clips[0][0] > 0 or clips[-1][1] < time:
            return -1
        if clips[0][1] >= time:
            return 1

        output_clips = [clips[0]]
        for index in range(1, len(clips)):
            clip = clips[index]
            if clip[1] > output_clips[-1][1]:
                insert_index = -1
                for output_index in range(len(output_clips)):
                    if output_clips[output_index][0] == clip[0]:
                        insert_index = output_index
                        break
                    elif output_clips[output_index][0] < clip[0] <= output_clips[output_index][1]:
                        insert_index = output_index + 1
                        break
                if insert_index != -1:
                    output_clips = output_clips[:insert_index] + [clip]
                    if output_clips[-1][1] >= time:
                        break

        return len(output_clips) if output_clips[-1][1] >= time else -1
