## Quyết định xử lý: Xóa dữ liệu trùng lặp (Duplicates)
 
**Quan sát**: 38 hàng trùng lặp hoàn toàn trong tập dữ liệu.
 
**Giả thuyết về nguyên nhân**:
  - Do lỗi hệ thống ghi nhận nhiều lần một lượt nộp form, hoặc người dùng submit form bị đúp.
  - Các dòng này trùng khớp 100% không cung cấp thêm thông tin mới.
 
**Phương án đã xem xét**:
  1. Giữ nguyên → có thể làm sai lệch phân phối và các thống kê (mean, median).
  2. Drop duplicates → loại bỏ nhiễu, làm sạch dữ liệu.
 
**Quyết định**: Phương án 2 (Drop duplicates)
**Lý do**: Các dòng lặp lại hoàn toàn không mang ý nghĩa phân tích, việc xóa bỏ giúp kết quả phân tích thống kê chính xác hơn và không tốn kém tài nguyên tính toán.


## Quyết định xử lý: Cột 'annual_salary' — sai kiểu dữ liệu (dtype) và missing ~14%
 
**Quan sát**: Cột 'annual_salary' đang là kiểu chuỗi (object) do chứa dấu phẩy ','. Có khoảng 14% bị thiếu (null).
 
**Giả thuyết về nguyên nhân**:
  - Người dùng nhập số tiền có dấu phẩy phân cách hàng nghìn.
  - Khả năng MNAR cao: người có lương thấp ngần ngại khai báo mức lương.
 
**Phương án đã xem xét**:
  1. Drop các dòng thiếu → mất 14% lượng dữ liệu, có thể gây bias mẫu.
  2. Làm sạch định dạng, ép sang numeric, fillna(global_median) → đơn giản nhưng bỏ qua context.
  3. Làm sạch định dạng, ép sang numeric, fillna(median theo industry) → tốt hơn, dùng được ngữ cảnh.
 
**Quyết định**: Phương án 3 + thêm cột flag 'salary_imputed'.
**Lý do**: Lương là biến phân tích chính, cần phải chuyển sang số thực để tính toán. Dùng median theo ngành nghề thực tế hơn nhiều so với global median. Flag giúp người dùng sau biết đây là dữ liệu đã được điền và có thể filter nếu cần.


## Quyết định xử lý: Các cột có tỷ lệ missing cao ('income_context', 'us_state', 'city', 'additional_monetary_comp') — missing > 50%
 
**Quan sát**: Các cột này có tỷ lệ missing value rất lớn, từ 55% đến 81%.
 
**Giả thuyết về nguyên nhân**:
  - Các trường này là tùy chọn (optional) trong biểu mẫu khảo sát.
  - Nhiều người không có thu nhập phụ hoặc cảm thấy không cần thiết điền.
 
**Phương án đã xem xét**:
  1. Drop hẳn các cột này → mất đi thông tin quý giá của khoảng 20-45% người đã cung cấp dữ liệu.
  2. Điền giá trị mặc định như 'Unknown' (đối với categorical/text) hoặc 0 (đối với tiền tệ) cho các giá trị null.
 
**Quyết định**: Phương án 2. Cụ thể điền 'Unknown' cho các cột categorical, điền 0 hoặc parse cẩn thận cho tiền tệ.
**Lý do**: Các thông tin này dù thiếu nhưng vẫn hữu ích cho việc khoan sâu (drill-down). Việc điền giá trị mặc định giúp giữ lại cột mà không làm code báo lỗi khi thống kê.
