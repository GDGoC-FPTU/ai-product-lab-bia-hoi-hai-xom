# Lab 02 — Individual Deliverable: Problem Scan & Quick Problem Cards

> **Họ và tên:** Nguyễn Thu Huyền  
> **Branch Git:** `NguyenThuHuyen`  
> **Đơn vị:** Vin Smart Future (Vingroup)  
> **Môn học:** AI Product Lab  

---

## 🔍 Phase 1 — SCAN: Bảng quét cơ hội vận hành Vingroup

Dựa trên **4 Lenses** (Lặp lại, Tốn thời gian, AI-upgrade, Stakeholder Pain), dưới đây là 5 bài toán vận hành thực tế tại các công ty thành viên thuộc Tập đoàn Vingroup:

| # | Công ty thành viên (Subsidiary) | Thấu kính (Lens) | Tên bài toán / Bottleneck vận hành | Mô tả ngắn chi tiết bài toán |
|---|----------------------------------|------------------|------------------------------------|--------------------------------------------------|
| 1 | **VinFast & Xanh SM** | **AI-upgrade** & **Stakeholder Pain** | Trợ lý điều phối trạm sạc khẩn cấp & Cứu hộ pin di động cho xe điện | Tự động phân tích dung lượng pin khẩn cấp, tọa độ GPS thực tế, công suất trụ sạc khả dụng để đề xuất trạm sạc tối ưu hoặc kích hoạt xe sạc lưu động cứu hộ khi pin dưới 5%. |
| 2 | **Vinhomes** | **Lặp lại (Repetitive)** | Phân loại & Điều hướng phản ánh cư dân qua App Vinhomes Resident | Phân loại tự động hàng ngàn yêu cầu/khiếu nại gửi về qua ứng dụng (mất nước, hỏng đèn, tiếng ồn, an ninh) và điều chuyển đúng Ban Quản lý từng phân khu/tòa nhà. |
| 3 | **Vinmec** | **Tốn thời gian (Time-consuming)** | Tự động soạn thảo bản tóm tắt hồ sơ xuất viện (Discharge Summary Assistant) | Trích xuất thông tin lâm sàng, lịch sử dùng thuốc, kết quả xét nghiệm từ bệnh án điện tử (EHR) để tự động draft tóm tắt xuất viện bằng ngôn ngữ phổ thông cho bệnh nhân. |
| 4 | **Vinpearl / VinWonders** | **Stakeholder Pain** | Phân tích cảm xúc & Tự động cảnh báo sự cố khẩn cấp từ đánh giá khách hàng | Quét bài đánh giá trên các nền tảng OTA (Booking.com, Agoda, Google Maps), phân loại phản hồi tiêu cực và gửi cảnh báo khẩn tới General Manager đối với sự cố vệ sinh/thái độ dịch vụ. |
| 5 | **VinFast** | **Lặp lại (Repetitive)** | Đối chiếu dữ liệu sạc điện & Hóa đơn đối tác trạm sạc nhượng quyền | So khớp dữ liệu sạc điện telemetry hàng tuần từ hàng nghìn trụ sạc liên kết bên ngoài với hóa đơn tài chính gửi về hệ thống kế toán nhằm phát hiện chênh lệch chỉ số. |

---

## 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Chọn 3 bài toán tiềm năng nhất từ danh sách trên để phân tích sơ bộ:

---

### 📌 QUICK PROBLEM CARD #1: Điều phối trạm sạc khẩn cấp & Cứu hộ pin di động (VinFast / Xanh SM)

