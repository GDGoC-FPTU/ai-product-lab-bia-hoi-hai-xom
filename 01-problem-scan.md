### 📝 List bài toán của tôi:
| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|---|---|---|
| 1 | Vinhomes | Lặp lại | Nhân viên phải đọc, phân loại và chuyển phản ánh của cư dân đến đúng bộ phận. Với giả định 100 yêu cầu/ngày và 5 phút/yêu cầu, quy trình tiêu tốn khoảng 8,3 giờ công/ngày. |
| 2 | Vinhomes | Tốn thời gian | Nhân viên phải tra cứu thủ công khi dữ liệu chủ sở hữu và tài khoản cư dân không đồng bộ. Ước tính 100 trường hợp cần khoảng 25 giờ công nếu mỗi trường hợp mất 15 phút. |
| 3 | Vinhomes | Pain từ người khác | Cư dân phản ánh đăng ký nhận diện khuôn mặt thất bại nhiều lần và khó liên hệ hotline. Hỗ trợ 100 trường hợp, mỗi trường hợp 10 phút, cần khoảng 16,7 giờ công. |
| 4 | Vinhomes | Pain từ người khác | Lỗi thanh toán phí quản lý khiến cư dân có nguy cơ bị tính phí chậm và phải khiếu nại. Đối chiếu 100 trường hợp, mỗi trường hợp 20 phút, cần khoảng 33,3 giờ công. |
| 5 | Vinhomes | AI có thể tốt hơn | Nhân viên phải tổng hợp thủ công phản ánh từ ứng dụng, hotline và App Store. Phân loại 100 phản ánh, mỗi phản ánh 6 phút, tiêu tốn khoảng 10 giờ công. |

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán (1 câu): Tự động phân loại và điều hướng phản ánh  │
│ của cư dân đến đúng bộ phận xử lý.                          │
│                                                             │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Nhân viên CSKH, Ban quản lý và cư dân. │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Nhận phản ánh                                          │
│   ──> 2. Đọc và phân loại nội dung                          │
│   ──> 3. Xác định tòa nhà, mức độ khẩn cấp                  │
│   ──> 4. Chuyển đến bộ phận phụ trách                       │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 và 3                │
│ (⏱ baseline ước tính: 5 phút/lượt)                         │
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 và 3: trích    │
│ xuất địa điểm, phân loại sự cố, đánh giá mức độ khẩn cấp    │
│ và đề xuất bộ phận xử lý để nhân viên phê duyệt.            │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│   - Giảm thời gian phân loại từ 5 phút xuống dưới 1 phút.   │
│   - Ít nhất 90% yêu cầu được đề xuất đúng bộ phận.          │
│   - Giảm tỷ lệ yêu cầu bị chuyển lại xuống dưới 5%.         │
│   - 100% sự cố an toàn phải được con người kiểm tra.        │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu): Tự động tổng hợp, gắn nhãn và gom nhóm    │
│ các phản ánh trùng lặp từ app, hotline và App Store.        │
│                                                             │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Nhân viên quản lý chất lượng, CSKH và  │
│ đội phát triển ứng dụng Vinhomes Resident.                  │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Thu thập phản ánh từ nhiều kênh                        │
│   ──> 2. Đọc và gắn nhãn từng phản ánh                      │
│   ──> 3. Kiểm tra và gom các phản ánh trùng nhau            │
│   ──> 4. Lập báo cáo, chuyển bộ phận liên quan              │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 và 3                │
│ (⏱ baseline ước tính: 6 phút/phản ánh)                      │
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 và 3: tóm tắt, │
│ phân loại chủ đề, phát hiện mức độ nghiêm trọng và gom các  │
│ phản ánh có khả năng xuất phát từ cùng một nguyên nhân.     │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│   - Giảm thời gian xử lý từ 6 phút xuống dưới 1 phút.       │
│   - Ít nhất 85% phản ánh được gắn đúng nhóm vấn đề.         │
│   - Ít nhất 80% phản ánh trùng lặp được gom đúng cụm.       │
│   - Cảnh báo phản ánh nghiêm trọng trong dưới 5 phút.       │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán (1 câu): Rút ngắn quá trình xử lý khi thông tin    │
│ chủ sở hữu không đồng bộ với tài khoản Vinhomes Resident.   │
│                                                             │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Cư dân không dùng được dịch vụ và      │
│ nhân viên CSKH phải tra cứu thông tin trên nhiều hệ thống.  │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Tiếp nhận báo lỗi tài khoản                            │
│   ──> 2. Xác minh số điện thoại và danh tính                │
│   ──> 3. Đối chiếu dữ liệu chủ sở hữu                       │
│   ──> 4. Đồng bộ dữ liệu hoặc chuyển đội kỹ thuật           │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 và 3                │
│ (⏱ baseline ước tính: 15 phút/trường hợp)                  │
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Chatbot thu thập dữ   │
│ liệu ban đầu; việc xác minh và đồng bộ sử dụng rule cố định.│
│ AI không được tự thay đổi quyền sở hữu hoặc quyền truy cập. │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│   - Giảm thời gian xử lý từ 15 phút xuống dưới 5 phút.      │
│   - Tự động định tuyến ít nhất 60% lỗi thông thường.        │
│   - Độ chính xác đối chiếu tài khoản đạt ít nhất 99,9%.     │
│   - 0 trường hợp cấp nhầm quyền truy cập căn hộ.            │
│                                                             │
│ Quick Architecture: [ ] No AI  [x] Rule  [ ] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