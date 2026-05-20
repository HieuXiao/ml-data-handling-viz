## SLOT 01 - Intro to Machine Learning 
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

## SLOT 02 - Data Handling & Visualization
### [LOG 01] - How to use mode()?
- Aim : Tìm giá trị xuất hiện nhiều nhất (most frequent value) trong dữ liệu.
- Syntax : `Series.mode(dropna=True)`
    - `dropna`: 
        - `True` (mặc định) → bỏ qua giá trị NaN.
        - `False` → tính cả NaN như một giá trị.
- Thường dùng cùng:
    - `fillna()` → điền dữ liệu khuyết bằng giá trị xuất hiện nhiều nhất.
- Ví dụ:
```python
df["gender"] = df["gender"].fillna(df["gender"].mode()[0])
```
- Giải thích:
    - `mode()` trả về Series chứa các giá trị xuất hiện nhiều nhất.
    - `[0]` dùng để lấy mode đầu tiên.
- Ứng dụng thực tiễn:
    - Điền missing value cho biến phân loại (categorical variable).
    - Xác định nhóm phổ biến nhất trong dữ liệu.
    - Tiền xử lý dữ liệu cho Machine Learning và Statistical Analysis.
### [LOG 02] - How to use interpolate()?
- Aim : Nội suy (interpolation) các giá trị khuyết dựa trên xu hướng hoặc mối quan hệ của dữ liệu xung quanh.
- Syntax : `Series.interpolate(method='linear', axis=0, limit_direction='forward')`

  - `method`:

    - `'linear'` (mặc định) → nội suy tuyến tính.
    - `'polynomial'` → nội suy đa thức.
    - `'time'` → nội suy theo thời gian.
    - `'nearest'` → lấy giá trị gần nhất.
  - `axis`:

    - `0` → nội suy theo cột.
    - `1` → nội suy theo hàng.
  - `limit_direction`:

    - `'forward'` → nội suy xuôi.
    - `'backward'` → nội suy ngược.
    - `'both'` → cả hai chiều.
- Ví dụ:

```python id="92ghmv"
df["temperature"] = df["temperature"].interpolate(method="linear")
```

- Giải thích:

  - `interpolate()` ước lượng giá trị NaN dựa trên các điểm dữ liệu lân cận.
  - `linear` giả định dữ liệu thay đổi tuyến tính giữa hai điểm.
- Ứng dụng thực tiễn:

  - Xử lý missing value trong dữ liệu time-series.
  - Nội suy dữ liệu cảm biến, tài chính, y sinh.
  - Làm mượt dữ liệu liên tục trước khi huấn luyện mô hình Machine Learning.
- Lưu ý:

  - Không nên áp dụng cho biến mục tiêu (target variable).
  - Hiệu quả hơn khi dữ liệu có tính liên tục hoặc tuần tự theo thời gian.
