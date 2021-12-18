import supportingMethods
from driverInitialization import *


def start_test(self=None):
    try:
        all_catg_btn = driver.find_element_by_id("nav-hamburger-menu")
        all_catg_btn.click()

        computers_item = driver.find_element_by_xpath('//*[@id="hmenu-content"]/ul[1]/li[8]/a')
        if computers_item.text == "Computers":
            computers_item.click()
            print('\x1b[6;30;42m' + "Inside Computers Section" + "\033[0m")

        compu_tablets_item = driver.find_element_by_xpath('//*[@id="hmenu-content"]/ul[6]/li[5]/a')
        if compu_tablets_item.text == "Computers & Tablets":
            compu_tablets_item.click()
            print('\x1b[6;30;42m' + "Inside Computers & Tablets Section" + "\033[0m")

        samsung_chkbox = driver.find_element_by_xpath('//*[@id="p_89/Samsung Electronics"]/span/a/div')
        if samsung_chkbox.is_displayed():
            samsung_chkbox.click()
            print('\x1b[6;30;42m' + "Samsung Products Selected" + "\033[0m")

# Iterate over the 24 products shown per page if the selected products is out of stock
        for i in range(1, 24):
        # slct_product = driver.find_element_by_class_name("s-image")
            slct_product = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[%s]'%i)
            if slct_product.is_displayed():
                slct_product.click()
                print('\x1b[6;30;42m' + "Product Selected " + "\033[0m")
                is_available = driver.find_element_by_id("availability")
                if is_available.text == "In Stock.":
                    add_to_cart_btn = driver.find_element_by_id("add-to-cart-button")
                    if add_to_cart_btn.is_displayed():
                        add_to_cart_btn.click()
                        print('\x1b[6;30;42m' + "Add to Cart action is Taken" + "\033[0m")
                    cart_add_confrm = driver.find_element_by_xpath(
                        '//*[@id="sw-atc-details-single-container"]/div[2]/div[1]/span')
                    assert "Added to Cart" in cart_add_confrm.text, '\x1b[6;30;41m' + "Adding Item to Cart has Failed " + "\033[0m"
                    print('\x1b[6;30;42m' + "Item Added to Cart " + "\033[0m")
                    break

        nav_cart = driver.find_element_by_id("nav-cart")
        if nav_cart.is_displayed():
            nav_cart.click()
            print('\x1b[6;30;42m' + "Inside Cart " + "\033[0m")

        remove_item = driver.find_element_by_xpath('//input[@value="Delete"]')
        if remove_item.is_displayed():
            remove_item.click()
            print('\x1b[6;30;43m' + "Item Pending Removal " + "\033[0m")

# In this part I meant to let the assertion fail to print the assertion error, you can find a screenshot taken in /app folder
        removal_conf = driver.find_element_by_class_name("sc-product-link")
        assert "was removed from Shopping Cart" in removal_conf.text, '\x1b[6;30;41m' + "Error While Removing The Item " + "\033[0m"
        print('\x1b[6;30;42m' + "Item Removed Successfully " + "\033[0m")

# Print Exception Error Message and take a screenshot of the page where the error happened and then close browser
    except Exception as e:
        print('\x1b[6;30;41m' + "Exception Found: " + "\033[0m" + str(e))
        driver.save_screenshot(supportingMethods.timestamp_filename())
        tear_down()





def tear_down():
    driver.quit()


start_test()
