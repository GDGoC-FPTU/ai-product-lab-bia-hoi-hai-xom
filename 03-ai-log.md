# 📝 Phase 6 — REFLECTION (AI Log & Self-Reflection)

**Họ và tên:** Hoàng Đức Anh  
**Vai trò:** AI Product Engineer — Vin Smart Future  
**Dự án:** Driver Intelligence Platform & VinFast EV Operations  

---

## 1. 🤖 AI đã đóng vai trò Trợ lý đồng hành (Thought-partner) như thế nào?

Trong suốt quá trình thực hiện bài lab, tôi đã sử dụng các mô hình AI (ChatGPT / Gemini) như một đồng nghiệp phản biện và mở rộng tư duy thiết kế sản phẩm:

* **Brainstorm bài toán vận hành:** AI giúp tôi rà soát các điểm nghẽn (bottlenecks) thực tế trong hệ sinh thái Vingroup (VinFast, Xanh SM), nổi bật là việc đề xuất ý tưởng tích hợp camera DMS (Driver Monitoring System) với dữ liệu cảm biến Telemetry cho hệ thống *Driver Intelligence Platform*.
* **Chuẩn hóa các thẻ bài toán (Quick Cards):** AI hỗ trợ bóc tách quy trình vận hành thủ công thành 4 bước rõ ràng, xác định chính xác bước tốn thời gian nhất và đưa ra các chỉ số đo lường hiệu quả (Metrics) bằng số định lượng (ví dụ: giảm thời gian phát hiện rủi ro từ 45 phút xuống dưới 5 giây).
* **Thiết lập ranh giới vận hành (Operational Boundary):** Trợ giúp gợi ý các quy tắc nghiêm ngặt để đảm bảo mô hình AI luôn hoạt động trong phạm vi an toàn, có con người kiểm duyệt (Human-in-the-loop) và có cơ chế dự phòng (Fallback).

---

## 2. ⚠️ AI đã đưa ra câu trả lời sai lệch (Hallucination) hoặc giải pháp chưa tối ưu ở điểm nào?

* **Lạm dụng LLM cho các tác vụ thời gian thực (Real-time Processing):** Ban đầu AI đề xuất sử dụng trực tiếp mô hình ngôn ngữ lớn (LLM) để phân tích luồng video camera DMS ở tốc độ 30 khung hình/giây. Đề xuất này không thực tế vì độ trễ (latency) của LLM quá cao và chi phí gọi API sẽ vượt ngoài tầm kiểm soát khi mở rộng cho toàn bộ hạm xe.
* **Tối ưu hóa thái quá bằng AI cho các tác vụ Rule-based:** AI có xu hướng đề xuất các giải pháp AI/LLM cho cả những tác vụ truy vấn dữ liệu tĩnh (như tra cứu vị trí trạm sạc VinFast gần nhất hay tra mã lỗi xe đơn giản), vốn chỉ cần các thuật toán Rule-based hoặc truy vấn CSDL thông thường để đạt tốc độ tức thì và độ chính xác 100%.

---

## 3. 🛠️ Tôi đã điều chỉnh Prompt, Kiến trúc & Ranh giới an toàn như thế nào?

* **Tách bạch kiến trúc Hybrid (Rule/Edge AI + LLM Feature):** 
  * Các cảnh báo khẩn cấp thời gian thực (buồn ngủ, xao nhãng) được chuyển sang xử lý bằng mô hình Edge AI nhẹ kết hợp luật Rule-based ngay trên thiết bị xe.
  * Mô hình LLM chỉ được áp dụng ở những tác vụ xử lý ngôn ngữ tự động và tổng hợp dữ liệu sau chuyến đi (*Automated Post-trip Driver Coaching Report*).
* **Bổ sung ranh giới an toàn cấm (Hard Operational Boundaries):** Trong System Prompt của prototype, tôi đã cài đặt ranh giới an toàn nghiêm ngặt:
  > *"AI chỉ đóng vai trò phân tích dữ liệu, cảnh báo và tự động sinh bản nháp báo cáo; TUYỆT ĐỐI KHÔNG được phép trực tiếp can thiệp vào hệ thống điều khiển xe điện hoặc đưa ra các quyết định xử phạt tài xế mà không có sự kiểm duyệt của Fleet Manager."*
