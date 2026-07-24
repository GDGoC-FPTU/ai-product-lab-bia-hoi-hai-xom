Phase 1 — SCAN 

| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | Xanh SM | Lặp lại | Điều phối viên phải đọc, tóm tắt và phân loại thủ công các báo cáo sự cố không có cấu trúc từ tài xế. |
| 2 | Xanh SM | Tốn thời gian | Điều phối viên phải kiểm tra mức pin, vị trí xe, khoảng cách và tình trạng trạm để hướng dẫn tài xế sạc xe. |
| 3 | Xanh SM | AI-upgrade | Việc phân bổ xe giữa các khu vực chủ yếu dựa trên kinh nghiệm và dữ liệu lịch sử, chưa dự báo chính xác nhu cầu theo thời gian thực. |
| 4 | Xanh SM | Stakeholder Pain | Nhân viên depot phải kiểm tra thủ công ngoại thất xe và so sánh ảnh cũ để phát hiện vết xước hoặc hư hỏng mới. |
| 5 | Xanh SM | Tốn thời gian | Nhân viên đối soát phải kiểm tra thủ công các trường hợp sai lệch về giá chuyến đi, khuyến mại, thanh toán và thu nhập tài xế. |

Phase 2 — QUICK-ASSESS

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: Điều phối viên Xanh SM phải đọc, tóm tắt và phân  │
│ loại thủ công các báo cáo sự cố không có cấu trúc từ tài xế.│
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau? Tài xế (chờ hỗ trợ), Điều phối viên (quá tải)  │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Tài xế gọi tổng đài hoặc gửi tin nhắn báo sự cố        │
│   → 2. Điều phối viên đọc/nghe toàn bộ nội dung             │
│   → 3. Xác định loại và mức độ nghiêm trọng của sự cố       │
│   → 4. Nhập lại thông tin vào hệ thống vận hành             │
│   → 5. Chuyển sự cố đến bộ phận phụ trách                   │
│                                                             │
│ Bước nào tốn nhất? Bước 2-4 (⏱ 8-12 phút/lượt)              │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-4              │
│ (Speech-to-text -> Tóm tắt -> Phân loại -> Draft hướng dẫn) │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ Giảm thời gian xử lý từ 8-12 phút ──> dưới 3 phút.          │
│ Độ chính xác phân loại đạt ít nhất 90%.                     │
│                                                             │
│ Quick Architecture: [x] LLM Feature + Rule-based Routing    │
│ (AI tạo bản nháp, điều phối viên kiểm tra trước khi gửi)     │
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán: Tài xế Xanh SM báo cáo sự cố sạc pin / hết pin    │
│ giữa đường cần điều phối cứu hộ hoặc trạm sạc gần nhất.     │
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau? Tài xế (chờ đợi), Điều phối viên (quá tải)     │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Tài xế gọi tổng đài điều vận báo xe sắp hoặc đã hết pin│
│   → 2. Điều phối viên tra cứu vị trí xe trên bản đồ         │
│   → 3. Tra cứu các trạm sạc còn trụ trống và tương thích    │
│   → 4. Soạn tin nhắn chỉ dẫn và gửi qua ứng dụng tài xế     │
│   → 5. Liên hệ đội cứu hộ nếu xe đã cạn hoàn toàn pin       │
│                                                             │
│ Bước nào tốn nhất? Bước 3-4 (⏱ khoảng 12 phút/lượt)         │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3-4              │
│ (Lấy vị trí -> Tra cứu trạm phù hợp -> Draft tin chỉ dẫn)   │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ Giảm thời gian xử lý sự cố từ 15 phút ──> dưới 3 phút.      │
│ Giảm ít nhất 50% số trường hợp xe hết pin ngoài trạm.       │
│                                                             │
│ Quick Architecture: [x] LLM Feature + Safety Rules          │
│ (AI tự động soạn chỉ dẫn, con người phê duyệt trước khi gửi)│
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán: Điều phối viên phân bổ tài xế và phương tiện giữa │
│ các khu vực chủ yếu dựa trên kinh nghiệm, dẫn đến nơi thừa  │
│ xe và nơi thiếu xe trong giờ cao điểm.                      │
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau? Khách hàng (chờ lâu), Tài xế (chạy rỗng),      │
│ Điều phối viên (khó dự báo nhu cầu)                         │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Điều phối viên xem số lượng xe tại từng khu vực        │
│   → 2. Kiểm tra dữ liệu đặt xe và chuyến đi gần đây         │
│   → 3. Ước tính khu vực có khả năng tăng nhu cầu            │
│   → 4. Gọi hoặc nhắn tài xế di chuyển sang khu vực khác     │
│   → 5. Theo dõi kết quả và điều chỉnh lại thủ công          │
│                                                             │
│ Bước nào tốn nhất? Bước 2-4 (⏱ 15-30 phút/lần điều phối)    │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-4              │
│ (Dự báo nhu cầu -> Đề xuất khu vực -> Gợi ý xe điều chuyển) │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ Giảm ít nhất 20% tỷ lệ hủy chuyến do thiếu tài xế.          │
│ Giảm 15% quãng đường xe chạy rỗng.                          │
│ Giảm thời gian đón khách trung bình ít nhất 10%.            │
│                                                             │
│ Quick Architecture: [x] Machine Learning + Optimization     │
│ (Dự báo nhu cầu và đề xuất tái phân bổ xe theo khu vực)     │
└─────────────────────────────────────────────────────────────┘