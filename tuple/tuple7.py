# 여러 값에 대해 비교 가능
# 튜플의 또다른 장점은 여러 값에 대해 비교가 가능하다는 점입니다.
# 비교의 방법은 각 튜플의 가장 왼쪽 값끼리 비교한 후 둘의 값이 다를 경우
# 에는 나머지 값들을 비교하지 않고 큰지 작은지 여부를 판단합니다.
# 만약 가장 왼쪽 값이 동일할 경우에는 그 다음 값을 비교하고, 그 값도
# 같으면 또 다음 값을 비교하는 형태로 비교가 진행됩니다.
(0, 1, 2) < (5, 1, 2)
# True 값을 가집니다.
(0, 1, 2000000) < (0, 3, 4)
# True 값을 가집니다.
('Jones', 'Sally') < ('Jones', 'Sam')
# True 값을 가집니다.
('Jones', 'Sally') > ('Adams', 'Sam')
# True 값을 가집니다.