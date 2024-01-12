from weasyprint import HTML, CSS
from jinja2 import Template


# Load HTML template
with open("report.html") as file:
    template = Template(file.read())
with open("./css/style.css") as file:
    css_content = file.read()
# Sample data
data = {
    "report_title": "Vehicle Valuation Report",
    "company_logo": "https://imgs.search.brave.com/2qO5R_WdGMMGXX4FmzUTipMbAdys_UVJ1W_6J1i2ARI/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9jYXJy/aWVyd2F2ZS5mdXp1/LmNvbS9lbXBsb3ll/cnMvbWVkaXVtXzJl/M2QzMmE1LWZmMWQt/NDAxYy1hZDI1LTY4/OTMxZTA5NjNhNy5q/cGc",
    "valuation_company": "Automobile Valuers And Assessors Ltd",
    "qrcode": "https://imgs.search.brave.com/Tk-itLh4Avazn0HqXlOK2ALBDTFO3ZUvMGab4VWD_L4/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9pbWcu/ZnJlZXBpay5jb20v/cHJlbWl1bS1waG90/by9xci1jb2RlXzg2/OTQyMy0xMDc3Lmpw/Zz9zaXplPTYyNiZl/eHQ9anBn",
    "corporate_ref_no": "CORP123",
    "customer_email": "john@doe.com",
    "customer_id_number": "12345678",
    "postal_address": "P.O Box 12345",
    "kra_pin": "A879W0213364U",
    "driving_license_number": "K1234567B",
    "serial_number": "VINW012345",
    "issued_by": "Automobile Valuers And Assessors, Utawala",
    "insured_name": "John Doe",
    "insured_phone": "+254 712 345 678",
    "policy_number": "PL45678",
    "policy_expiry": "2023-12-31",
    "reg_no": "KCM 514K",
    "chassis_number": "chas12346",
    "color": "Red",
    "air_bags": "2 Airbags",
    "yom": 2010,
    "make": "Toyota",
    "engine_rating": "1800 CC",
    "engine_number": "ENG123",
    "odometer_reading": 185000,
    "lights": "LED Headlights and Brake lights",
    "repairs_noted": "Yes",
    "accident_damages_noted": "No",
    "roof_linings_damaged_or_repaired": "N/A",
    "paint_work_scratched_faded_dented": "Yes",
    "inner_wings_repaired_or_damaged": "No",
    "bumpers_outer_wing_repaired": "N/A",
    "body_complete_respray": "Yes",
    "upholstery_torn_faded_worn_out": "No",
    "chassis_kinked_or_damaged": "N/A",
    "parking_brake_effective": "Yes",
    "braking_system_okay": "Yes",
    "drive_shafts_worn_out": "No",
    "gearbox_okay": "Yes",
    "steering_system_okay": "Yes",
    "suspension_system_okay": "No",
    "cooling_system_operating_well": "Yes",
    "signs_of_leakage": "No",
    "engine_mountings_worn_out": "N/A",
    "indicator_lights_operate_well": "Yes",
    "wipers_operating_well": "Yes",
    "instrument_panel_lights_work_well": "No",
    "brake_lights_operate_well": "Yes",
    "headlights_operate_well": "Yes",
    "coachwork_notes": "Minor scratches on the right side, cracked rear bumper, scratches noted on doors, wings and bumpers.",
    "electrical_notes": "Instrument panel lights flicker occasionally",
    "mechanical_notes": "Suspension system needs attention, worn out arm bushes, engine and gearbox mountings",
    "extras": "AC, ABS, Alloy rims, Fog Lamps, Xenon Lights, Side Mirror Indicator, Wing Indicator, Wind Breakers, Tint Windows, Car Identity, CDL, Cup Holder, 2 Cut Off, Rear Disk brakes, Rear Spoiler with high mounted brake lights, Rear Wiper, Roof aerial, Head rest, Foot Rest, Arm Rest, Digital Odometer,Dual SRS Airbags, Inbuilt R/CD/TV Player, Paddle shifters,Power mirror, Power Steering, Power Window, Sun Visors, Tiptronic Gearbox, Telescopic Bonnet Damper, Wood Print Finish,",
    "anti_theft_car_alarm": "Yes",
    "tyres": "4 GOODYEAR TYRES 225/65R17 AND BRIDGESTONE T165/80R17 DONUT SPAREWHEEL ALL OF GOOD THREAD DEPTH",
    "general_condition": "Fair",
    "assessed_value": "850,000 /= (Eight Hundred And Fifty Thousand,Shillings Only )",
    "radio_estimate": "20000",
    "windscreen_estimate": "60000",
    "remarks": "Assessed value consistent with low usage.",
    "note": "N/A",
    "remedy": "Recommended suspension system repair and respray the affected panels, replace worn out arm bushes, engine and gearbox mountings.",
    "country_of_origin": "Japan",
    "inspection_date": "2023-05-15",
    "valuer": "John Valuer",
    "destination": "Vehicle Dealer",
    "inspection_location": "Nairobi, Kenya",
    "amendment": "None",
    "signature": "John Doe",
    "signature_date": "2023-05-16",
    "receipt_no": "REC12345",
    "fuel_type": "Petrol",
    "type": "AUTO 5 SEATER S/WAGON",
    "underwriter": "MUA Insurance",
    "image_paths": [
        "https://wip.client1.v2.flip-sys.com/_next/image/?url=https%3A%2F%2Finternal-work-bench.s3.amazonaws.com%2Fflip_V2%2Fvaluation%2Fimages%2Fv1.0.0%2FFCcuieTI.jpg%3FX-Amz-Algorithm%3DAWS4-HMAC-SHA256%26X-Amz-Credential%3DASIA22RMLRO25MB4S67U%252F20240108%252Feu-central-1%252Fs3%252Faws4_request%26X-Amz-Date%3D20240108T193702Z%26X-Amz-SignedHeaders%3Dhost%26X-Amz-Expires%3D3600%26X-Amz-Security-Token%3DIQoJb3JpZ2luX2VjEEMaDGV1LWNlbnRyYWwtMSJGMEQCID3q27rYMntJX98bXRCD4QORiDehuGgtrPubGm3rj3ujAiAL02MT%252BkO6%252BqysYOEOPBvpYY6lUivlSN79tbOYvxS16CrGBQjc%252F%252F%252F%252F%252F%252F%252F%252F%252F%252F8BEAIaDDc0NDE5NjExNTM4MSIMz5lopVvhlg2r1jzxKpoFjIkkv7nCWPNg88BxCKLKEOV42HFZb13K7ePtVu1l1kP403lDF6iCXoNzps4jlAnanb45RYRS0eKuKuB2jMwR2%252BwuDNxIFentxDynVOlbNHkISEaTH46afDy3aT4ydPJ6571JyShqktmSJc7L4MBBz%252FudFIQUBxvVqvhoLEMkIWeFHyxsX1orc2q6v5uo2W%252BI1oLnGRVU7HIy42g5AfgScICUAMitscioxSSnJzo%252Ffeh7ZahTJtJV1QJjyl%252Bd6uCFU0ocSscUfsjnqzzqQZKPnQcmoxn8i9053iXg%252BheZE4qSJ06sYaFEP63PYzeneHII3G8%252F%252BHyzRX0XjTfH2IwAIPBZwUWGczad6hz19lMFUy1hKp4MmY3GAIS0%252Fhp9kNMKiOrzTaY0DwOB2u9b4h5fSY%252BccawvyVuL%252B%252Fkq3f9elTR5V09Q31Vzz93JkPDwVtfzI2IoYT7qiuGymrS%252BiPyem6nIIqCsZ7%252BPJQL5Gi1D9dyGAkpotkqESpYs1ki6pLBvDw1Q9MfpUSheISgJOkcI5LDBls4x9ZGaqGbx%252BbRkRnpQZOIED3EzqNsGTIpJn42KF8GM9Rgn0jitfZjslcjw77O%252F2bqdejaL1uMgz5NpKchbjZNBUaEsyrZ2j3HP83ZzAQcNLDYIr3N6dY8hFW1ykRRVhPfJzmbp%252BYJZuLHRBWDZ%252FpRbyNCYEpLEb5ZHs8VDNBYPFhQrWRzJj8mRWkP2A%252BeTmrJ4csi%252BYI82mUaV3udCRn8hSJQf%252Fr75U4a1AaPA7iwtAX2lf8cHkHqNfXFRigaNzQhU6%252BJF1mO6wupbLr%252FjrYxhcK6hExA%252F8gMnTBjmtbvSyZs461FSkAPtxlPCoPA615XKHBVwpwNXrWO68MYhxqvbiI%252BotuEIMOOA8awGOrIBIZUG0oHkSR3KPSaQeOpOEjRSMHMfa6p%252BeE2GCDEg6M5Xg4CgjZbTkaR8GmE8CI1buxWx4EAZA4D9ZAT33pe4MihY2c%252BfSClRtLiFvq2EaPpqOqYgNz6rSIyKK2ak8ufsU5tzRhri2X8Hxc%252F%252FljDBtmKt6b9197CbP17dAWmkLmw2Il%252B%252FuxLK1TLQRQF5%252F%252Bp%252FIE5Yypp44JsxX%252FxBodp38GcfEscvaXA22dnecbjD%252Be0huw%253D%253D%26X-Amz-Signature%3Dca3ca30ec052b29d56954629323ab3a04ff7d7b2c174d292c4c7d6923c0ffbae&w=384&q=75",
        "https://wip.client1.v2.flip-sys.com/_next/image/?url=https%3A%2F%2Finternal-work-bench.s3.amazonaws.com%2Fflip_V2%2Fvaluation%2Fimages%2Fv1.0.0%2Ftl15pW72.jpg%3FX-Amz-Algorithm%3DAWS4-HMAC-SHA256%26X-Amz-Credential%3DASIA22RMLRO25MB4S67U%252F20240108%252Feu-central-1%252Fs3%252Faws4_request%26X-Amz-Date%3D20240108T193702Z%26X-Amz-SignedHeaders%3Dhost%26X-Amz-Expires%3D3600%26X-Amz-Security-Token%3DIQoJb3JpZ2luX2VjEEMaDGV1LWNlbnRyYWwtMSJGMEQCID3q27rYMntJX98bXRCD4QORiDehuGgtrPubGm3rj3ujAiAL02MT%252BkO6%252BqysYOEOPBvpYY6lUivlSN79tbOYvxS16CrGBQjc%252F%252F%252F%252F%252F%252F%252F%252F%252F%252F8BEAIaDDc0NDE5NjExNTM4MSIMz5lopVvhlg2r1jzxKpoFjIkkv7nCWPNg88BxCKLKEOV42HFZb13K7ePtVu1l1kP403lDF6iCXoNzps4jlAnanb45RYRS0eKuKuB2jMwR2%252BwuDNxIFentxDynVOlbNHkISEaTH46afDy3aT4ydPJ6571JyShqktmSJc7L4MBBz%252FudFIQUBxvVqvhoLEMkIWeFHyxsX1orc2q6v5uo2W%252BI1oLnGRVU7HIy42g5AfgScICUAMitscioxSSnJzo%252Ffeh7ZahTJtJV1QJjyl%252Bd6uCFU0ocSscUfsjnqzzqQZKPnQcmoxn8i9053iXg%252BheZE4qSJ06sYaFEP63PYzeneHII3G8%252F%252BHyzRX0XjTfH2IwAIPBZwUWGczad6hz19lMFUy1hKp4MmY3GAIS0%252Fhp9kNMKiOrzTaY0DwOB2u9b4h5fSY%252BccawvyVuL%252B%252Fkq3f9elTR5V09Q31Vzz93JkPDwVtfzI2IoYT7qiuGymrS%252BiPyem6nIIqCsZ7%252BPJQL5Gi1D9dyGAkpotkqESpYs1ki6pLBvDw1Q9MfpUSheISgJOkcI5LDBls4x9ZGaqGbx%252BbRkRnpQZOIED3EzqNsGTIpJn42KF8GM9Rgn0jitfZjslcjw77O%252F2bqdejaL1uMgz5NpKchbjZNBUaEsyrZ2j3HP83ZzAQcNLDYIr3N6dY8hFW1ykRRVhPfJzmbp%252BYJZuLHRBWDZ%252FpRbyNCYEpLEb5ZHs8VDNBYPFhQrWRzJj8mRWkP2A%252BeTmrJ4csi%252BYI82mUaV3udCRn8hSJQf%252Fr75U4a1AaPA7iwtAX2lf8cHkHqNfXFRigaNzQhU6%252BJF1mO6wupbLr%252FjrYxhcK6hExA%252F8gMnTBjmtbvSyZs461FSkAPtxlPCoPA615XKHBVwpwNXrWO68MYhxqvbiI%252BotuEIMOOA8awGOrIBIZUG0oHkSR3KPSaQeOpOEjRSMHMfa6p%252BeE2GCDEg6M5Xg4CgjZbTkaR8GmE8CI1buxWx4EAZA4D9ZAT33pe4MihY2c%252BfSClRtLiFvq2EaPpqOqYgNz6rSIyKK2ak8ufsU5tzRhri2X8Hxc%252F%252FljDBtmKt6b9197CbP17dAWmkLmw2Il%252B%252FuxLK1TLQRQF5%252F%252Bp%252FIE5Yypp44JsxX%252FxBodp38GcfEscvaXA22dnecbjD%252Be0huw%253D%253D%26X-Amz-Signature%3D9e785ea2ef3f9ccc1eaea72b03ac06c7a0e29597a1e9ee84f7ac6e5821b3726d&w=384&q=75",
        "https://wip.client1.v2.flip-sys.com/_next/image/?url=https%3A%2F%2Finternal-work-bench.s3.amazonaws.com%2Fflip_V2%2Fvaluation%2Fimages%2Fv1.0.0%2FoLi3gHYD.jpg%3FX-Amz-Algorithm%3DAWS4-HMAC-SHA256%26X-Amz-Credential%3DASIA22RMLRO25MB4S67U%252F20240108%252Feu-central-1%252Fs3%252Faws4_request%26X-Amz-Date%3D20240108T193702Z%26X-Amz-SignedHeaders%3Dhost%26X-Amz-Expires%3D3600%26X-Amz-Security-Token%3DIQoJb3JpZ2luX2VjEEMaDGV1LWNlbnRyYWwtMSJGMEQCID3q27rYMntJX98bXRCD4QORiDehuGgtrPubGm3rj3ujAiAL02MT%252BkO6%252BqysYOEOPBvpYY6lUivlSN79tbOYvxS16CrGBQjc%252F%252F%252F%252F%252F%252F%252F%252F%252F%252F8BEAIaDDc0NDE5NjExNTM4MSIMz5lopVvhlg2r1jzxKpoFjIkkv7nCWPNg88BxCKLKEOV42HFZb13K7ePtVu1l1kP403lDF6iCXoNzps4jlAnanb45RYRS0eKuKuB2jMwR2%252BwuDNxIFentxDynVOlbNHkISEaTH46afDy3aT4ydPJ6571JyShqktmSJc7L4MBBz%252FudFIQUBxvVqvhoLEMkIWeFHyxsX1orc2q6v5uo2W%252BI1oLnGRVU7HIy42g5AfgScICUAMitscioxSSnJzo%252Ffeh7ZahTJtJV1QJjyl%252Bd6uCFU0ocSscUfsjnqzzqQZKPnQcmoxn8i9053iXg%252BheZE4qSJ06sYaFEP63PYzeneHII3G8%252F%252BHyzRX0XjTfH2IwAIPBZwUWGczad6hz19lMFUy1hKp4MmY3GAIS0%252Fhp9kNMKiOrzTaY0DwOB2u9b4h5fSY%252BccawvyVuL%252B%252Fkq3f9elTR5V09Q31Vzz93JkPDwVtfzI2IoYT7qiuGymrS%252BiPyem6nIIqCsZ7%252BPJQL5Gi1D9dyGAkpotkqESpYs1ki6pLBvDw1Q9MfpUSheISgJOkcI5LDBls4x9ZGaqGbx%252BbRkRnpQZOIED3EzqNsGTIpJn42KF8GM9Rgn0jitfZjslcjw77O%252F2bqdejaL1uMgz5NpKchbjZNBUaEsyrZ2j3HP83ZzAQcNLDYIr3N6dY8hFW1ykRRVhPfJzmbp%252BYJZuLHRBWDZ%252FpRbyNCYEpLEb5ZHs8VDNBYPFhQrWRzJj8mRWkP2A%252BeTmrJ4csi%252BYI82mUaV3udCRn8hSJQf%252Fr75U4a1AaPA7iwtAX2lf8cHkHqNfXFRigaNzQhU6%252BJF1mO6wupbLr%252FjrYxhcK6hExA%252F8gMnTBjmtbvSyZs461FSkAPtxlPCoPA615XKHBVwpwNXrWO68MYhxqvbiI%252BotuEIMOOA8awGOrIBIZUG0oHkSR3KPSaQeOpOEjRSMHMfa6p%252BeE2GCDEg6M5Xg4CgjZbTkaR8GmE8CI1buxWx4EAZA4D9ZAT33pe4MihY2c%252BfSClRtLiFvq2EaPpqOqYgNz6rSIyKK2ak8ufsU5tzRhri2X8Hxc%252F%252FljDBtmKt6b9197CbP17dAWmkLmw2Il%252B%252FuxLK1TLQRQF5%252F%252Bp%252FIE5Yypp44JsxX%252FxBodp38GcfEscvaXA22dnecbjD%252Be0huw%253D%253D%26X-Amz-Signature%3D3ed759e2ef41859b9b48b5503dcf8a706b7aa6e99936e241cc14c53ea7e6747a&w=384&q=75",
        "https://wip.client1.v2.flip-sys.com/_next/image/?url=https%3A%2F%2Finternal-work-bench.s3.amazonaws.com%2Fflip_V2%2Fvaluation%2Fimages%2Fv1.0.0%2FpdTmMfRN.jpg%3FX-Amz-Algorithm%3DAWS4-HMAC-SHA256%26X-Amz-Credential%3DASIA22RMLRO25MB4S67U%252F20240108%252Feu-central-1%252Fs3%252Faws4_request%26X-Amz-Date%3D20240108T193702Z%26X-Amz-SignedHeaders%3Dhost%26X-Amz-Expires%3D3600%26X-Amz-Security-Token%3DIQoJb3JpZ2luX2VjEEMaDGV1LWNlbnRyYWwtMSJGMEQCID3q27rYMntJX98bXRCD4QORiDehuGgtrPubGm3rj3ujAiAL02MT%252BkO6%252BqysYOEOPBvpYY6lUivlSN79tbOYvxS16CrGBQjc%252F%252F%252F%252F%252F%252F%252F%252F%252F%252F8BEAIaDDc0NDE5NjExNTM4MSIMz5lopVvhlg2r1jzxKpoFjIkkv7nCWPNg88BxCKLKEOV42HFZb13K7ePtVu1l1kP403lDF6iCXoNzps4jlAnanb45RYRS0eKuKuB2jMwR2%252BwuDNxIFentxDynVOlbNHkISEaTH46afDy3aT4ydPJ6571JyShqktmSJc7L4MBBz%252FudFIQUBxvVqvhoLEMkIWeFHyxsX1orc2q6v5uo2W%252BI1oLnGRVU7HIy42g5AfgScICUAMitscioxSSnJzo%252Ffeh7ZahTJtJV1QJjyl%252Bd6uCFU0ocSscUfsjnqzzqQZKPnQcmoxn8i9053iXg%252BheZE4qSJ06sYaFEP63PYzeneHII3G8%252F%252BHyzRX0XjTfH2IwAIPBZwUWGczad6hz19lMFUy1hKp4MmY3GAIS0%252Fhp9kNMKiOrzTaY0DwOB2u9b4h5fSY%252BccawvyVuL%252B%252Fkq3f9elTR5V09Q31Vzz93JkPDwVtfzI2IoYT7qiuGymrS%252BiPyem6nIIqCsZ7%252BPJQL5Gi1D9dyGAkpotkqESpYs1ki6pLBvDw1Q9MfpUSheISgJOkcI5LDBls4x9ZGaqGbx%252BbRkRnpQZOIED3EzqNsGTIpJn42KF8GM9Rgn0jitfZjslcjw77O%252F2bqdejaL1uMgz5NpKchbjZNBUaEsyrZ2j3HP83ZzAQcNLDYIr3N6dY8hFW1ykRRVhPfJzmbp%252BYJZuLHRBWDZ%252FpRbyNCYEpLEb5ZHs8VDNBYPFhQrWRzJj8mRWkP2A%252BeTmrJ4csi%252BYI82mUaV3udCRn8hSJQf%252Fr75U4a1AaPA7iwtAX2lf8cHkHqNfXFRigaNzQhU6%252BJF1mO6wupbLr%252FjrYxhcK6hExA%252F8gMnTBjmtbvSyZs461FSkAPtxlPCoPA615XKHBVwpwNXrWO68MYhxqvbiI%252BotuEIMOOA8awGOrIBIZUG0oHkSR3KPSaQeOpOEjRSMHMfa6p%252BeE2GCDEg6M5Xg4CgjZbTkaR8GmE8CI1buxWx4EAZA4D9ZAT33pe4MihY2c%252BfSClRtLiFvq2EaPpqOqYgNz6rSIyKK2ak8ufsU5tzRhri2X8Hxc%252F%252FljDBtmKt6b9197CbP17dAWmkLmw2Il%252B%252FuxLK1TLQRQF5%252F%252Bp%252FIE5Yypp44JsxX%252FxBodp38GcfEscvaXA22dnecbjD%252Be0huw%253D%253D%26X-Amz-Signature%3Da8b4476ee2915429c63b53c92069d9e1475e25633d929d75cbb6db3ba8f4e1de&w=384&q=75",
    ],
    "corporation": "flip",
    "anti_theft": "CAR ALARM",
}

html_output = template.render(data)

# options = {
#     'page-size': 'Letter',
#     'margin-top': '0mm',
#     'margin-right': '0mm',
#     'margin-bottom': '0mm',
#     'margin-left': '0mm',
# }


# HTML(string=html_output).write_pdf("report_sample_doc.pdf")

html = HTML(string=html_output)
css = CSS(string=css_content)
html.write_pdf("report_sample_doc.pdf", stylesheets=[css])
