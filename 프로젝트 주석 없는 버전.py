import random
import time

print("로또 번호 추첨 프로그램을 시작합니다")
print("-" * 30)

def get_lottery_nums(): #임의적으로 로또 번호를 생성하는 함수
    lottery = []
    
    while len(lottery) < 6:
        n = random.randint(1, 45)
        if n not in lottery:
            print("%d를 추가합니다" % n)
            lottery.append(n)
        else:
            print("%d는 중복입니다" % n)
    return lottery

def get_bonus_num(lottery): #보너스 번호를 생성하는 함수
    while True:
        num_bonus = random.randint(1, 45)
        if num_bonus not in lottery:
            return num_bonus

def get_user_nums(): #수동 선택 시 사용자에게 번호를 입력받는 함수
    num_user = []
    
    while len(num_user) < 6:
        num = int(input("1~45까지의 수 중 하나를 선택하세요: "))
        if num in num_user:
            print("중복된 숫자는 입력할 수 없습니다.")
        elif num < 1 or num > 45:
            print("숫자는 1과 45 사이여야 합니다.")
        else:
            num_user.append(num)
    return num_user

def auto_generate_user_nums(): #자동 선택 시 임의적으로 번호를 생성하는 함수
    num_user = []
    
    while len(num_user) < 6:
        n = random.randint(1, 45)
        if n not in num_user:
            time.sleep(1)
            print("%d를 추가합니다." % n)
            num_user.append(n)
        else:
            print("%d는 중복입니다." % n)
    return num_user

def purchase_lottery_tickets():
    while True:
        count = int(input("복권을 몇 개 구매하시겠습니까? "))
        if count > 100:
            print("복권의 1회 최대 구매 한도는 10만원입니다. 다시 입력해주세요.")
            print()
        elif count > 0 and count <= 100:
            print("복권을 %d개 구매하신다면 %d원입니다." % (count, count * 1000))
            break
        else:
            print("입력하신 응답을 확인해주세요. 원하는 형식의 응답이 아닙니다.")
            print()
            
    print()
    return count

def check_results(lottery, num_bonus, num_user):
    common_num = 0
    for num in num_user:
        if num in lottery:
            common_num += 1

    if common_num <= 2:
        return "아쉽게도 미당첨입니다. 다음 기회에 다시 도전하세요!!"
    elif common_num == 3:
        return "5등 당첨입니다. 당첨액은 5000원입니다."
    elif common_num == 4:
        return "4등 당첨입니다. 당첨액은 50000원입니다."
    elif common_num == 5:
        if num_bonus in num_user:
            return "2등 당첨입니다."
        else:
            return "3등 당첨입니다"
    else:
        return "1등 당첨입니다'"

while True:
        lottery = get_lottery_nums()
        num_bonus = get_bonus_num(lottery)
        
        print("선택된 복권 번호: ", lottery)
        print("보너스 번호: ", num_bonus)
        print()

        count = purchase_lottery_tickets()

        while True:
            user_choice = input("번호를 직접 입력하시겠습니까? (y/n): ")
            if user_choice == 'Y' or user_choice == 'y':
                for i in range(count):
                    print()
                    print("%d번째 복권 숫자 입력이 시작됩니다." % (i + 1))
                    num_user = get_user_nums()
                    print()
                    print("%d번째 복권에 해당하는 숫자 입력이 끝났습니다." % (i + 1))
                    print()
                    print("사용자가 입력한 복권 번호: ", num_user)
                    result = check_results(lottery, num_bonus, num_user)
                    print()
                    print(result)
                break
            
            elif user_choice == 'N' or user_choice == 'n':
                print()
                print("직접 입력하지 않겠다고 하셨으므로 컴퓨터가 임의로 번호를 생성합니다.")
                print()
                for i in range(count):
                    num_user = auto_generate_user_nums()
                    print("%d번째 복권에 해당하는 숫자 생성이 끝났습니다." % (i + 1))
                    print()
                    print("자동 생성된 사용자 복권 번호: ", num_user)
                    result = check_results(lottery, num_bonus, num_user)
                    print()
                    print(result)
                break
            else:
                print("입력하신 응답을 확인해주세요. 원하는 형식의 응답이 아닙니다.")
                print()
        
        another_round = input("다시 시도하시겠습니까? (y/n): ")
        if another_round != 'Y' or 'y':
            break

print("-" * 30)
print("로또 번호 추첨 프로그램이 종료됩니다.")
