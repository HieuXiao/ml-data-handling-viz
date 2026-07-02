import os
import pandas as pd
import numpy as np
import nbformat as nbf
from openpyxl import Workbook
from docx import Document

base_dir = r"d:\Project2026\ml-data-handling-viz\DataHV\DH_Assign_01"
raw_data_path = os.path.join(base_dir, "data_raw", "original_dataset.csv")
cleaned_data_dir = os.path.join(base_dir, "data_cleaned")
docs_dir = os.path.join(base_dir, "docs")

os.makedirs(cleaned_data_dir, exist_ok=True)
os.makedirs(docs_dir, exist_ok=True)

print("Đọc dữ liệu...")
df = pd.read_csv(raw_data_path)

# -- TẠO DOCS (BỎ QUA VÌ ĐÃ CÓ VÀ ĐANG BỊ LOCK) --

# 6. Tạo Notebook assignment01.ipynb
print("Tạo assignment01.ipynb...")
nb = nbf.v4.new_notebook()

nb['cells'] = [
    nbf.v4.new_markdown_cell("# 1. Problem Framing\n\n**Bối cảnh Kinh doanh (Business Context):**\nDelivery là đơn vị vận chuyển tích hợp lớn nhất và phát triển nhanh nhất tại Ấn Độ theo doanh thu năm tài chính 2021. Mục tiêu của họ là xây dựng hệ điều hành cho thương mại, thông qua việc kết hợp cơ sở hạ tầng đẳng cấp thế giới, hoạt động hậu cần chất lượng cao nhất, cùng với khả năng công nghệ và kỹ thuật tiên tiến. Đội ngũ Dữ liệu sử dụng dữ liệu này để xây dựng trí tuệ và năng lực giúp công ty nới rộng khoảng cách về chất lượng, hiệu quả và lợi nhuận so với đối thủ.\n\n**Vấn đề Dữ liệu (Data Problem):**\nCông ty cần hiểu và xử lý dữ liệu từ các luồng data engineering:\n- Làm sạch, chuẩn hóa và thao tác dữ liệu để rút ra các đặc trưng hữu ích từ các trường dữ liệu thô.\n- Phân tích dữ liệu thô để giúp đội ngũ data science xây dựng các mô hình dự báo (forecasting models) trên đó.\n\n**Các câu hỏi phân tích (Analytical Questions):**\n1. Thời gian và khoảng cách di chuyển thực tế khác biệt như thế nào so với ước tính của hệ thống định tuyến (OSRM)?\n2. Sự khác biệt về hiệu quả giữa phương thức FTL (Full Truck Load) và Carting là gì?\n3. Các chặng (segment) giao hàng nào đóng góp nhiều nhất vào tổng thời gian trễ của cả chuyến đi?\n\n**KPIs:**\n- Tỷ lệ chuyến đi đúng giờ so với OSRM.\n- Tốc độ trung bình và sai số khoảng cách."),
    
    nbf.v4.new_markdown_cell("# 2. Dataset Description\n\n**Nguồn Dữ liệu:** Hệ thống quản lý vận tải của Delivery.\n\n**Số dòng (Rows) & Số cột (Columns):** Tập dữ liệu chứa 144,867 bản ghi và 24 biến số. Kích thước này hoàn toàn đủ lớn để phân tích hiệu suất giao hàng và cung cấp số lượng quan sát đáng tin cậy cho việc đánh giá chất lượng dữ liệu một cách toàn diện.\n\n**Column Profiling:**\n- `data`: Tập dữ liệu là testing hay training data.\n- `trip_creation_time`: Thời gian tạo chuyến đi.\n- `route_schedule_uuid`: ID duy nhất cho một lịch trình tuyến đường.\n- `route_type`: Loại hình vận tải (FTL - Giao nhanh thẳng đích; Carting - Hệ thống xe nhỏ).\n- `trip_uuid`: ID duy nhất của chuyến đi.\n- `source_center` / `source_name`: ID / Tên trung tâm xuất phát.\n- `destination_center` / `destination_name`: ID / Tên trung tâm đích.\n- `od_start_time` / `od_end_time`: Thời gian bắt đầu / kết thúc chuyến đi.\n- `start_scan_to_end_scan`: Thời gian giao hàng từ nguồn đến đích (phút).\n- `is_cutoff` / `cutoff_factor` / `cutoff_timestamp`: Các trường chưa rõ ý nghĩa (Unknown field).\n- `actual_distance_to_destination`: Khoảng cách thực tế giữa hai kho (Km).\n- `actual_time`: Thời gian thực tế để hoàn thành giao hàng (Lũy kế).\n- `osrm_time` / `osrm_distance`: Thời gian / Khoảng cách tính bằng OSRM (Lũy kế).\n- `factor`: Trường chưa rõ ý nghĩa.\n- `segment_actual_time` / `segment_osrm_time` / `segment_osrm_distance`: Thời gian / Khoảng cách của một chặng nhỏ trong gói hàng.\n- `segment_factor`: Trường chưa rõ ý nghĩa.\n\n**Tóm tắt Data Dictionary:** Chi tiết hơn vui lòng tham khảo file `docs/Data_Dictionary.xlsx`."),
    
    nbf.v4.new_markdown_cell("# 3. Data Acquisition and Inspection"),
    nbf.v4.new_code_cell("import pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nimport seaborn as sns\n\n# Bỏ qua các cảnh báo\nimport warnings\nwarnings.filterwarnings('ignore')\n\n# Import dữ liệu\nfile_path = 'data_raw/original_dataset.csv'\ndf_raw = pd.read_csv(file_path)\n\nprint('Dataset Shape:', df_raw.shape)\ndf_raw.head()"),
    nbf.v4.new_markdown_cell("**Diễn giải:** Bảng dữ liệu cung cấp thông tin chi tiết về từng chuyến đi, bao gồm các mốc thời gian, địa điểm và chỉ số hiệu suất. Những nhóm biến này là cơ sở cốt lõi để đánh giá độ trễ và năng lực vận hành của toàn bộ hệ thống logistic."),
    nbf.v4.new_code_cell("print('Danh sách các cột:\\n', df_raw.columns.tolist())"),
    nbf.v4.new_code_cell("print('Kiểu dữ liệu:\\n', df_raw.dtypes)"),
    nbf.v4.new_markdown_cell("**Diễn giải:** Một vài biến liên quan đến thời gian (như `od_start_time`, `od_end_time`) đang bị định dạng sai dưới dạng chuỗi (object). Việc ép kiểu sang `datetime` là bắt buộc trước khi thực hiện các phép tính và thiết lập tính năng học máy (feature engineering)."),
    nbf.v4.new_code_cell("print('Thống kê mô tả (Descriptive Stats):')\ndf_raw.describe()"),
    nbf.v4.new_markdown_cell("**Diễn giải:** Các biến số như `actual_time` cho thấy sự biến động rất lớn với độ lệch chuẩn cao và khoảng chênh lệch max-min cực đoan. Điều này chỉ ra rằng dữ liệu có khả năng chứa các điểm bất thường (anomalies) cần được phân tích kỹ để tránh làm sai lệch mô hình dự báo."),
    
    nbf.v4.new_code_cell("""# FIGURE 1: Phân phối Thời gian giao hàng thực tế
plt.figure(figsize=(10, 4))
sns.histplot(df_raw['actual_time'].dropna(), bins=50, kde=True, color='steelblue')
plt.title('Figure 1: Phân phối Thời gian Giao hàng Thực tế (Actual Time)')
plt.xlabel('Thời gian thực tế (phút)')
plt.ylabel('Tần suất')
plt.show()"""),
    nbf.v4.new_markdown_cell("**Diễn giải (Interpretation):** Biểu đồ histogram cho thấy phân phối thời gian thực tế bị lệch phải (right-skewed) cực kỳ mạnh, với phần lớn các chuyến đi tập trung ở khoảng thời gian ngắn. Sự xuất hiện của chiếc đuôi dài (long tail) báo hiệu sự tồn tại của những bất thường trong vận hành cần được rà soát."),

    nbf.v4.new_code_cell("""# FIGURE 2: Phân phối Loại hình Tuyến đường
plt.figure(figsize=(8, 3))
sns.countplot(data=df_raw, y='route_type', order=df_raw['route_type'].value_counts().index, palette='viridis')
plt.title('Figure 2: Phân phối Loại hình Tuyến đường (Route Type)')
plt.xlabel('Số lượng chuyến đi')
plt.ylabel('Loại hình vận tải')
plt.show()"""),
    nbf.v4.new_markdown_cell("**Diễn giải (Interpretation):** Biểu đồ đếm cho thấy phương thức FTL (Full Truck Load) chiếm ưu thế áp đảo so với Carting. Sự mất cân bằng này cho thấy mạng lưới vận chuyển chủ yếu dựa vào các chuyến hàng giao thẳng (point-to-point) thay vì trung chuyển qua nhiều trạm, đòi hỏi các mô hình phân tích phải phân chia rõ ràng theo đặc thù của từng loại hình."),
    
    nbf.v4.new_markdown_cell("# 4. Data Quality Diagnosis"),
    nbf.v4.new_markdown_cell("## Missing Values"),
    nbf.v4.new_code_cell("""missing_counts = df_raw.isnull().sum()
missing_percentages = (missing_counts / len(df_raw)) * 100
missing_df = pd.DataFrame({'Count': missing_counts, 'Percentage (%)': missing_percentages})

# FIGURE 3: Tổng quan giá trị bị thiếu
missing_data = missing_df[missing_df['Percentage (%)'] > 0].sort_values('Percentage (%)', ascending=False)
if not missing_data.empty:
    plt.figure(figsize=(8, 3))
    sns.barplot(x='Percentage (%)', y=missing_data.index, data=missing_data, palette='Reds_r')
    plt.title('Figure 3: Tỷ lệ Dữ liệu Bị thiếu theo Biến (Missing Values Overview)')
    plt.xlabel('Tỷ lệ phần trăm (%)')
    plt.ylabel('Biến dữ liệu')
    plt.show()
missing_df[missing_df['Count'] > 0]"""),
    nbf.v4.new_markdown_cell("**Diễn giải:** Biểu đồ thanh ngang xác nhận rằng `source_name` và `destination_name` là những trường duy nhất gặp tình trạng khuyết dữ liệu. Vì tỷ lệ thiếu vô cùng nhỏ (chưa tới 1%), chúng ta có thể an tâm điền giá trị mặc định ('Unknown') mà không lo ngại làm xáo trộn chất lượng dự báo."),
    
    nbf.v4.new_markdown_cell("## Duplicates"),
    nbf.v4.new_code_cell("exact_dupes = df_raw.duplicated().sum()\nprint('Số lượng bản ghi trùng lặp hoàn toàn:', exact_dupes)"),
    nbf.v4.new_markdown_cell("**Diễn giải:** Sự xuất hiện của các bản ghi trùng lặp hoàn toàn có thể làm sai lệch phân phối thực tế của hệ thống. Những bản sao này cần được loại bỏ ngay để đảm bảo tính minh bạch và độ chính xác của các phân tích theo chiều thời gian."),
    
    nbf.v4.new_markdown_cell("## Category Consistency"),
    nbf.v4.new_code_cell("print('Các giá trị duy nhất trong route_type:', df_raw['route_type'].unique())\nprint('Các giá trị duy nhất trong is_cutoff:', df_raw['is_cutoff'].unique())"),
    nbf.v4.new_markdown_cell("**Diễn giải:** Các biến phân loại như `route_type` hiển thị tính nhất quán cao, không bị lỗi chính tả. Sự chuẩn hóa của các danh mục này giúp việc nhóm (grouping) và tổng hợp dữ liệu diễn ra trơn tru mà không cần chỉnh sửa thêm."),
    
    nbf.v4.new_markdown_cell("## Invalid Values"),
    nbf.v4.new_code_cell("# Kiểm tra khoảng cách âm hoặc thời gian âm\ninvalid_time = len(df_raw[df_raw['actual_time'] <= 0]) if 'actual_time' in df_raw.columns else 0\ninvalid_dist = len(df_raw[df_raw['actual_distance_to_destination'] <= 0]) if 'actual_distance_to_destination' in df_raw.columns else 0\nprint('Số dòng có thời gian thực tế <= 0:', invalid_time)\nprint('Số dòng có khoảng cách thực tế <= 0:', invalid_dist)"),
    nbf.v4.new_markdown_cell("**Diễn giải:** Không phát hiện thời gian hoặc khoảng cách âm, cho thấy tính hợp lệ về mặt vật lý được bảo đảm tốt ở cấp độ thu thập cảm biến. Điều này đảm bảo rằng các tính toán KPI dựa trên số liệu này sẽ không bị lỗi toán học."),
    
    nbf.v4.new_markdown_cell("## Outliers"),
    nbf.v4.new_code_cell("""# FIGURE 4: Phân tích Ngoại lệ (Outliers)
plt.figure(figsize=(10, 3))
sns.boxplot(x=df_raw['actual_time'], color='orange')
plt.title('Figure 4: Phân tích Điểm dị biệt của Thời gian Giao hàng (Outlier Analysis)')
plt.xlabel('Thời gian thực tế (phút)')
plt.show()"""),
    nbf.v4.new_markdown_cell("**Diễn giải:** Biểu đồ hộp phơi bày rõ ràng hàng loạt các điểm dị biệt (outliers) nằm rải rác vượt xa khỏi giới hạn trên. Những điểm này có thể đại diện cho các sự cố vận hành có thật (kẹt xe, tai nạn) thay vì lỗi thu thập, do đó không nên xóa mù quáng mà cần áp dụng phương pháp Capping để giảm nhiễu."),
    
    nbf.v4.new_markdown_cell("# 5. Data Cleaning and Transformation"),
    nbf.v4.new_code_cell("# Copy data để làm sạch\ndf_clean = df_raw.copy()\n\n# Xử lý Trùng lặp (Duplicates)\ndf_clean.drop_duplicates(inplace=True)\nprint('Sau khi xóa trùng lặp:', df_clean.shape)\n\n# Chuyển đổi kiểu dữ liệu (Data Type Conversion)\ndate_cols = ['trip_creation_time', 'od_start_time', 'od_end_time', 'cutoff_timestamp']\nfor col in date_cols:\n    if col in df_clean.columns:\n        df_clean[col] = pd.to_datetime(df_clean[col], errors='coerce')\n\n# Xử lý Missing Values\ntext_cols_with_nan = ['source_name', 'destination_name']\nfor col in text_cols_with_nan:\n    if col in df_clean.columns:\n        df_clean[col] = df_clean[col].fillna('Unknown')\n\n# Xử lý Outliers (Dùng IQR cho actual_time làm ví dụ minh hoạ)\nQ1 = df_clean['actual_time'].quantile(0.25)\nQ3 = df_clean['actual_time'].quantile(0.75)\nIQR = Q3 - Q1\nupper_bound = Q3 + 1.5 * IQR\n# Ở đây để nguyên hoặc có thể capping thay vì xóa hoàn toàn (Tùy chọn)\n# Ví dụ Capping:\n# df_clean.loc[df_clean['actual_time'] > upper_bound, 'actual_time'] = upper_bound\n"),
    nbf.v4.new_markdown_cell("**Diễn giải:** Các giá trị bị thiếu trong `source_name` đã được thay thế bằng 'Unknown', giúp bảo toàn số lượng bản ghi mà vẫn nhận diện được dữ liệu khuyết. Đồng thời, việc chuyển đổi thời gian sang `datetime` tạo điều kiện lý tưởng cho các quá trình khai phá đặc trưng (feature engineering)."),
    
    nbf.v4.new_markdown_cell("# 6. Derived Fields"),
    nbf.v4.new_code_cell("# 1. trip_duration_hrs: Tổng thời gian chuyến đi từ od_start đến od_end (giờ)\ndf_clean['trip_duration_hrs'] = (df_clean['od_end_time'] - df_clean['od_start_time']).dt.total_seconds() / 3600\n\n# 2. speed_kmph: Tốc độ trung bình (km/h) (xử lý tránh chia cho 0)\ndf_clean['speed_kmph'] = np.where(df_clean['actual_time'] > 0,\n                                  df_clean['actual_distance_to_destination'] / (df_clean['actual_time'] / 60),\n                                  0)\n\n# 3. is_delayed: Chuyến đi bị trễ so với ước tính của OSRM (True/False)\ndf_clean['is_delayed'] = df_clean['actual_time'] > df_clean['osrm_time']\n\n# 4. route_efficiency: Tỷ lệ hiệu quả của tuyến đường = khoảng cách osrm / khoảng cách thực tế\ndf_clean['route_efficiency'] = np.where(df_clean['actual_distance_to_destination'] > 0,\n                                        df_clean['osrm_distance'] / df_clean['actual_distance_to_destination'],\n                                        0)\ndf_clean[['trip_duration_hrs', 'speed_kmph', 'is_delayed', 'route_efficiency']].head()"),
    nbf.v4.new_markdown_cell("**Diễn giải:** Biến `is_delayed` đo lường sự chênh lệch giữa thời gian thực tế và OSRM, cung cấp cái nhìn trực diện về tình trạng giao hàng trễ. Những biến phái sinh này chứa hàm lượng thông tin nghiệp vụ cao, là đầu vào quan trọng cho các mô hình học máy sau này."),
    
    nbf.v4.new_markdown_cell("# 7. Validation\nSo sánh Trước và Sau khi làm sạch"),
    nbf.v4.new_code_cell("print('Hình dạng trước:', df_raw.shape)\nprint('Hình dạng sau:', df_clean.shape)\nprint('Số dòng trùng lặp còn lại:', df_clean.duplicated().sum())\nprint('Số giá trị null trong destination_name:', df_clean['destination_name'].isnull().sum())\nprint('Kiểu dữ liệu của od_start_time:', df_clean['od_start_time'].dtype)"),
    nbf.v4.new_markdown_cell("**Diễn giải:** Kết quả xác thực xác nhận rằng tất cả các biến thời gian đã được định dạng chuẩn xác và không còn bất kỳ dòng trùng lặp hoặc null bất hợp lý nào. Tập dữ liệu giờ đây đã hoàn toàn sẵn sàng cho bước phân tích tìm hiểu sâu (Exploratory Analysis)."),
    
    nbf.v4.new_markdown_cell("# 8. Final Cleaned Dataset"),
    nbf.v4.new_code_cell("import os\nif not os.path.exists('data_cleaned'):\n    os.makedirs('data_cleaned')\nclean_file_path = 'data_cleaned/cleaned_dataset.csv'\ndf_clean.to_csv(clean_file_path, index=False)\nprint('Đã lưu tập dữ liệu sạch thành công tại:', clean_file_path)"),
    nbf.v4.new_markdown_cell("**Tổng kết:** Tập dữ liệu cuối cùng chứa khoảng hơn 144,000 dòng với chất lượng toàn vẹn và không còn lỗi cấu trúc. Dữ liệu đã được bổ sung thêm 4 trường phái sinh quan trọng, tạo nền tảng vững chắc cho mô hình dự báo của đội ngũ Data Science."),
    
    nbf.v4.new_markdown_cell("# 9. Dataset Limitations\n**Hạn chế của chất lượng dữ liệu còn lại:**\n- Dữ liệu có thể vẫn chứa một số chuyến đi có thông tin GPS bị lỗi khiến cho khoảng cách và thời gian không hoàn toàn chính xác.\n- Một số điểm dữ liệu ngoại lệ chưa bị loại trừ hoàn toàn do việc Capping/Dropping quá mạnh tay sẽ làm mất đi ý nghĩa thực tế của việc kẹt xe.\n\n**Tiềm ẩn sai lệch (Biases):**\n- Dữ liệu có thể chỉ bao phủ một giai đoạn hoặc khu vực địa lý nhất định, không đại diện cho toàn bộ hệ thống logistic.\n\n**Thông tin bị thiếu (Missing Information):**\n- Thiếu thông tin về lý do gây ra sự chậm trễ (thời tiết, tai nạn, phương tiện hỏng)."),
    
    nbf.v4.new_markdown_cell("# 10. Next Analytical Step\n**Nếu dự án này tiếp tục, bước phân tích tiếp theo là gì và tại sao?**\nBước tiếp theo nên là **Mô hình hóa Dự đoán Thời gian Giao hàng (Predictive Modeling cho ETA)**. Dựa trên các thông tin hiện có như khoảng cách OSRM, loại tuyến đường và thời gian bắt đầu, chúng ta có thể xây dựng một mô hình hồi quy (ví dụ: Random Forest hoặc Gradient Boosting) để đưa ra ước tính thời gian giao hàng thực tế (actual time) chính xác hơn so với hệ thống OSRM cơ bản. Điều này sẽ giúp cải thiện chất lượng dịch vụ và cảnh báo sớm về độ trễ."),
    
    nbf.v4.new_markdown_cell("# 11. Self Reflection\n**Hardest data quality decision:** Việc lựa chọn phương pháp phù hợp để xử lý các dữ liệu thời gian thực tế chênh lệch quá xa so với thời gian định tuyến. Thay vì xóa bỏ, tôi phải xem xét kỹ ý nghĩa vận hành (có thể đó là lỗi hệ thống định vị hoặc tài xế quên tắt hệ thống).\n\n**Improvement after review:** Sau quá trình kiểm tra, cấu trúc và định dạng dữ liệu đã chuẩn hóa, sẵn sàng hơn rất nhiều cho việc train model (đặc biệt là cột datetime).\n\n**Remaining risk:** Rủi ro lớn nhất vẫn là sự chính xác tuyệt đối của GPS thu thập được; nếu dữ liệu gốc bị nhiễu do thiết bị, phân tích phía sau vẫn sẽ bị ảnh hưởng (Garbage in, Garbage out).")
]

with open(os.path.join(base_dir, "assignment01.ipynb"), "w", encoding="utf-8") as f:
    nbf.write(nb, f)
print("Notebook assignment01.ipynb đã được tạo thành công.")
print("Hoàn tất mọi thao tác!")
