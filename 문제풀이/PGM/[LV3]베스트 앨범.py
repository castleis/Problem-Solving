from collections import defaultdict

def solution(genres, plays):
    N = len(genres)

    info = defaultdict(list)
    for i in range(N):
        info[genres[i]].append([i,  plays[i]])
    # print(info)
    answer = []
    seq = defaultdict(str)

    for genre in info:
        sum_of_plays = [sum(x) for x in zip(*info[genre])][1]
        # sum_plays2 = list(map(sum, zip(*info[genre])))
        # print(sum_plays2)
        info[genre].sort(key = lambda x : (-x[1],x[0]))
        info[genre] = info[genre][:2]
        seq[sum_of_plays] = genre
    order = list(seq.keys())
    # print(info)
    # print('seq : ',seq)
    # print('order : ',sorted(order, reverse=True))
    for g in sorted(order, reverse=True):
        play = info[seq[g]]
        if len(play) == 1:
            answer.append(play[0][0])
        else:
            answer += [play[0][0], play[1][0]]
    return answer

genres, plays = ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
print(solution(genres, plays))


def solution_1(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        print('e : ',e)
        d[e[0]].append([e[1] , e[2]])
    print('d : ', d)
    # x : genre, y : play 횟수.
    # map(lambda y:y[0], d[x]) => d[x]의 첫번째 원소, 즉 해당 곡의 플레이 횟수
    # lambda x : sum(map(lambda y:y[0], d[x])) => x 장르에 속하는 곡들의 플레이 횟수를 모두 더하기
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    print('genreSort :', genreSort)
    for g in genreSort:
        # d[g]를 플레이 횟수, -인덱스 로 reverse 정렬한 것의 두번째 원소들을 리스트로 만든 것
        # 즉, 문제에서 요구한 정렬 기준에 맞게 정렬 후, 음악의 고유번호 (e[1])들을 모아 리스트로 만들기
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        print('temp :', temp)
        # min(len(temp),2) => temp가 1개 있다면 1개만, 2개 이상이면 2개를 담아주기 위함
        answer += temp[:min(len(temp),2)]
    return answer
print(solution_1(genres, plays))