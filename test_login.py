import json
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_scenario():
    """
    Test the login scenario on Fashion Stack e-commerce site
    using BrowserStack Cross-Browser Automation Agent.
    The aiAuthoring capability in browserstack.yml enables natural language commands.
    """
    # Initialize the WebDriver - BrowserStack SDK handles capabilities
    driver = webdriver.Remote(
        command_executor="https://hub.browserstack.com/wd/hub",
        options=webdriver.ChromeOptions()
    )

    try:
        # Step 1: Navigate to the Fashion Stack login page
        driver.get("https://ecommercebs.vercel.app")

        # Step 2: Use Cross-Browser Automation Agent with natural language
        # Navigate to login page
        driver.execute_script(
            'browserstack_executor: {"action": "ai", "arguments": {"task": "Click on the Login button in the top navigation bar"}}'
        )

        # Step 3: Verify we are on the login page
        driver.execute_script(
            'browserstack_executor: {"action": "ai", "arguments": {"task": "Verify that the page shows a Sign In form with Email Address and Password fields"}}'
        )

        # Step 4: Enter email address
        driver.execute_script(
            'browserstack_executor: {"action": "ai", "arguments": {"task": "Enter testuser@example.com in the Email Address field"}}'
        )

        # Step 5: Enter password
        driver.execute_script(
            'browserstack_executor: {"action": "ai", "arguments": {"task": "Enter Test@1234 in the Password field"}}'
        )

        # Step 6: Click Sign In button
        driver.execute_script(
            'browserstack_executor: {"action": "ai", "arguments": {"task": "Click the Sign In button"}}'
        )

        # Step 7: Verify login result
        driver.execute_script(
            'browserstack_executor: {"action": "ai", "arguments": {"task": "Verify the page response after clicking Sign In"}}'
        )

        # Mark test as passed
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status": "passed", "reason": "Login scenario completed successfully across platforms"}}'
        )

    except Exception as e:
        # Mark test as failed
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status": "failed", "reason": "Test failed"}}'
        )
        raise

    finally:
        driver.quit()


if __name__ == "__main__":
    test_login_scenario()
