# Assignment 01: Data Acquisition, Understanding, and Preparation

## Tổng quan Dự án (Project Overview)
Dự án này tập trung vào việc tiền xử lý và làm sạch một tập dữ liệu về hoạt động giao hàng (Delivery / Service Operations). Mục tiêu là chuẩn bị dữ liệu chất lượng cao để phục vụ cho các bước phân tích hoặc huấn luyện mô hình học máy tiếp theo.

## Mô tả Tập dữ liệu (Dataset Description)
Tập dữ liệu ban đầu chứa các thông tin về chuyến đi, lộ trình vận chuyển, thời gian ước tính (OSRM), thời gian thực tế và khoảng cách.

## Tóm tắt quá trình Làm sạch (Cleaning Summary)
- Xóa các bản ghi trùng lặp hoàn toàn.
- Thay thế các giá trị văn bản bị thiếu bằng chuỗi "Unknown".
- Xử lý các giá trị không hợp lệ (ví dụ: khoảng cách âm, thời gian âm).
- Ép kiểu dữ liệu thời gian về định dạng datetime chuẩn.

## Các Trường Phái sinh (Derived Fields)
1. `trip_duration_hrs`: Thời gian chuyến đi tính bằng giờ.
2. `speed_kmph`: Tốc độ trung bình (km/h).
3. `is_delayed`: Trạng thái trễ so với dự kiến.
4. `route_efficiency`: Tỷ lệ hiệu quả định tuyến.

## Cấu trúc Thư mục (Folder Structure)
```
DH_Assign_01/
├── data_raw/
│   └── original_dataset.csv
├── data_cleaned/
│   └── cleaned_dataset.csv
├── docs/
│   ├── Data_Dictionary.xlsx
│   ├── Issue_Log.xlsx
│   ├── Transformation_Log.xlsx
│   ├── README.md
│   └── Reflection.docx
└── assignment01.ipynb
```

## Hướng dẫn tái lập (Reproducibility Instructions)
1. Mở file `assignment01.ipynb` bằng Jupyter Notebook hoặc IDE có hỗ trợ.
2. Chạy toàn bộ các ô code (Run All) theo thứ tự từ trên xuống dưới.
3. Dữ liệu sạch sẽ được tự động ghi vào thư mục `data_cleaned/`.
