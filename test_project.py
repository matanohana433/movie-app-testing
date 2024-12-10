import pytest
from selenium.webdriver import ActionChains

user = "alex"
password = "alex123"
admin_user = "admin"
admin_password = "admin123"


class TestUser:
    @pytest.mark.functional
    def test_sign_up(self, setup):
        """Script 1 signup by a user:"""
        driver = setup[0]
        By = setup[1]
        driver.get("http://localhost:5000")
        driver.find_element(By.LINK_TEXT, "Signup").click()
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys(user)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button").click()
        signupmsg = driver.find_element(By.CSS_SELECTOR, ".success").text
        assert f"{user}" and "created successfully" in signupmsg, "test1 failed"
        print("test1 passed")

    @pytest.mark.functional
    def test_login(self, setup):
        """script 2 login by the user:"""
        driver = setup[0]
        By = setup[1]
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys(user)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button").click()
        loginmsg = driver.find_element(By.CSS_SELECTOR, ".success").text
        assert f"{user}" and "logged on successfully" in loginmsg, "test2 failed"
        print("test2 passed")

    @pytest.mark.functional
    def test_hello_msg(self, setup):
        """script 3 checking hello message:"""
        driver = setup[0]
        By = setup[1]
        assert user in driver.find_element(By.XPATH, "//div[@class='head']/p").text, "test3 failed"
        print("test3 passed")

    @pytest.mark.functional
    def test_leave_comment(self, setup):
        """script 4 leave a comment by the user:"""
        driver = setup[0]
        By = setup[1]
        movie_list = driver.find_elements(By.XPATH, "//div[@class='card-container']//div")
        movie_list[3].click()
        text_area = driver.find_element(By.XPATH, "//textarea[@name='freeform']")
        text_area.clear()
        my_comment = "Wow what a great movie"
        text_area.send_keys(my_comment)
        driver.find_element(By.XPATH, "//button").click()
        list_comments = driver.find_elements(By.CSS_SELECTOR, ".comment")
        for comment in list_comments:
            if user and my_comment in comment.text:
                print("test4 passed")
        assert driver.find_element(By.CSS_SELECTOR, ".success").is_displayed(), "test 5 failed"
        print("test5 passed")

    @pytest.mark.functional
    def test_logout(self, setup):
        """script 5 leave a comment by the user:"""
        driver = setup[0]
        By = setup[1]
        driver.find_element(By.LINK_TEXT, "Logout").click()
        assert f"{user}" and "logged out" in driver.find_element(By.CSS_SELECTOR, ".success").text, "test6 failed"
        print("test6 passed")


