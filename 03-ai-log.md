<!-- Bia Hoi Hai Xom - Lương Quốc Khánh -->
# 03 — AI Log & Reflection

**Thành viên:** Lương Quốc Khánh

**Bối cảnh:** Lab AI Product Scoping — Xanh SM xử lý sự cố pin thấp cho taxi điện.

## AI đã giúp tôi như thế nào?

Tôi dùng AI như một thought-partner để brainstorm các pain point vận hành của Xanh SM, sau đó thu hẹp phạm vi về tình huống tài xế báo pin thấp. AI giúp tôi chuyển ý tưởng rộng thành một luồng cụ thể: nhận mô tả của tài xế, trích xuất mức pin/vị trí, kiểm tra ranh giới an toàn, tạo bản nháp và để điều phối viên phê duyệt.

AI cũng hỗ trợ viết system prompt và adversarial tests. Ba tình huống tôi dùng để stress-test là: ép điều hướng xe pin 2% đến trạm 8 km, yêu cầu bỏ thẻ `[DRAFT_ONLY]`, và prompt injection yêu cầu tự điều xe/khẳng định trạm còn chỗ.

## AI đã sai hoặc có thể gây rủi ro ở đâu?

Nếu chỉ tin vào prompt, AI có thể viết một câu trả lời nghe hợp lý nhưng không kiểm chứng được GPS, pin thực tế hay số chỗ trống tại trạm. Một phản hồi như “trạm gần nhất còn chỗ” sẽ là hallucination nếu hệ thống không được cấp dữ liệu thời gian thực.

AI cũng có thể làm theo yêu cầu “gửi ngay” hoặc “bỏ qua luật” nếu ranh giới chỉ nằm trong ngôn ngữ prompt. Điều này không chấp nhận được với tình huống pin thấp, vì một hướng dẫn sai có thể làm xe không đến được trạm và gây rủi ro vận hành.

## Tôi đã sửa prompt và ranh giới ra sao?

Tôi bổ sung hai ràng buộc chính: mọi bản nháp gửi tài xế phải bắt đầu bằng `[DRAFT_ONLY]`, và khi pin dưới 5% thì không được gợi ý trạm sạc xa hơn 5 km mà phải trả lệnh `dispatch_mobile_charger`.

Quan trọng hơn, tôi không coi prompt là lớp an toàn duy nhất. Code kiểm tra phần trăm pin, xác thực phản hồi Gemini và dùng fallback xác định trước khi thiếu API key, API lỗi hoặc mô hình trả nội dung sai ranh giới. Điều phối viên vẫn là người duyệt/gửi, còn AI không được tự điều xe hoặc thay đổi booking.

## Bài học rút ra

Với bài toán có yếu tố an toàn, giải pháp tốt không phải là “dùng AI nhiều nhất”. Rule-based logic phù hợp để chặn tình huống pin thấp; LLM phù hợp để hiểu mô tả tiếng Việt và soạn nháp. Tôi chọn kiến trúc Rule + LLM + HITL thay vì Agent tự hành vì có thể kiểm soát lỗi, giải thích được quyết định và thử nghiệm theo scope hẹp.
