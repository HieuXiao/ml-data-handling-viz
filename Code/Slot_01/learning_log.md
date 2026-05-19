### [LOG 01] - How to use pd.cut()?
- Aim : Chuyển đổi dữ liệu số liên tục (continuous) thành dữ liệu phân loại hoặc các khoảng (categorical/bins).
- Syntax : pd.cut(x, bins, labels=None, right=True)
    - x: Mảng 1 chiều (Pandas Series, list) cần phân chia.
    - bins: Số lượng nhóm (số nguyên) hoặc mảng các mốc chia (ví dụ: [0, 18, 60, 100]).
    - labels: Danh sách tên đại diện cho từng nhóm tương ứng.
    - right: True (mặc định) là khoảng đóng bên phải (a, b]. False là khoảng đóng bên trái [a, b).
- Ứng dụng thực tiễn:
    - Phân khúc người dùng (VD: thu nhập thấp, trung bình, cao).
    - Phân loại nhóm tuổi (VD: trẻ em, người lớn, người già) cho các mô hình Machine Learning.
    - Xếp loại điểm học tập (A, B, C, D).
### [LOG 02] - How to use .unstack()?
- Aim : Xoay (pivot) một cấp độ của chỉ mục (Index) thành các cột (Columns). Đóng vai trò chuyển đổi dữ liệu từ dạng dài (long format) sang dạng rộng (wide format).
- Syntax: DataFrame.unstack(level=-1, fill_value=None)
    - level: Cấp độ của MultiIndex cần xoay (mặc định -1 đại diện cho cấp độ trong cùng/cuối cùng).
    - fill_value: Giá trị thay thế cho các ô bị thiếu (NaN) sinh ra sau khi unstack.
 - Ứng dụng thực tiễn:
    - Định dạng lại dữ liệu sau khi sử dụng .groupby() với nhiều trường (MultiIndex).
    - Chuẩn bị ma trận hai chiều (2D matrix) để vẽ biểu đồ Heatmap.
    - Trình bày bảng chéo (cross-tabulation) để báo cáo số liệu dễ đọc hơn.