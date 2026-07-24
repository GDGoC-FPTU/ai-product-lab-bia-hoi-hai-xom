import os
from PIL import Image, ImageDraw, ImageFont

img_w, img_h = 1400, 700
bg_color = (15, 23, 42) # Dark navy background
card_bg = (30, 41, 59)
border_color = (51, 65, 85)
highlight_red = (239, 68, 68)
text_white = (248, 250, 252)
text_muted = (148, 163, 184)
accent_cyan = (56, 189, 248)

img = Image.new('RGB', (img_w, img_h), color=bg_color)
draw = ImageDraw.Draw(img)

try:
    title_font = ImageFont.truetype('arial.ttf', 26)
    header_font = ImageFont.truetype('arial.ttf', 18)
    body_font = ImageFont.truetype('arial.ttf', 14)
except Exception:
    title_font = ImageFont.load_default()
    header_font = ImageFont.load_default()
    body_font = ImageFont.load_default()

# Title
draw.text((50, 35), 'XANH SM INTELLIGENT DISPATCHING — CURRENT-STATE WORKFLOW', fill=accent_cyan, font=title_font)
draw.text((50, 75), 'Manual Vehicle Rebalancing & Dispatching Process (Total Duration: 20 min / cycle)', fill=text_muted, font=body_font)

steps = [
    {'title': 'Step 1: Track Heatmap', 'actor': 'Dispatcher', 'desc': 'Observe map for demand spikes\n& unserved bookings', 'time': '2 min', 'bottleneck': False},
    {'title': 'Step 2: Lookup Imbalance', 'actor': 'Dispatcher', 'desc': 'Manual search for zones\nwith vehicle shortages', 'time': '5 min', 'bottleneck': True},
    {'title': 'Step 3: Match EV & Battery', 'actor': 'Dispatcher', 'desc': 'Check idle GPS position\n& battery SoC (>20%)', 'time': '5 min', 'bottleneck': True},
    {'title': 'Step 4: Draft Instruction', 'actor': 'Dispatcher', 'desc': 'Write SMS or call driver\nto move to demand hot-spot', 'time': '5 min', 'bottleneck': True},
    {'title': 'Step 5: Track Driver', 'actor': 'Dispatcher', 'desc': 'Verify if driver accepts\n& starts moving', 'time': '3 min', 'bottleneck': False},
]

box_w, box_h = 230, 340
start_x, start_y = 50, 140
spacing = 35

for i, step in enumerate(steps):
    x = start_x + i * (box_w + spacing)
    y = start_y
    
    b_color = highlight_red if step['bottleneck'] else border_color
    draw.rectangle([x, y, x + box_w, y + box_h], fill=card_bg, outline=b_color, width=3 if step['bottleneck'] else 2)
    
    # Header tag
    tag_bg = (127, 29, 29) if step['bottleneck'] else (30, 58, 138)
    draw.rectangle([x+10, y+15, x + box_w - 10, y + 45], fill=tag_bg)
    draw.text((x+20, y+20), f'Step {i+1}', fill=text_white, font=header_font)
    
    if step['bottleneck']:
        draw.ellipse([x + box_w - 40, y + 18, x + box_w - 18, y + 40], fill=highlight_red)
        draw.text((x + box_w - 32, y + 21), '!', fill=text_white, font=header_font)
        
    draw.text((x+15, y+65), step['title'].split(': ')[1], fill=text_white, font=header_font)
    draw.text((x+15, y+100), f"Actor: {step['actor']}", fill=accent_cyan, font=body_font)
    draw.text((x+15, y+125), f"Duration: {step['time']}", fill=highlight_red if step['bottleneck'] else text_muted, font=header_font)
    
    # Description wrap
    draw.text((x+15, y+165), step['desc'], fill=text_muted, font=body_font)
    
    if step['bottleneck']:
        draw.rectangle([x+15, y+275, x + box_w - 15, y + 310], fill=(153, 27, 27))
        draw.text((x+25, y+285), '🔴 BOTTLENECK', fill=text_white, font=body_font)
        
    # Arrow to next
    if i < len(steps) - 1:
        arrow_x = x + box_w + 5
        arrow_y = y + box_h // 2
        draw.line([arrow_x, arrow_y, arrow_x + 22, arrow_y], fill=accent_cyan, width=3)
        draw.polygon([(arrow_x + 22, arrow_y - 6), (arrow_x + 29, arrow_y), (arrow_x + 22, arrow_y + 6)], fill=accent_cyan)

# Legend at bottom
draw.rectangle([50, 520, 1350, 640], fill=card_bg, outline=border_color, width=2)
draw.ellipse([80, 545, 100, 565], fill=highlight_red)
draw.text((110, 547), '🔴 Bottleneck: Heavy manual processing, high latency (15 min total lost time per cycle)', fill=text_white, font=body_font)
draw.line([80, 595, 110, 595], fill=accent_cyan, width=3)
draw.polygon([(110, 589), (117, 595), (110, 601)], fill=accent_cyan)
draw.text((125, 587), '➡️ Handoff: Information transition between Dispatcher, GPS Telemetry, and Driver App', fill=text_white, font=body_font)

img.save('04-workflow-diagram.png')
print('Successfully generated 04-workflow-diagram.png')
