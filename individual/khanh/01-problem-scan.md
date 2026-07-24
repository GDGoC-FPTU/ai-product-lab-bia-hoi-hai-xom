<!-- Bia Hoi Hai Xom - Lương Quốc Khánh -->
# 01 — Problem Scan & Quick Assess

**Thành viên:** Lương Quốc Khánh

**Use case ưu tiên:** Xanh SM (GSM) — hỗ trợ điều phối sự cố pin thấp cho taxi điện.
**Lưu ý:** Các thời gian và baseline dưới đây là giả định phục vụ lab; nhóm cần thay bằng log vận hành nếu có.

## Phase 1 — SCAN

| # | Công ty thành viên | Lens | Bài toán vận hành |
|---:|---|---|---|
| 1 | Xanh SM | Tốn thời gian | Điều phối viên nhận cuộc gọi tài xế báo pin thấp, phải ghi nhận vị trí, mức pin và tự tra cứu trạm/cứu hộ. |
| 2 | Xanh SM | Lặp lại | Tổng hợp ghi chú và cuộc gọi về lý do khách hủy chuyến để chuyển đúng nhóm vận hành xử lý. |
| 3 | Xanh SM | Stakeholder Pain | Tài xế không biết trạm sạc còn khả dụng khi gần hết pin, phải gọi tổng đài nhiều lần. |
| 4 | VinFast | Lặp lại | Đối soát bản ghi sạc và hóa đơn của trạm sạc đối tác theo tuần. |
| 5 | Vinhomes | AI-upgrade | Phân loại phản ánh cư dân như mất nước, hỏng đèn, tiếng ồn và chuyển đến đúng ban quản lý. |

## Phase 2 — QUICK-ASSESS

### Quick Problem Card #1 — Điều phối sự cố pin thấp cho tài xế Xanh SM

| Trường | Nội dung |
|---|---|
| **Bài toán** | Hỗ trợ điều phối viên xử lý nhanh tài xế taxi điện báo pin thấp hoặc có nguy cơ không đến được trạm sạc. |
| **Công ty thành viên** | Xanh SM (GSM) |
| **Actor đang gặp khó khăn** | Tài xế cần hỗ trợ khẩn; điều phối viên tổng đài cần ra quyết định an toàn. |
| **Workflow thủ công hiện tại** | 1) Tài xế gọi tổng đài. 2) Điều phối viên hỏi vị trí, mức pin, mã xe. 3) Tra cứu trạm/cứu hộ. 4) Soạn hướng dẫn. 5) Quản lý hoặc điều phối viên xác nhận và gọi lại tài xế. |
| **Bottleneck** | Thu thập thông tin thiếu/không thống nhất và tra cứu phương án phù hợp; giả định lab: khoảng 6 phút/lượt. |
| **AI hỗ trợ** | Trích xuất thông tin từ mô tả tiếng Việt, tạo bản nháp hướng dẫn. Rule engine kiểm tra pin `<5%` và buộc chuyển sang điều xe sạc di động. |
| **Metric** | Giảm thời gian tạo bản nháp từ 6 phút xuống dưới 1 phút; 100% trường hợp pin `<5%` có lệnh `dispatch_mobile_charger` và có người duyệt. |
| **Quick Architecture** | **Rule + LLM Feature**, không dùng Agent tự hành. |
| **Ranh giới** | AI không gửi tin, không tự điều xe và không bịa dữ liệu GPS/trạm sạc; mọi hướng dẫn là `[DRAFT_ONLY]` để điều phối viên duyệt. |

### Quick Problem Card #2 — Phân loại lý do hủy chuyến Xanh SM

| Trường | Nội dung |
|---|---|
| **Bài toán** | Tự phân loại ghi chú hủy chuyến và cuộc gọi đã được chuyển thành văn bản để nhóm vận hành thấy nguyên nhân lặp lại. |
| **Công ty thành viên** | Xanh SM (GSM) |
| **Actor đang gặp khó khăn** | Nhân viên vận hành phải đọc nhiều ghi chú ngắn, viết tắt và phản hồi lặp lại. |
| **Workflow thủ công hiện tại** | 1) Xuất ghi chú/cuộc gọi. 2) Đọc từng bản ghi. 3) Gán nhãn lý do. 4) Lập bảng tổng hợp. 5) Chuyển báo cáo cho đội phụ trách. |
| **Bottleneck** | Gán nhãn không nhất quán giữa nhân viên; giả định lab: 2 phút/bản ghi. |
| **AI hỗ trợ** | LLM đề xuất nhãn và tóm tắt ngắn; rule kiểm tra nhãn hợp lệ, nhân viên duyệt các bản ghi có độ tin cậy thấp. |
| **Metric** | Ít nhất 85% bản ghi được đề xuất nhãn trong dưới 10 giây; độ chính xác sau duyệt từ 90% trở lên. |
| **Quick Architecture** | **LLM Feature + Rule validation**. |
| **Ranh giới** | Không tự phạt tài xế/khách; không suy luận thông tin nhạy cảm; bản ghi không rõ phải chuyển người duyệt. |

### Quick Problem Card #3 — Điều hướng phản ánh điểm đón khó tìm

| Trường | Nội dung |
|---|---|
| **Bài toán** | Phân loại phản ánh của tài xế về điểm đón khó tìm hoặc vị trí khách không chính xác để chuyển đúng đội bản đồ/vận hành. |
| **Công ty thành viên** | Xanh SM (GSM) |
| **Actor đang gặp khó khăn** | Tài xế mất thời gian tìm khách; nhân viên hỗ trợ phải đọc và chuyển ticket thủ công. |
| **Workflow thủ công hiện tại** | 1) Tài xế gửi ghi chú. 2) CSKH đọc nội dung. 3) Tra lịch sử chuyến. 4) Phân loại lỗi bản đồ/khách/tài xế. 5) Chuyển ticket. |
| **Bottleneck** | Nội dung ngắn, nhiều viết tắt và thiếu địa chỉ chuẩn; giả định lab: 4 phút/ticket. |
| **AI hỗ trợ** | Chuẩn hóa mô tả, đề xuất loại ticket và thông tin còn thiếu để CSKH hỏi lại. |
| **Metric** | Giảm thời gian triage từ 4 phút xuống dưới 45 giây; ít nhất 80% ticket được chuyển đúng nhóm ngay lần đầu. |
| **Quick Architecture** | **LLM Feature**, có rule bắt buộc trường thông tin trước khi chuyển ticket. |
| **Ranh giới** | Không tự thay đổi tọa độ/điểm đón và không tự liên hệ khách hàng; nhân viên phê duyệt trước mọi cập nhật. |

## Lựa chọn để Deep-Dive

Nhóm nên chọn **Card #1 — Điều phối sự cố pin thấp** vì có ranh giới vận hành rõ ràng, rủi ro có thể kiểm soát bằng Human-in-the-loop và khớp với `starter-code/prompt_prototype.py`.
