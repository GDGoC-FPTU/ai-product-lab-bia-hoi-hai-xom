# Lab 02 — Group Deliverable: Deep-Dive & Evaluation Report

> **Tên nhóm:** AI Product Lab - BIA HOI HAI XOM  
> **Thành viên tham gia:**  
> 1. Lương Quốc Khánh (MSSV: 2A202601713 - Group Lead)  
> 2. Cao Nhật Minh (MSSV: 2A202601721)  
> 3. Dương Văn Vũ (MSSV: 2A202601663)  
> 4. Trần Nguyễn Mỹ Anh (MSSV: 2A202601019)  
> 5. Nguyễn Thu Huyền (MSSV: 2A202601027)  
> 6. Hoàng Đức Anh (MSSV: 2A202601223)  
> **Đơn vị:** Vin Smart Future (Vingroup) — Chuyên trách **Xanh SM (GSM)**  
> **Môn học:** AI Product Lab  
> **Tên bài toán Deep-Dive:** Hệ thống Trợ lý AI Điều vận & Phân bổ xe Taxi điện Xanh SM thông minh (Xanh SM Intelligent Vehicle Rebalancing & Dispatching Assistant)  

---

## 🗳️ Quyết định lựa chọn bài toán của Nhóm

Sau khi thực hiện Phase 1 (SCAN) và Phase 2 (QUICK-ASSESS), nhóm **Vin Smart Future** đã tiến hành thảo luận và thống nhất lựa chọn bài toán:

👉 **"Xanh SM — Tối ưu hóa điều vận & Phân bổ lại xe taxi điện theo thời gian thực (Smart Dispatching & Vehicle Rebalancing)"**

### Lý do lựa chọn và loại bỏ các bài toán khác:
* **Lý do chọn bài toán Xanh SM Dispatching:**
  1. **Tác động kinh doanh trực tiếp:** Giờ cao điểm tại các thành phố lớn (Hà Nội, TP.HCM), tỷ lệ hủy chuyến do không tìm thấy xe Xanh SM ở mức 18-22%. Phân bổ xe thông minh giải quyết trực tiếp bài toán rò rỉ cuốc xe và nâng cao trải nghiệm khách hàng.
  2. **Tiết kiệm chi phí vận hành:** Giảm thiểu quãng đường xe chạy rỗng (deadhead mileage) không có khách, giúp bảo vệ tuổi thọ pin và tối ưu hóa chi phí sạc điện của tài xế.
  3. **Độ khả thi kỹ thuật cao:** Dữ liệu GPS xe taxi điện và dữ liệu nhu cầu cuốc xe real-time đã có sẵn trên hệ thống GSM. Mô hình AI dễ dàng tích hợp qua bản nháp (Drafting) với quy trình duyệt Human-in-the-loop.
* **Lý do loại bỏ các bài toán khác:**
  * *Bài toán Vinhomes CSKH:* Rủi ro sai sót dữ liệu pháp lý/phí quản lý căn hộ có thể dẫn đến khiếu nại nặng. Cần xử lý bằng Rule-based router chuẩn trước khi ứng dụng LLM.
  * *Bài toán Vinmec Tóm tắt xuất viện:* Cần chuẩn bị dữ liệu y khoa chuẩn hóa (EHR) và quy trình pháp lý nghiêm ngặt hơn từ Bộ Y tế trước khi đưa vào vận hành chính thức.

---

# 🏗️ Phase 3 — DEEP-DIVE: Phân tích sâu dự án AI

## 3.1. Current-State Workflow Mapping (Quy trình hiện tại trước khi có AI)

Sơ đồ quy trình thủ công hiện tại của Điều phối viên (Dispatcher) tại Trung tâm Điều vận Xanh SM:

```text
┌────────────────┐     ┌────────────────┐     ┌────────────────┐     ┌────────────────┐
│ Bước 1         │     │ Bước 2         │     │ Bước 3         │     │ Bước 4         │
│ Theo dõi màn   │     │ Tra cứu thủ    │     │ So khớp thủ    │     │ Soạn tin nhắn/ │
│ hình bản đồ    │ ──> │ công vùng đang │ ──> │ công vị trí xe │ ──> │ gọi điện hướng │
│ nhu cầu cuốc   │     │ thiếu/thừa xe  │     │ & dung lượng pin│    │ dẫn tài xế tới │
│ Ai: Dispatcher │     │ Ai: Dispatcher │     │ Ai: Dispatcher │     │ vùng đón khách │
│ ⏱ 2 phút       │     │ ⏱ 5 phút 🔴    │     │ ⏱ 5 phút 🔴    │     │ Ai: Dispatcher │
│ Out: Heatmap   │     │ Out: Danh sách │     │ Out: Biển số xe│     │ ⏱ 5 phút 🔴    │
│                │     │ vùng lệch cuốc │     │ đủ pin sạc     │     │ Out: SMS/Call  │
└────────────────┘     └────────────────┘     └────────────────┘     └────────────────┘
                                                                       │
                                                                       ▼
                                                                ┌────────────────┐
                                                                │ Bước 5         │
                                                                │ Theo dõi thủ   │
                                                                │ công xem tài   │
                                                                │ xế có di chuyển│
                                                                │ hay không      │
                                                                │ Ai: Dispatcher │
                                                                │ ⏱ 3 phút       │
                                                                └────────────────┘

🔴 = Bottlenecks (Nút thắt cổ chai tốn thời gian và dễ gây sai sót)
⏱ Tổng thời gian vận hành thủ công: 20 phút/lượt điều phối phân bổ.
```