class TestAdmin:
    @pytest.mark.smoke
    def test_admin_login(self, setup):
        """"Script 6,7,8 checking admin login, dashboard data,
        and deleting new account that created and check number of comments after :"""
        driver = setup[0]
        By = setup[1]
        driver.get("http://localhost:5000/login")
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys(admin_user)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(admin_password)
        driver.find_element(By.XPATH, "//button").click()
        assert "logged on" in driver.find_element(By.CSS_SELECTOR, ".success").text, "test7 failed"
        print("test7 passed")

    @pytest.mark.smoke
    def test_dashboard(self, setup):
        driver = setup[0]
        By = setup[1]
        driver.find_element(By.LINK_TEXT, "Dashboard").click()
        # movie_comments_amount_before = int(
        #     driver.find_element(By.XPATH, "//table[2]//tr[td[contains(text(),'Spider-Man: No Way Home')]]/td[3]").text)
        # print(movie_comments_amount_before)
        new_user_row = driver.find_elements(By.XPATH, f"//table[1]//tr[td[text()='{user}']]/td")
        # for td in new_user_row:
        #     print(td.text)
        assert int(new_user_row[3].text) == 1, "test8 failed"
        print("test8 passed")

    @pytest.mark.functional
    def test_comments_count(self, setup):
        driver = setup[0]
        By = setup[1]
        movie_comments_amount_before = int(
            driver.find_element(By.XPATH, "//table[2]//tr[td[contains(text(),'Spider-Man: No Way Home')]]/td[3]").text)
        new_user_row = driver.find_elements(By.XPATH, f"//table[1]//tr[td[text()='{user}']]/td")
        new_user_row[4].click()
        movie_comments_amount_after = int(
            driver.find_element(By.XPATH, "//table[2]//tr[td[contains(text(),'Spider-Man: No Way Home')]]/td[3]").text)
        assert movie_comments_amount_before - 1 == movie_comments_amount_after, "test9 failed"
        print("test9 passed")

    @pytest.fixture(scope="class")
    def test_add_movie(self, setup):
        """Script 9 adding a movie:"""
        driver = setup[0]
        By = setup[1]
        Select = setup[2]
        driver.find_element(By.LINK_TEXT, "Searchmovie").click()
        driver.find_element(By.XPATH, "//input[@name='movie_name']").send_keys("black panther")
        driver.find_element(By.XPATH, "//button").click()
        movie_name = 'Black Panther: Wakanda Forever'
        dropdown = Select(driver.find_element(By.XPATH, "//select"))
        dropdown.select_by_visible_text(movie_name)
        driver.find_element(By.XPATH, "//button[@name='button_2']").click()
        driver.find_element(By.XPATH, "//button[@name='button_3']").click()
        new_movie_list = driver.find_elements(By.XPATH, "//div[@class='card-container']//div")
        new_movie_list[-1].click()
        assert driver.find_element(By.TAG_NAME, 'h1').text == movie_name, "test 10 failed"
        print("test10 passed")
        return movie_name, new_movie_list

    @pytest.mark.acceptance
    def test_check_dashboard_homepage(self, setup, test_add_movie):
        """Script 10 checking how many movies in the movie dashboard
        and homepage and if it matches the total in the dashboard table
        and checking if there's a new movie in the dashboard with no comments and deleting it:"""
        movie_name = test_add_movie[0]
        new_movie_list = test_add_movie[1]
        driver = setup[0]
        By = setup[1]
        driver.find_element(By.LINK_TEXT, "Dashboard").click()
        movie_list_dashboard = driver.find_elements(By.XPATH, "//table[2]//tr[td]")
        my_txt = driver.find_element(By.XPATH, "//p[2]").text
        my_sign = my_txt.find(":")
        assert len(new_movie_list) and len(movie_list_dashboard) == int(my_txt[my_sign + 1:]), "test 11 failed"
        print("test11 passed")
        movie_added = driver.find_elements(By.XPATH, f"//table[2]//tr[td[contains(text(),'{movie_name}')]]/td")
        assert movie_added[1].text == movie_name and int(movie_added[2].text) == 0, "test12 failed"
        print("test12 passed")
        movie_added[-1].click()
        assert driver.find_element(By.CSS_SELECTOR, ".success").is_displayed(), "test 13 failed"
        print("test13 passed")


class TestDesign:
    @pytest.fixture(scope="class")
    def test_hover_on_movie(self, setup):
        """Script 11, 12 checking if the hover is working
        in the image home page and nav bar:"""
        driver = setup[0]
        By = setup[1]
        driver.get("http://localhost:5000/login")
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys(admin_user)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(admin_password)
        driver.find_element(By.XPATH, "//button").click()
        action = ActionChains(driver)
        element = driver.find_element(By.XPATH, "//div[@class='card-container']/div[1]/a/img")
        border_before = element.value_of_css_property('border')
        action.move_to_element(element).perform()
        border_after = element.value_of_css_property('border')
        assert border_before != border_after, "test14 failed"
        print("test14 passed")
        return action

    @pytest.mark.acceptance
    def test_hover_on_navbar(self, setup, test_hover_on_movie):
        """checking navbar"""
        driver = setup[0]
        By = setup[1]
        action = test_hover_on_movie
        nav_element = driver.find_element(By.LINK_TEXT, "Searchmovie")
        nav_before = nav_element.value_of_css_property('background-color')
        action.move_to_element(nav_element).perform()
        nav_after = nav_element.value_of_css_property('background-color')
        assert nav_before != nav_after, "test15 failed"
        print("test15 passed")


