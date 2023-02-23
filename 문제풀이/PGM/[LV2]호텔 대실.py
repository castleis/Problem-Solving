book_time1 = [["09:10", "10:10"], ["10:20", "12:20"]]
book_time2 = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:55"], ["18:20", "21:20"]]
book_time3 = [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]

def solution(book_time):
    times = []
    for time in book_time:
        S_h, S_m = time[0].split(':')
        E_h, E_m = time[1].split(':')
        times.append([int(S_h+S_m), int(E_h+E_m)])
    times.sort()
    answer = 0

    V = [0] * len(times)
    for i in range(len(times)):
        if not V[i]:
            print(f'========= {times[i]} =========')
            start, end = times[i]
            answer += 1
            print(end%100, end//100)
            for j in range(i+1, len(times)):
                if V[j]:
                    continue
                print(f'- {times[j]} -')
                s,e = times[j]
                new_end = end + 10
                if new_end % 100 > 60:    # 퇴실 후 청소 시간을 합친 것이 60분을 넘어가면 hour로 넘기기
                    new_end = int(str(new_end // 10 + 1) + '0' + str(new_end % 100 - 60))
                if s >= new_end:
                    V[j] = 1
                    end = e
    return answer

print('정답~~~',solution(book_time1))
print('정답~~~',solution(book_time2))
print('정답~~~',solution(book_time3))
