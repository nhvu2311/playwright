from playwright.sync_api import sync_playwright

def test_e_commerce_website():
    # Khởi tạo Playwright
    with sync_playwright() as p:
        # Khởi tạo trình duyệt mới (có thể thay đổi thành 'firefox' hoặc 'webkit')
        browser = p.chromium.launch()
        page = browser.new_page()

        # Truy cập trang web thương mại điện tử
        page.goto("https://your-ecommerce-website.com")

        # Điền form (ví dụ: tìm kiếm sản phẩm)
        page.fill("input[name='search']", "Áo thun")
        page.click("button[type='submit']")

        # Chờ trang tải hoàn thành
        page.wait_for_load_state("networkidle")

        # Thực hiện thao tác chuyển trang (ví dụ: chọn sản phẩm đầu tiên)
        page.click("div.product:first-child")

        # Thực hiện các thao tác khác (ví dụ: thêm vào giỏ hàng, thanh toán, ...)
        # Ví dụ: thêm vào giỏ hàng
        page.click("button.add-to-cart")

        # Chờ trang tải hoàn thành
        page.wait_for_load_state("networkidle")

        # Ví dụ: chuyển đến trang thanh toán
        page.click("button.checkout")

        # Chờ trang tải hoàn thành
        page.wait_for_load_state("networkidle")

        # Thực hiện các tương tác khác tùy thuộc vào kịch bản kiểm thử của bạn

        # Đóng trình duyệt
        browser.close()

# Chạy hàm kiểm thử
test_e_commerce_website()