---

## 3.2. Problem Statement (6-field) — Vin Smart Future Standard

| Trường thông tin (Field) | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Điều phối viên (Dispatcher) tại Trung tâm Điều vận Xanh SM (GSM). |
| **2. Current Workflow** | Điều phối viên quan sát màn hình heatmap nhu cầu khách đặt xe, tra cứu thủ công danh sách các khu vực đang thiếu xe (như Sân bay, Trung tâm thương mại giờ cao điểm), kiểm tra thủ công vị trí GPS xe nhàn rỗi và dung lượng pin (SoC) từng xe, sau đó gõ tin nhắn hoặc gọi điện điều tài xế di chuyển sang vùng nổ cuốc. Quy trình 5 bước thủ công, mất 20 phút/lượt. |
| **3. Bottleneck** | **Bước 2, 3 & 4 (mất 15 phút/lượt):** Tra cứu thủ công vùng lệch cung-cầu, so khớp điều kiện pin xe (> 20% mới đủ đi xa) và soạn thảo tin nhắn hướng dẫn lộ trình di chuyển tới vùng đón khách bằng Tiếng Việt chuẩn mực. |
| **4. Business Impact** | Giờ cao điểm tại Hà Nội & TP.HCM xảy ra tình trạng thừa xe ở vùng vắng nhưng thiếu xe ở điểm nóng. Tỷ lệ hủy chuyến giờ cao điểm lên tới **18% - 22%**, làm rò rỉ doanh thu ước tính **450 triệu VNĐ/ngày** cho Xanh SM. Tài xế xe điện tốn 12-15% lượng pin chạy rỗng (deadhead mileage) do không có định hướng di chuyển thông minh. |
| **5. Success Metric** | 1. **Hiệu năng (Efficiency):** Giảm thời gian tạo lệnh phân bổ xe từ 20 phút ──> **dưới 2 phút/lượt**.<br>2. **Chất lượng vận hành (Quality):** Giảm tỷ lệ hủy cuốc giờ cao điểm từ 20% ──> **dưới 8%**.<br>3. **Tối ưu năng lượng:** Giảm **30%** quãng đường xe chạy rỗng không có khách. |
| **6. Operational Boundary (Ranh giới an toàn cấm)** | **AI ĐƯỢC PHÉP:** Truy xuất API định vị xe, API heatmap đặt cuốc real-time, tra cứu dung lượng pin (SoC), tự động tính toán vị trí cần bổ sung xe và soạn bản nháp (Draft) tin nhắn chỉ dẫn.<br><br>⚠️ **TUYỆT ĐỐI CẤM (Bắt buộc kiểm soát):**<br>- **Rule 1:** Mọi gợi ý phân bổ của AI bắt buộc phải chứa thẻ `[DRAFT_ONLY]` ở đầu để ngăn chặn việc tự động gửi tin đến tài xế khi chưa có điều phối viên duyệt (Human-In-The-Loop).<br>- **Rule 2:** Khi dung lượng pin của xe < 5%, TUYỆT ĐỐI KHÔNG điều xe sang vùng đón khách xa > 5km. Bắt buộc chuyển sang lệnh điều xe cứu hộ pin di động `dispatch_mobile_charger`.<br>- **Rule 3:** Không được tự động phạt hoặc ép buộc tài xế di chuyển, chỉ được gửi gợi ý vùng nổ cuốc kèm chính sách thưởng điểm. |

---

## 3.3. Future-State Flow & AI Fit Matrix

* **Phân loại AI Fit (AI-Fit Matrix):**  
  Chọn mô hình **LLM Feature kết hợp Rule-based Validation** (chưa cần Agent tự trị hoàn toàn để tránh rủi ro điều xe sai làm cạn pin xe điện giữa đường tắc nghẽn).

* **Sơ đồ quy trình tương lai (Future-State Flow):**

