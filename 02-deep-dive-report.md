# Deep-Dive Report — Xanh SM Emergency EV Charging Dispatcher

**Nhóm:** Bia Hơi Hai Xóm  
**Thành viên:** 
1. Lương Quốc Khánh (MSSV: 2A202601713 - Group Lead)
2. Cao Nhật Minh (MSSV: 2A202601721)
3. Dương Văn Vũ (MSSV: 2A202601663)
4. Trần Nguyễn Mỹ Anh (MSSV: 2A202601019)
5. Nguyễn Thu Huyền (MSSV: 2A202601027)
6. Hoàng Đức Anh (MSSV: 2A202601223)

## Quyết định lựa chọn

Nhóm chọn bài toán điều phối hỗ trợ xe Xanh SM có pin ở mức nguy cấp. Một gợi ý trạm sạc không phù hợp có thể khiến xe dừng giữa đường, ảnh hưởng an toàn tài xế, hành khách và SLA vận hành.

## 3.1. Current-State Workflow

1. Tài xế gọi tổng đài hoặc gửi chat báo mức pin và vị trí — **2 phút**.
2. Tổng đài viên hỏi lại loại xe, phần trăm pin, địa chỉ, tình trạng giao thông — **4 phút**. **🔴 Bottleneck:** thông tin thường thiếu hoặc không đồng nhất.
3. Tổng đài viên mở bản đồ/trạm sạc, kiểm tra thủ công khoảng cách và tình trạng trạm — **5 phút**. **🔄 Handoff:** tổng đài → hệ thống bản đồ/trạm sạc. Đây là **🔴 bottleneck** thứ hai.
4. Tổng đài viên gọi điều phối xe sạc lưu động hoặc hướng dẫn tài xế đến trạm — **4 phút**. **🔄 Handoff:** tổng đài → điều phối hiện trường.
5. Điều phối xác nhận và nhắn lại cho tài xế — **3 phút**.

**Tổng thời gian trung bình: 18 phút/lượt.** Bước 2–3 chiếm 9 phút và dễ sai khi tài xế đang di chuyển.

## 3.2. Problem Statement (6 fields)

| Field | Nội dung |
|---|---|
| Actor / Operator | Tổng đài viên Xanh SM, điều phối viên cứu hộ/sạc lưu động và tài xế EV. |
| Current Workflow | Tổng đài viên đọc chat/cuộc gọi, thu thập thông tin, tra cứu trạm trên nhiều màn hình, rồi chuyển yêu cầu cho điều phối. |
| Bottleneck | Chuẩn hóa thông tin vị trí và quyết định xử lý khi pin thấp; tra cứu thủ công chậm và có nguy cơ gợi ý trạm quá xa. |
| Business Impact | Xe ngừng hoạt động làm mất cuốc, tăng thời gian chờ khách và tạo rủi ro an toàn; mỗi ca hiện mất khoảng 18 phút xử lý tổng đài. |
| Success Metric | 90% yêu cầu có bản nháp điều phối dưới 60 giây; 100% ca pin dưới 5% được chuyển sang xe sạc lưu động, không gợi ý trạm xa hơn 5 km. |
| Operational Boundary | AI chỉ chuẩn hóa dữ liệu và tạo **[DRAFT_ONLY]**. AI không tự gửi tin, không tự điều xe, không bịa vị trí/trạng thái trạm. Pin <5% phải tạo `dispatch_mobile_charger`; tổng đài viên duyệt trước mọi tác động vận hành. |

## 3.3. Future-State Flow & AI Fit

**AI fit:** LLM feature có rào chắn rule-based, không phải agent tự chủ.

```text
Tài xế chat/call
  → 🔵 LLM trích xuất pin, vị trí, yêu cầu thành JSON
  → Rule engine: pin <5%? khoảng cách trạm ≤5 km?
  → 🟢 Tổng đài viên kiểm tra bản nháp [DRAFT_ONLY]
  → Điều phối viên xác nhận xe sạc / hướng dẫn trạm
  → Tài xế nhận thông báo đã được duyệt

↩ Fallback: thiếu vị trí, confidence thấp, hoặc lỗi API → tạo ticket thủ công;
  tổng đài viên gọi lại tài xế, không tự gửi hoặc tự điều xe.
```

LLM hữu ích cho tiếng Việt tự do và tóm tắt ngữ cảnh. Các quyết định khoảng cách, ngưỡng pin và quyền điều phối giữ ở rule engine có thể kiểm toán.

## 5. Evaluate

| Checklist | Trạng thái | Bằng chứng / việc cần làm |
|---|---|---|
| Có dữ liệu mẫu/log sạch? | Có điều kiện | Dùng chat/ticket đã ẩn danh; bổ sung nhãn pin, GPS, kết quả xử lý trong pilot. |
| Rủi ro AI sai được kiểm soát? | Có | Rule bắt buộc cho ngưỡng 5 km và 5%; HITL trước dispatch; fallback thủ công. |
| Stakeholders sẵn sàng đổi quy trình? | Có điều kiện | Pilot với một ca trực và đào tạo tổng đài viên dùng bản nháp thay vì tự động gửi. |

### Quyết định: GO — pilot scope hẹp

Bắt đầu pilot 4 tuần cho các ticket hỗ trợ pin nguy cấp tại một khu vực. Chi phí gồm tích hợp một màn hình ticket, API bản đồ/trạm sạc và chi phí LLM theo lượt; không cần xây agent tự chủ. Chỉ mở rộng khi dashboard chứng minh mục tiêu dưới 60 giây và không có sự cố gợi ý nguy hiểm. Quyết định dispatch cuối cùng vẫn thuộc nhân viên điều phối.
