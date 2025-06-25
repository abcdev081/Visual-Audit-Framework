# utils/gestures.py

def swipe_down(driver):#Used to scroll down a page
    
    size = driver.get_window_size()
    start_x = size["width"] * 0.5
    start_y = size["height"] * 0.8
    end_y = size["height"] * 0.3
    driver.swipe(start_x, start_y, start_x, end_y, duration=800)

def swipe_up(driver):#Used to scroll up a page
    
    size = driver.get_window_size()
    start_x = size["width"] * 0.5
    start_y = size["height"] * 0.3
    end_y = size["height"] * 0.8
    driver.swipe(start_x, start_y, start_x, end_y, duration=800)