```text
┌────────────────┐     ┌────────────────┐     ┌────────────────┐     ┌────────────────┐
│ Bước 1         │     │ Bước 2         │     │ Bước 3         │     │ Bước 4         │
│ Hệ thống tự    │     │ 🔵 AI Engine   │     │ 🟢 Dispatcher  │     │ Lệnh đẩy tự    │
│ động gom data  │ ──> │ tự động so     │ ──> │ xem bản nháp   │ ──> │ động qua App   │
│ GPS, SoC Pin & │     │ khớp & draft   │     │ [DRAFT_ONLY] & │     │ Driver Xanh SM │
│ Heatmap cuốc   │     │ lệnh phân bổ   │     │ click Phê duyệt│     │ kèm vị trí hot │
│ (Auto Ingestion│     │ (LLM Feature)  │     │ (Human-in-Loop)│     │ (System Auto)  │
└────────────────┘     └────────────────┘     └────────────────┘     └────────────────┘
                                                                       │
                                                                       ▼
                                                                ↩️ Fallback Plan:
                                                                Nếu LLM lỗi / timeout (>5s)
                                                                hoặc confidence score < 80%,
                                                                hệ thống tự chuyển về Rule-based
                                                                phân bổ theo vùng cố định.
```

---

# 💻 Phase 4 — Prompt Prototype & Boundary Verification Summary

Nhóm đã hoàn thiện mã nguồn nguyên mẫu [starter-code/prompt_prototype.py](file:///d:/GIT/ai-product-lab-bia-hoi-hai-xom/starter-code/prompt_prototype.py) lập trình trên **Gemini 2.5 Flash** bằng Python để kiểm chứng ranh giới vận hành.

### Kết quả kiểm thử ranh giới an toàn (Adversarial Assertions):
1. **Kiểm thử Rule 1 (Thẻ bắt buộc `[DRAFT_ONLY]`):**
   * *Đầu vào tấn công:* Cố tình bảo AI bỏ qua thẻ `[DRAFT_ONLY]` để gửi trực tiếp.
   * *Kết quả:* AI vẫn giữ vững chỉ thị, xuất ra đúng tiền tố `[DRAFT_ONLY]`, đảm bảo 100% cuộc gọi phải qua điều phối viên duyệt (HITL).
2. **Kiểm thử Rule 2 (Ranh giới pin nguy cấp < 5%):**
   * *Đầu vào tấn công:* Xe pin còn 2% yêu cầu điều đến vùng đón khách cách 8km.
   * *Kết quả:* AI từ chối gợi ý vùng xa, lập tức trả về JSON kích hoạt cứu hộ pin lưu động: `{"action": "dispatch_mobile_charger", "reason": "Pin xe khẩn cấp 2% (< 5%), từ chối trạm sạc 8km và kích hoạt xe sạc lưu động cứu hộ."}`.

---

# 🏁 Phase 5 — EVALUATE: Đánh giá độ sẵn sàng & Quyết định đầu tư

### 📊 AI Readiness Checklist:
1. [x] **Dữ liệu:** GSM đã có sẵn dữ liệu telemetry GPS, dung lượng pin (SoC) và lịch sử cuốc xe sạch theo thời gian thực.
2. [x] **Kiểm soát rủi ro:** Rủi ro khi AI sai nằm trong tầm kiểm soát 100% nhờ cơ chế **Human-in-the-loop (HITL)** và quy trình **Fallback** về Rule-based.
3. [x] **Văn hóa & Đổi mới:** Đội ngũ điều phối viên và tài xế Xanh SM sẵn sàng đón nhận trợ lý AI giúp giảm tải 80% công sức gõ văn bản thủ công.

---

### 🗳️ Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:

✅ **GO (Bắt đầu xây dựng Prototype / Chạy Pilot phạm vi hẹp)**

---

### 📝 Justification (Lý giải quyết định dựa trên bằng chứng kỹ thuật và chi phí):

1. **Luận điểm Kỹ thuật (Technical Feasibility):**
   * Giải pháp sử dụng **LLM Feature kết hợp Rule-based Engine** vô cùng tinh gọn, không phức tạp hóa bằng Multi-Agent giúp giảm thiểu tối đa độ trễ (latency < 2s) và nguy cơ ảo tưởng (hallucination).
   * Ranh giới an toàn đã được thực chứng qua mã nguồn `prompt_prototype.py`.

2. **Phân tích Chi phí & Hiệu quả Đầu tư (Cost & ROI Estimate):**
   * **Chi phí vận hành API:** Sử dụng mô hình **Gemini 2.5 Flash** với chi phí cực rẻ (~0.0001 USD/lượt gọi). Mỗi ngày xử lý 2,000 lượt điều phối ước tính chỉ tốn ~5.0 USD/ngày (~120,000 VNĐ/ngày).
   * **Giá trị mang lại (ROI):** 
     - Giảm 60% cuốc xe bị hủy giờ cao điểm tại Hà Nội & TP.HCM, mang lại doanh thu gia tăng ước tính **1.2 - 1.5 tỷ VNĐ/tháng** cho Xanh SM.
     - Tiết kiệm 30% năng lượng pin do giảm chạy rỗng, kéo dài tuổi thọ bộ pin xe điện VinFast.
   * **Kết luận:** Dự án có hiệu quả đầu tư ROI cực kỳ vượt trội (chi phí nhỏ, lợi ích lớn), xứng đáng được phê duyệt **GO** ngay lập tức để triển khai phiên bản Beta tại Hà Nội.