class TestErrors:
    @pytest.mark.security
    def test_check_password(self, setup):
        """Script 13 creating a new user and try to log in with incorrect password:"""
        driver = setup[0]
        By = setup[1]
        driver.get("http://localhost:5000/signup")
        uname = "matantest"
        pword = "test123"
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys(uname)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(pword)
        driver.find_element(By.XPATH, "//button").click()
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys(uname)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123123")
        driver.find_element(By.XPATH, "//button").click()
        error_check = driver.find_element(By.CSS_SELECTOR, ".error")
        assert error_check.is_displayed() and error_check.text == "password incorrect", "test16 failed"
        print("test16 passed")
        # logging to admin in order to delete user:
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys(admin_user)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(admin_password)
        driver.find_element(By.XPATH, "//button").click()
        driver.find_element(By.LINK_TEXT, "Dashboard").click()
        driver.find_element(By.XPATH, f"//table[1]//tr[td[text()='{uname}']]/td[5]").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()

    @pytest.mark.security
    def test_duplicate_user(self, setup):
        """Script 14 checking for duplications of usernames:"""
        driver = setup[0]
        By = setup[1]
        driver.find_element(By.LINK_TEXT, "Signup").click()
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys("matan")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("justapassword")
        driver.find_element(By.XPATH, "//button").click()
        assert driver.find_element(By.CSS_SELECTOR, '.error').text == 'This username is already taken', "test17 failed"
        print("test17 passed")

    @pytest.mark.security
    def test_movie_already_exist(self, setup):
        """Script 15 try to add a movie that is already in the homepage:"""
        driver, By, Select = setup
        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys(admin_user)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(admin_password)
        driver.find_element(By.XPATH, "//button").click()
        driver.find_element(By.LINK_TEXT, "Searchmovie").click()
        driver.find_element(By.XPATH, "//input[@name='movie_name']").send_keys("Avengers")
        driver.find_element(By.TAG_NAME, "button").click()
        drop_down = Select(driver.find_element(By.XPATH, "//select"))
        drop_down.select_by_visible_text("Avengers: Endgame")
        driver.find_element(By.XPATH, "//button[@name='button_2']").click()
        driver.find_element(By.CSS_SELECTOR, ".card-content").click()
        errormsg = driver.find_element(By.CSS_SELECTOR, ".error")
        assert errormsg.is_displayed() and "Avengers: Endgame" in errormsg.text, "test18 failed"
        print("test18 passed")

    @pytest.mark.security
    def test_access(self, setup):
        """Script 16 check that a normal user or a guest cannot access
         users and movies management page:"""
        driver = setup[0]
        By = setup[1]
        driver.find_element(By.LINK_TEXT, "Logout").click()
        driver.get("http://127.0.0.1:5000/users/")
        (driver.find_element(By.CSS_SELECTOR, ".error").is_displayed()
         and driver.find_element(By.CSS_SELECTOR, ".error").text == "Access denied", "test17 failed")
        print("test17 passed")
        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys("matan")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("1234")
        driver.find_element(By.XPATH, "//button").click()
        driver.get("http://127.0.0.1:5000/users/")
        assert (driver.find_element(By.CSS_SELECTOR, ".error").is_displayed()
                and driver.find_element(By.CSS_SELECTOR, ".error").text == "Access denied"), "test19 failed"
        print("test19 passed")
        driver.find_element(By.LINK_TEXT, "Logout").click()

    @pytest.mark.security
    def test_wrong_credentials(self, setup):
        """Script 17 trying to log in with wrong credentials that do not exist:"""
        driver = setup[0]
        By = setup[1]
        driver.get("http://localhost:5000/login")
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys("usernotexist")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("1234")
        driver.find_element(By.XPATH, "//button").click()
        assert (driver.find_element(By.CSS_SELECTOR, ".error").is_displayed()
                and driver.find_element(By.CSS_SELECTOR, ".error").text == "username not exists"), "test20 failed"
        print("test20 passed")
