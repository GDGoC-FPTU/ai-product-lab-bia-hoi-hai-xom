# Lab 02 — Individual Deliverable: Problem Scan & Quick Problem Cards

> **Họ và tên:** Nguyễn Thu Huyền  
> **Branch Git:** `NguyenThuHuyen`  
> **Đơn vị:** Vin Smart Future (Vingroup) — Chuyên trách mảng **Vinpearl**  
> **Môn học:** AI Product Lab  

---

## 🔍 Phase 1 — SCAN: Bảng quét cơ hội vận hành Vinpearl

Dựa trên **4 Lenses** (Lặp lại, Tốn thời gian, AI-upgrade, Stakeholder Pain), dưới đây là 5 bài toán vận hành thực tế được phát hiện tại mảng Du lịch & Resort (**Vinpearl**):

| # | Subsidiary | Lens | Tên bài toán / Bottleneck vận hành | Mô tả ngắn chi tiết bài toán |
|---|------------|------|------------------------------------|--------------------------------------------------|
| 1 | **Vinpearl** | **Time-consuming** | Tự động hóa xử lý email đặt phòng đoàn từ đại lý lữ hành (Group Booking Email Automation) | Trích xuất thông tin từ email và file đính kèm (Excel/PDF) của đối tác lữ hành B2B, tự động đối chiếu quỹ phòng và draft lệnh đặt phòng vào hệ thống PMS (Opera). |
| 2 | **Vinpearl** | **Stakeholder Pain** | Phân tích review đa kênh & Cảnh báo khiếu nại khẩn cấp (Multi-channel Review Monitoring & Escalation) | Quét tự động đánh giá từ Booking.com, Agoda, Google Maps, TripAdvisor, phân tích cảm xúc và gửi cảnh báo khẩn cấp tới General Manager khi có phản hồi tiêu cực về vệ sinh/dịch vụ. |
| 3 | **Vinpearl** | **AI-upgrade** | Trợ lý tư vấn lịch trình nghỉ dưỡng & Dịch vụ cá nhân hóa (Personalized Resort Concierge) | Chatbot/Trợ lý ảo hỗ trợ khách hàng tra cứu thông tin tour, lịch xe buggy, gợi ý dịch vụ spa/nhà hàng phù hợp với nhu cầu từng gia đình theo thời gian thực. |
| 4 | **Vinpearl** | **Repetitive** | Phân loại & Đối chiếu dữ liệu hành lý / Vật phẩm thất lạc (Lost & Found Intelligent Matcher) | Phân loại tự động thông tin mô tả vật phẩm thất lạc do du khách khai báo (văn bản/hình ảnh) và đối chiếu với cơ sở dữ liệu đồ nhặt được của bộ phận Security/Housekeeping. |
| 5 | **Vinpearl** | **Repetitive** | Đối chiếu tự động hóa đơn F&B / Dịch vụ phòng với Billing Folio trên PMS trước checkout | So khớp tự động các hóa đơn F&B, voucher ưu đãi và dịch vụ phòng do khách sử dụng tại các nhà hàng/quầy bar Vinpearl với billing folio trên PMS để phát hiện chênh lệch chỉ số trước khi khách làm thủ tục trả phòng. |

---

## 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards (Vinpearl Edition)

Chọn 3 bài toán tiềm năng nhất từ danh sách trên để phân tích chi tiết:

---

### 📌 QUICK PROBLEM CARD #1: Tự động hóa xử lý email đặt phòng đoàn (Vinpearl)

```text
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                                                       │
│                                                                                             │
│ Bài toán: Trích xuất dữ liệu email đặt phòng đoàn B2B và draft lệnh booking trên PMS        │
│ Công ty thành viên: [x] Vinpearl  [ ] VinWonders  [ ] Khác (Ghi rõ)________________________  │
│                                                                                             │
│ Ai đang đau (Actor)? Nhân viên phòng Kinh doanh (Sales Admin) & Bộ phận Đặt phòng (Reservation)│
│                                                                                             │
│ Workflow thủ công hiện tại (4 bước):                                                         │
│   1. Đại lý lữ hành gửi email kèm file Excel/PDF danh sách khách đoàn (khách sạn, loại phòng) │
│   ──> 2. Sales Admin đọc thủ công email và kiểm tra thông tin từng file đính kèm            │
│   ──> 3. Tra cứu thủ công quỹ phòng trống trên phần mềm Quản lý khách sạn (PMS Opera)        │
│   ──> 4. Nhập tay thông tin từng phòng/khách vào PMS để giữ chỗ và gửi email xác nhận báo giá  │
│                                                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 4 (Đọc hiểu dữ liệu không cấu trúc & nhập tay PMS) │
│ ⏱ Thời gian xử lý: 30 - 60 phút/đoàn                                                        │
│                                                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 4 (LLM trích xuất dữ liệu structured từ      │
│ email/Excel/PDF, gọi API check quỹ phòng và draft sẵn lệnh booking trên PMS).              │
│                                                                                             │
│ Đo thành công bằng gì (Metric có số)?                                                       │
│   - Giảm thời gian xử lý yêu cầu booking đoàn từ 45 phút ──> dưới 3 phút/đoàn                │
│   - Tăng độ chính xác nhập liệu từ 85% ──> 99%, giảm thiểu sai sót loại phòng/ngày ở        │
│                                                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM Feature  [ ] Agent                         │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

* **Lý giải kiến trúc (Quick Architecture):**  
  Sử dụng **LLM Feature** (Document/Email Parsing & Structured Output JSON). Định dạng file Excel/email của các đại lý lữ hành rất đa dạng, không cố định cấu trúc nên LLM tỏ ra vượt trội so với các công cụ đọc OCR/Rule-based truyền thống.

---

### 📌 QUICK PROBLEM CARD #2: Phân tích review đa kênh & Cảnh báo khiếu nại khẩn cấp (Vinpearl)

```text
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                                                       │
│                                                                                             │
│ Bài toán: Tự động gom review đa nền tảng, phân tích cảm xúc và cảnh báo sự cố nghiêm trọng  │
│ Công ty thành viên: [x] Vinpearl  [ ] VinWonders  [ ] Khác (Ghi rõ)________________________  │
│                                                                                             │
│ Ai đang đau (Actor)? Trưởng bộ phận Quản lý Chất lượng (QA) & General Manager khu nghỉ dưỡng │
│                                                                                             │
│ Workflow thủ công hiện tại (4 bước):                                                         │
│   1. Khách để lại đánh giá tiêu cực trên Booking.com, Agoda, Google Maps, TripAdvisor      │
│   ──> 2. Nhân viên QA đăng nhập thủ công từng trang web 1 lần/ngày để đọc và chép vào Excel  │
│   ──> 3. Phân loại thủ công nội dung phàn nàn (Vệ sinh, Thái độ phục vụ, Đồ ăn, Thiết bị)  │
│   ──> 4. Soạn báo cáo gửi Email định kỳ cho General Manager để xử lý                        │
│                                                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (Đọc và phân loại thủ công, phản ứng trễ sự cố) │
│ ⏱ Thời gian trễ xử lý: 24 - 48 giờ sau khi khách đăng review                                │
│                                                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 3 (Tự động cào/lấy API review, phân tích     │
│ cảm xúc aspect-based, cảnh báo khẩn qua Telegram/Zalo cho Manager nếu có sự cố nghiêm trọng).│
│                                                                                             │
│ Đo thành công bằng gì (Metric có số)?                                                       │
│   - Giảm thời gian phát hiện và phản hồi khiếu nại khẩn từ 24 giờ ──> dưới 15 phút          │
│   - Tăng tỷ lệ xử lý hài lòng sự cố tại chỗ trước khi khách checkout từ 30% ──> 85%         │
│                                                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM Feature  [ ] Agent                         │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

