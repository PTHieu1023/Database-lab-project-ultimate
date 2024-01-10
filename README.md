# Demo chương trình quản lý siêu thị mini (Mini Supermarket Managerment system)
# Mô tả ứng dụng
## I. Tổng quan chương trình
- Quản lý chung (General)
- Quản lý đơn hàng (Order)
- Quản lý hàng hoá (Product)
- Quản lý khách hàng (Customer)
- Quản lý nhân viên (Staff)
## III. Đối tượng người dùng
**Mặc định user của phần mềm sẽ là quản lý siêu thị nên sẽ có toàn quyền thêm sửa xoá dữ liệu**
## II. Chi tiết
1. Quản lý chung general (General)
    - Ở giao diện general người dùng có thể sử dụng truy vấn SQL để tra các thông tin có trong cơ sở dữ liệu (Chức năng này để kiểm tra là chính và sẽ có cập nhật lại thành quản lý chi tiêu cho tương lai)
2. Quản lý đơn hàng (Order)
    - Ở giao diện đơn hàng người dùng có thể xem toàn bộ đơn hàng và tìm kiếm đơn hàng theo tên người mua, người bán hoặc tên sản phẩm
    - Người dùng có thể thêm đơn hàng, xoá đơn hàng
    - Khi thêm đơn hàng sẽ có cửa số popup hiện ra để người dùng điền thông tin đơn hàng. Đối với trường thông tin là customer và saler, thì người dùng tra cứu id trong Customer và Staff để điền vào form, để thêm vật phẩm thì nhấn nút thêm hàng hoá và điền số lượng.
    - Đối với đơn hàng đã được tạo thì không thể chỉnh sửa từ giao diện người dùng (Cần can thiệp từ Database)
3. Quản lý hàng hoá (Product)
    - Người dùng có thể theo dõi danh sách hàng hoá trong kho. 
    - Người dùng có thể thêm loại hàng mới cũng như cập nhật số lượng trong kho bằng cách tạo thêm đơn nhập hàng mới
    - Người dùng không thể xoá mặt hàng đang có trong kho
4. Quản lý người dùng (Customer)
    - CRUD thông tin người dùng
5. Quản lý nhân viên (Staff)
    - CRUD thông tin nhân viên