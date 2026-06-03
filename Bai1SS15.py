# Phân tích 
# Ở đây biến global là biến inventory_stock và total_revenue còn biến cục bộ thì ở chức năng 2 chúng ta tạo 1 biến là discount là biến để lưu giảm giá 
# Đề bài này thì chúng ta cần tạo 1 menu gồm 4 chức năng 
# Để làm menu này thì chúng ta cần tạo 1 vòng while và kết thúc khi người dùng ấn 4
# Chức năng đầu tiên là chức năng nhập hàng vào kho, để làm chức năng này thì đầu tiên chúng ta cần tạo 1 hàm riêng 
# Trong hàm này thì chúng ta có tham số là số lượng yêu cầu người dùng và sau đó truyền cái này vào hàm 
# Đầu tiên trong hàm chúng ta nên gọi biến global inventory_stock, sau đó thực hiện tính toán và sau đó trả về tổng số lượng sản phẩm của kho 
# Và số lượng người dùng nhập chúng ta phải check xem sản phẩm có <= 0 không, nếu như vậy thì bắt người dùng nhập lại 
# Chức năng số 2 là chức năng bán hàng, để làm được chức năng này thì chúng ta cần tạo 1 hàm mới 
# Hàm này có 2 tham số là số lượng và đơn giá, 2 tham số này là 2 biến input yêu cầu người dùng nhập và sau đó truyền vào đối số khi chúng ta gọi hàm 
# Cần check xem số lượng và đơn giá có hợp lệ không 
# Trong hàm đầu tiên thì chúng ta cần tính số tiền tạm tính và xem có được giảm giá không, cộng thêm thuế và cuối cùng là trả về giá trị cuối cùng 
# Hàm thứ 2 trong chức năng này là hàm để kiểm tra, xem trong kho có đủ số lượng để bán không, nếu đủ thì cộng và in ra hóa đơn 
# Còn nếu không đủ thì in ra thông báo lỗi 
# Và chức năng cuối cùng là xem báo cáo, thì chức năng này chúng ta phải tạo thêm 1 hàm và hàm này phải có docstring để xem hàm này có chức năng là gì 
# Trong hàm này thì chúng ta in ra số lượng hàng trong kho hiện tại và tổng doanh thu người bán 

# Viết code 
inventory_stock = 100
total_revenue = 0.0

def add_stock(amount):
    global inventory_stock
    inventory_stock += int(amount)
    return inventory_stock

def calculate_final_price(quantity, price):
    total_price = int(quantity)*int(price)
    discount = 0.1
    tax = 0.08
    if total_price >= 1000:
        total_price = total_price - total_price*discount
    final_total =  total_price + total_price*tax
    print(f"""-> Hóa đơn chi tiết: 
Số lượng: {quantity} | Đơn giá: ${price}
Tạm tính: ${total_price}
Giảm giá (10%): ${total_price*discount}
Thuế VAT (8%): ${total_price*tax}
Tổng thanh toán: ${final_total}
Đã bán hàng thành công!""")
    return final_total

def process_sale(quantity, final_total):
    global inventory_stock
    global total_revenue
    if int(quantity) > inventory_stock:
        print(f"Lỗi: Không đủ hàng trong kho. Tồn kho hiện tại chỉ còn {inventory_stock}")
        return False 
    inventory_stock -= int(quantity)
    total_revenue += final_total
    return True

def print_report():
    """
    Hàm này để xem mô tả về trạng thái
    Hiển thị thông tin gồm hàng tồn kho và tổng doanh thu
    """
    print(f"Tồn kho hiện tại: {inventory_stock}")
    print(f"Tổng doanh thu: ${total_revenue}")
while True:
    choose = input("""========== TECHSTORE MANAGEMENT SYSTEM ==========
1. Nhập thêm hàng vào kho
2. Bán hàng (Tính toán hóa đơn)
3. Xem báo cáo tổng quan
4. Thoát chương trình
=================================================
Chọn chức năng (1-4): """)
    if choose == "1":
        print("--- NHẬP HÀNG ---")
        add_product = input("Nhập số lượng sản phẩm muốn thêm: ").strip()
        while not add_product.isdigit() or int(add_product) <= 0:
            print("Số lượng không hợp lệ")
            add_product = input("Nhập số lượng muốn thêm: ")
        print(f"Đã nhập thành công {add_product} sản phẩm")
        print(f"Tồn kho hiện tại: {add_stock(add_product)}")
        print()
    elif choose == "2":
        print("--- BÁN HÀNG ---")
        buy_quantity = input("Nhập số lượng mua: ")
        while not buy_quantity.isdigit() or int(buy_quantity) <= 0:
            print("Số lượng không hợp lệ")
            buy_quantity = input("Nhập số lượng mua: ")
        price = input("Nhập đơn giá ($): ")
        while not price.isdigit() or int(price) <= 0:
            print("Đơn giá không hợp lệ")
            price = input("Nhập đơn giá ($): ")
        process_sale(buy_quantity,calculate_final_price(buy_quantity,price))
        if process_sale(buy_quantity,calculate_final_price(buy_quantity,price)):
            calculate_final_price(buy_quantity,price)
        print()
    elif choose == "3":
        print_report()
        print()
    elif choose == "4":
        print("Chương trình kết thúc")
        break
    else:
        print("Lựa chọn không hợp lệ")