* **Lý giải kiến trúc (Quick Architecture):**  
  Sử dụng **LLM Feature** (Aspect-Based Sentiment Analysis & Classification). LLM có khả năng phân tích ngữ cảnh phức tạp trong các đoạn review dài, đa ngôn ngữ của du khách quốc tế và trích xuất đúng điểm phàn nàn chính.

---

### 📌 QUICK PROBLEM CARD #3: Trợ lý tư vấn lịch trình nghỉ dưỡng & Dịch vụ cá nhân hóa (Vinpearl)

```text
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                                                       │
│                                                                                             │
│ Bài toán: Trợ lý AI Concierge tư vấn dịch vụ resort 24/7 và hỗ trợ đặt lịch spa/nhà hàng    │
│ Công ty thành viên: [x] Vinpearl  [ ] VinWonders  [ ] Khác (Ghi rõ)________________________  │
│                                                                                             │
│ Ai đang đau (Actor)? Du khách lưu trú tại Vinpearl & Nhân viên Lễ tân / Concierge Desk      │
│                                                                                             │
│ Workflow thủ công hiện tại (4 bước):                                                         │
│   1. Du khách gọi điện thoại hoặc đến quầy Lễ tân hỏi về thông tin dịch vụ, giờ buggy, menu │
│   ──> 2. Nhân viên Lễ tân tra cứu sổ tay/hệ thống nội bộ để tư vấn giải đáp                 │
│   ──> 3. Nhân viên ghi chú thủ công yêu cầu đặt chỗ dịch vụ (Spa, Nhà hàng, Buggy)          │
│   ──> 4. Gọi điện thoại xác nhận lại với bộ phận liên quan để hoàn tất đặt dịch vụ          │
│                                                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (Xếp hàng tại Lễ tân giờ cao điểm, trễ phản hồi) │
│ ⏱ Thời gian chờ đợi: 10 - 20 phút/lượt                                                      │
│                                                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2, 3 & 4 (Trợ lý AI Concierge trên Vinpearl App/Zalo│
│ trả lời tự động 24/7, gợi ý gói dịch vụ cá nhân hóa và draft lệnh đặt chỗ vào hệ thống).   │
│                                                                                             │
│ Đo thành công bằng gì (Metric có số)?                                                       │
│   - Giảm 70% số lượng cuộc gọi/yêu cầu hỏi thông tin lặp đi lặp lại tới quầy Lễ tân        │
│   - Giảm thời gian phản hồi tư vấn dịch vụ từ 15 phút ──> dưới 10 giây/câu hỏi              │
│                                                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [ ] LLM  [x] Agent (LLM + Resort Booking APIs)     │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

* **Lý giải kiến trúc (Quick Architecture):**  
  Sử dụng **Agent** kết hợp tích hợp công cụ (Tools). Trợ lý AI cần gọi API tra cứu lịch trình resort real-time, API kiểm tra khung giờ trống của dịch vụ Spa/Nhà hàng và API tạo đơn đặt chỗ tự động.

---

## 🎯 Kết luận & Đề xuất bài toán cho thảo luận nhóm (Phase 3)

Trong 3 bài toán trên, bài toán **"QUICK PROBLEM CARD #1: Tự động hóa xử lý email đặt phòng đoàn (Vinpearl)"** hoặc **"QUICK PROBLEM CARD #2: Phân tích review đa kênh & Cảnh báo khiếu nại khẩn cấp (Vinpearl)"** là những ứng viên rất phù hợp để nhóm Vin Smart Future lựa chọn thực hiện Deep-Dive vì tính thực tế cao, dữ liệu rõ ràng và mang lại giá trị vận hành trực tiếp cho Vinpearl.
