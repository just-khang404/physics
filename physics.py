import math
#hàm def mô phỏng tính nhanh
def fast(t, h):
    g = 2 * h / (t ** 2)
    return g
def high(h):
    t = math.sprt(2 * h / 9.8)
    return t
def time(t):
    h = 1/2 * 9.8 * t**2
    return h
def dd(t):
    v = 9.8 * t
    return v
#def tính trung bình
def tb(x):
    total = 0
    if x <= 0:
        return "số lần thí nghiệm phải trên 0 lần"
    for n in range(x):
        a = float(input(f"hãy nhập h{n + 1}: "))
        b = float(input(f"hãy nhập t{n + 1}: "))
        if b <= 0:
            return "thời gian phải lớn hơn 0"
        g = 2 * a / (b ** 2)
        total += g
    return total / x
#câu hỏi
while True:
    try:
        print("hê lô chào mừng đến buổi thí nghiệm vật lí!! ")
        print("chúng ta thống nhất đơn vị các đại lượng là m và s")
        L = input("hiện tại có 2 phương án A và B, A là tính nhanh và B là tính trung bình, xin hãy chọn ")
        if L == "A":
            print("phương án A gồm nhiều loại")
            print("từ thời gian chạm đất và chiều cao của vật tính ra g: A1")
            print("từ chiều cao của vật tính ra thời gian chạm đất A2")
            print("từ thời gian chạm đất tính ra độ cao A3")
            print("từ thời gian chạm đất tính ra vận tốc A4")
            lua_chon = input("hãy nhập lựa chọn : ")
            if lua_chon == "A1":
                t1 = float(input("hãy nhập thời gian vật chạm đất: "))
                h1 = float(input("hãy nhập khoảng cách của vật so với mặt đất "))
                if t1 <= 0 or h1 <= 0:
                    print("không hợp lệ")
                    exit()
                else:
                    A1 = fast(t1, h1)
                    print(f"gia tốc trọng trường của vật là {A1}m/s\u00b2")
            elif lua_chon == "A2":
                h2 = float(input("hãy nhập khoảng cách của vật so với mặt đất "))
                if h2 <= 0:
                    print("chưa hợp lệ")
                    exit()
                else:
                    A2 = high(h2)
                    print(f"thời gian vật chạm đất là: {A2}s")
            elif lua_chon == "A3":
                t3 = float(input("thời gian mà vật chạm đất là bao nhiêu giây "))
                if t3 <= 0:
                    print("lựa chon sai")
                    exit()
                else:
                    A3 = time(t3)
                    print(f"độ cao của vật là {A3}m")
            elif lua_chon == "A4":
                t4 = float(input("hãy cho tôi biết thời gian chạm đất"))
                if t4 <= 0:
                    print("none")
                    exit()
                else:
                    A4 = dd(t4)
                    print(f"vận tốc của vật là {A4}m/s")
        elif L == "B":
            B = int(input("Hãy nhập số lần thí nghiệm lưu ý B sinh ra dành cho bài nên chỉ tính g trung bình "))
            if B <= 0:
                print("none")
                exit()
            else:
                Bx = tb(B)
                print(f"qua {B} lần thí nghiệm ta thu được giá trị trung bình của g là : {Bx}m/s\u00b2")
                
        break
    except ValueError:
        print("none")
        exit()
        
        
                           
                    
                
                
        