```text
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                                                       │
│                                                                                             │
│ Bài toán: Hỗ trợ điều hướng trạm sạc và kích hoạt xe sạc cứu hộ lưu động khi xe báo pin yếu │
│ Công ty thành viên: [x] VinFast  [x] Xanh SM  [ ] Vinhomes  [ ] Vinmec  [ ] Khác            │
│                                                                                             │
│ Ai đang đau (Actor)? Tài xế Xanh SM & Chủ xe điện VinFast gặp sự cố hết pin/pin khẩn cấp     │
│                                                                                             │
│ Workflow thủ công hiện tại (5 bước):                                                         │
│   1. Xe báo pin yếu/khẩn cấp (< 10%)                                                       │
│   ──> 2. Tài xế gọi Tổng đài hỗ trợ / Tự tìm trạm sạc trên app                              │
│   ──> 3. Tổng đài viên kiểm tra vị trí xe & tra cứu bản đồ trạm sạc thủ công                 │
│   ──> 4. Tổng đài viên xác nhận tình trạng trụ trống qua gọi điện cho quản lý trạm           │
│   ──> 5. Soạn tin nhắn hướng dẫn tài xế tới trạm hoặc tạo lệnh điều xe cứu hộ sạc          │
│                                                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 & 4 (Tra cứu thủ công & xác nhận trụ)               │
│ ⏱ Thời gian xử lý: 10 - 15 phút/lượt                                                       │
│                                                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3, 4 & 5 (Tự động đọc GPS + SOC pin, gợi ý trạm    │
│ phù hợp và draft tin nhắn/lệnh điều xe sạc di động).                                        │
│                                                                                             │
│ Đo thành công bằng gì (Metric có số)?                                                       │
│   - Giảm thời gian xử lý yêu cầu hỗ trợ sạc từ 12 phút ──> dưới 2 phút/lượt                 │
│   - Giảm 90% nguy cơ xe nằm đường chết pin do được điều xe sạc di động kịp thời khi pin < 5%  │
│                                                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [ ] LLM  [x] Agent (LLM + Tools integration)       │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

* **Lý giải kiến trúc (Quick Architecture):**  
  Cần sử dụng **Agent** kết hợp LLM Feature. Hệ thống cần gọi Tool tra cứu vị trí GPS thực tế, API tình trạng trụ sạc trống theo thời gian thực (Real-time Occupancy API) và API kiểm tra tọa độ xe sạc di động gần nhất để ra quyết định điều hướng chính xác.

---

### 📌 QUICK PROBLEM CARD #2: Phân loại & Điều hướng phản ánh cư dân (Vinhomes)

```text
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                                                       │
│                                                                                             │
│ Bài toán: Phân loại và phân luồng tự động ý kiến/khiếu nại của cư dân trên App Vinhomes     │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes  [ ] Vinmec  [ ] Khác            │
│                                                                                             │
│ Ai đang đau (Actor)? Nhân viên CSKH Ban quản lý tòa nhà Vinhomes & Cư dân khu đô thị         │
│                                                                                             │
│ Workflow thủ công hiện tại (4 bước):                                                         │
│   1. Cư dân gửi phản ánh (văn bản/hình ảnh) trên App Vinhomes Resident                      │
│   ──> 2. Điều phối viên CSKH trung tâm đọc thủ công từng ticket                              │
│   ──> 3. Phân loại nhóm sự cố (Kỹ thuật/Vệ sinh/An ninh/Cảnh quan) và gán độ ưu tiên          │
│   ──> 4. Chuyển ticket về Ban Quản lý từng tòa nhà/phân khu xử lý                            │
│                                                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (Đọc hiểu văn bản mô tả tự do & phân loại)      │
│ ⏱ Thời gian xử lý: 15 - 30 phút/ticket                                                      │
│                                                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 3 (Đọc hiểu văn bản tiếng Việt tự nhiên,     │
│ trích xuất loại sự cố, gán tag ưu tiên và đề xuất Ban Quản lý tiếp nhận).                   │
│                                                                                             │
│ Đo thành công bằng gì (Metric có số)?                                                       │
│   - Tăng tốc độ phân luồng ticket phản ánh từ 20 phút ──> dưới 30 giây/ticket               │
│   - Đạt độ chính xác phân loại tự động > 92%, giảm 80% công sức phân loại thủ công           │
│                                                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM Feature  [ ] Agent                         │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

