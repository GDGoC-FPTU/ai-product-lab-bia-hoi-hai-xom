# 🔍 Phase 1 — SCAN & Phase 2 — QUICK-ASSESS

**Họ và tên:** *Hoàng Đức Anh*  
**Công ty / Dự án:** Vin Smart Future (Vingroup)

---

## 🔍 Phase 1 — SCAN

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | VinFast | Lặp lại | Tự động so khớp & đối chiếu dữ liệu hóa đơn giao dịch sạc điện giữa trạm sạc VinFast và các trạm sạc đối tác hằng tuần. |
| 2 | VinFast | Tốn thời gian | Phân loại & trích xuất lỗi từ log kỹ thuật xe điện (BMS/ECU) gửi về từ Xưởng dịch vụ để gợi ý quy trình xử lý cho kỹ thuật viên. |
| 3 | VinFast | Stakeholder Pain | Tự động phân loại mức độ khẩn cấp và draft câu trả lời xử lý khiếu nại của chủ xe về sự cố sạc pin / lỗi phần mềm trên App CSKH. |
| 4 | Xanh SM / VinFast | Stakeholder Pain | Driver Risk & Fleet Intelligence: Tích hợp tín hiệu DMS (buồn ngủ, xao nhãng) & Telemetry thời gian thực để cảnh báo nguy hiểm và tính điểm rủi ro chuyến đi (Risk Fusion Score) cho Quản lý đội xe để đánh giá khả năng lái xe an toàn của tài xế. |
| 5 | Xanh SM / VinFast | AI-upgrade | Automated Post-trip Coaching: Tự động phân tích xu hướng hành vi tài xế sau chuyến đi từ video DMS + telemetry để tạo báo cáo hướng dẫn an toàn (Coaching Report) gửi qua Email/API. |

---

## 🃏 Phase 2 — QUICK-ASSESS (3 Quick Problem Cards)

```text
┌─────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #4 — DRIVER RISK & FLEET INTELLIGENCE                │
│                                                                         │
│ Bài toán (1 câu): Tích hợp tín hiệu DMS (buồn ngủ, xao nhãng) &        │
│ Telemetry thời gian thực để cảnh báo nguy hiểm khẩn cấp và tính điểm    │
│ rủi ro chuyến đi (Risk Fusion Score) cho Quản lý đội xe.                │
│ Công ty thành viên: [x] Xanh SM (GSM)   [x] VinFast Fleet               │
│                                                                         │
│ Ai đang đau (Actor)? Fleet Manager (thiếu góc nhìn rủi ro tổng thể),    │
│                     Tài xế (không nhận biết nguy cơ xao nhãng).         │
│                                                                         │
│ Workflow thủ công hiện tại (4 bước):                                    │
│   1. Xe chạy ──> 2. Camera DMS / Telemetry phát hiện vi phạm rải rác   │
│   ──> 3. Cảnh báo phát âm thanh tại chỗ ──> 4. Quản lý chỉ biết       │
│   sự cố sau khi va chạm xảy ra.                                         │
│                                                                         │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 & 4 (⏱ mất 30-60 phút/lượt)     │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3 & 4                        │
│ (Hợp nhất tín hiệu DMS + Telemetry thời gian thực -> Tính Risk Score)   │
│                                                                         │
│ Đo thành công bằng gì (Metric có số)?                                   │
│ Giảm thời gian phát hiện rủi ro hạm xe từ 45 min ──> under 5 sec;       │
│ giảm 35% sự cố mất tập trung nghiêm trọng.                             │
│                                                                         │
│ Quick Architecture: [ ] No AI  [ ] Rule  [ ] LLM  [x] Agent / AI Fusion │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #5 — AUTOMATED POST-TRIP DRIVER COACHING             │
│                                                                         │
│ Bài toán (1 câu): Tự động phân tích xu hướng hành vi tài xế sau chuyến  │
│ đi từ video DMS + telemetry để tạo báo cáo hướng dẫn an toàn            │
│ (Coaching Report) gửi qua Email/API.                                   │
│ Công ty thành viên: [x] Xanh SM (GSM)   [x] VinFast Fleet               │
│                                                                         │
│ Ai đang đau (Actor)? Chuyên viên An toàn giao thông / Đào tạo tài xế    │
│ (mất nhiều thời gian xem lại video và chấm điểm thủ công).              │
│                                                                         │
│ Workflow thủ công hiện tại (4 bước):                                    │
│   1. Chuyến đi kết thúc ──> 2. Chuyên viên trích xuất video vi phạm    │
│   ──> 3. Đánh giá và ghi chép nhận xét bằng Excel ──> 4. Gửi email      │
│   nhắc nhở tài xế vào cuối tuần.                                        │
│                                                                         │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ mất 20-30 phút/tài xế)   │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2, 3 & 4                     │
│ (LLM trích xuất event -> Tự động sinh 3 điểm cải thiện -> Xuất báo cáo) │
│                                                                         │
│ Đo thành công bằng gì (Metric có số)?                                   │
│ Giảm thời gian tạo báo cáo coaching từ 30 min/tài xế ──> under 3 sec;   │
│ 100% chuyến đi được phản hồi tức thì.                                   │
│                                                                         │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent             │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2 — VINFAST BMS/ECU LOG DIAGNOSTICS                 │
│                                                                         │
│ Bài toán (1 câu): Phân loại và trích xuất lỗi từ log kỹ thuật xe điện   │
│ (BMS/ECU) gửi về từ Xưởng dịch vụ để gợi ý quy trình sửa chữa cho      │
│ kỹ thuật viên.                                                          │
│ Công ty thành viên: [x] VinFast                                         │
│                                                                         │
│ Ai đang đau (Actor)? Kỹ thuật viên chẩn đoán lỗi tại Service Center.    │
│                                                                         │
│ Workflow thủ công hiện tại (4 bước):                                    │
│   1. Xe vào xưởng ──> 2. Cắm máy cào tệp log BMS/ECU hàng ngàn dòng    │
│   ──> 3. Tra cứu thủ công trong tài liệu hướng dẫn (Manual) ──> 4. Đưa   │
│   ra phương án sửa chữa.                                                │
│                                                                         │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ mất 45-60 phút/lượt)     │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 3                        │
│ (LLM phân tích log -> Trích xuất nguyên nhân -> Gợi ý quy trình sửa)    │
│                                                                         │
│ Đo thành công bằng gì (Metric có số)?                                   │
│ Giảm thời gian chẩn đoán lỗi từ 60 min ──> under 5 min;                 │
│ tăng độ chính xác gợi ý sửa chữa lên > 90%.                             │
│                                                                         │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent             │
└─────────────────────────────────────────────────────────────────────────┘
```
