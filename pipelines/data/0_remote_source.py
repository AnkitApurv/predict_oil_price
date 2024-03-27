import pathlib

from playwright.sync_api import sync_playwright


def main():
    downloads_path = pathlib.Path("../../data/raw/")
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False, downloads_path=downloads_path)
        page = browser.new_page()
        page.goto("https://asb.opec.org/data/ASB_Data.php")
        # Start waiting for the download
        with page.expect_download() as download_info:
            # Perform the action that initiates download
            page.get_by_text("Download all").to_be_visible().click()
        download = download_info.value

        # Wait for the download process to complete and save the downloaded file somewhere
        download.save_as(downloads_path / pathlib.Path(download.suggested_filename))
        browser.close()
    return


if __name__ == "__main__":
    main()