* **Lý giải kiến trúc (Quick Architecture):**  
  Sử dụng **LLM Feature** (Text Classification & Structured Output). Ngôn ngữ cư dân mô tả rất tự do, nhiều từ địa phương hoặc viết tắt (ví dụ: *"tòa S2.01 thang máy kêu rè rè lắc mạnh"*, *"nước chảy yếu quá"*) nên LLM xử lý vượt trội so với Rule-based thông thường.

---

### 📌 QUICK PROBLEM CARD #3: Soạn thảo bản tóm tắt hồ sơ xuất viện (Vinmec)

```text
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                                                       │
│                                                                                             │
│ Bài toán: Trích xuất và soạn thảo tự động bản tóm tắt xuất viện dễ hiểu cho bệnh nhân        │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  [x] Vinmec  [ ] Khác            │
│                                                                                             │
│ Ai đang đau (Actor)? Bác sĩ điều trị / Điều dưỡng Vinmec & Bệnh nhân xuất viện              │
│                                                                                             │
│ Workflow thủ công hiện tại (4 bước):                                                         │
│   1. Bác sĩ/Điều dưỡng tổng hợp dữ liệu từ bệnh án điện tử EHR (kết quả xét nghiệm, đơn thuốc)│
│   ──> 2. Bác sĩ gõ thủ công bản tóm tắt quá trình điều trị và dặn dò sau xuất viện          │
│   ──> 3. Điều dưỡng kiểm tra lại thông tin và in bản cứng                                   │
│   ──> 4. Bác sĩ giải thích trực tiếp cho bệnh nhân khi làm thủ tục xuất viện                │
│                                                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 (Tổng hợp dữ liệu rải rác & gõ bản tóm tắt)         │
│ ⏱ Thời gian xử lý: 25 - 40 phút/hồ sơ                                                       │
│                                                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 (Trích xuất thông tin chính từ EHR và soạn     │
│ nháp bản tóm tắt xuất viện bằng thuật ngữ phổ thông, kèm dặn dò dùng thuốc).               │
│                                                                                             │
│ Đo thành công bằng gì (Metric có số)?                                                       │
│   - Giảm thời gian soạn thảo bản tóm tắt xuất viện từ 30 phút ──> dưới 5 phút (Human-in-the-loop)│
│   - Giảm 100% sai lệch thông tin liều dùng thuốc nhờ tự động đối chiếu dữ liệu EHR           │
│                                                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM Feature  [ ] Agent                         │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

* **Lý giải kiến trúc (Quick Architecture):**  
  Sử dụng **LLM Feature** với quy trình kiểm duyệt **Human-in-the-Loop (HITL)** nghiêm ngặt. LLM giúp gom thông tin y khoa phức tạp và biên dịch thành ngôn ngữ dễ hiểu cho bệnh nhân. Bác sĩ bắt buộc phải ký duyệt bản nháp trước khi in cho bệnh nhân nhằm đảm bảo an toàn tuyệt đối.

---

## 🎯 Kết luận & Đề xuất bài toán cho thảo luận nhóm (Phase 3)

Trong 3 bài toán trên, bài toán **"QUICK PROBLEM CARD #1: Điều phối trạm sạc khẩn cấp & Cứu hộ pin di động (VinFast / Xanh SM)"** là ứng viên sáng giá nhất để nhóm Vin Smart Future lựa chọn thực hiện Deep-Dive vì:
1. Gắn liền trực tiếp với hoạt động cốt lõi của VinFast & Xanh SM (Hệ sinh thái xe điện).
2. Tác động kinh doanh trực tiếp đến trải nghiệm tài xế/khách hàng và giảm tỷ lệ hủy chuyến do cố hết pin.
3. Ranh giới an toàn (Operational Boundary) rõ ràng: Ranh giới pin < 5% không khuyến nghị trạm sạc xa > 5km mà phải kích hoạt điều xe cứu hộ pin di động.
