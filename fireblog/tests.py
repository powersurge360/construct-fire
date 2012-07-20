from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.test import LiveServerTestCase, SimpleTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from fireblog.models import Entry


class EntryAdmin(LiveServerTestCase):
    fixtures = ["users"]

    def setUp(self):
        Entry.objects.create(
            title="Yeah, yeah, yeah",
            intro="Can't wait to get started",
            body="Hello!",
            published="d",
            author=User.objects.get(username="powersurge"),
        )

        self.browser = webdriver.Firefox()

    def log_in(self):
        # User opens the admin section
        self.browser.get(self.live_server_url + "/admin/")

        # User logs in
        username = self.browser.find_element_by_name("username")
        password = self.browser.find_element_by_name("password")

        username.send_keys("powersurge")
        password.send_keys("test")
        password.send_keys(Keys.RETURN)

    def test_add_unpublished_blog(self):
        # User logs in
        self.log_in()

        # User clicks blogs link.
        self.browser.find_element_by_link_text("Entries").click()

        # User clicks through to create blog entry
        self.browser.find_element_by_link_text("Add entry").click()

        # User creates blog entry
        self.browser.find_element_by_name("title").send_keys("A short history")
        self.browser.find_element_by_name("intro").send_keys("hello")
        self.browser.find_element_by_name("body").send_keys("Sup")
        self.browser.find_element_by_id("entry_form").submit()

        # Blog entry exists
        self.browser.find_element_by_link_text("A short history")

    def test_publish_existing_blog(self):
        # User logs in
        self.log_in()

        # User clicks blogs link.
        self.browser.find_element_by_link_text("Entries").click()

        # User sees that there is a draft available.
        published = self.browser.find_elements_by_css_selector(".row1 td")
        self.assertIn("Draft", published[2].text)

        # User clicks the draft.
        self.browser.find_element_by_link_text("Yeah, yeah, yeah").click()

        # User clicks the select and clicks publish.
        select = self.browser.find_element_by_id("id_published")
        for option in select.find_elements_by_tag_name("option"):
            if option.text == "Published":
                option.click()

        # User saves the entry.
        self.browser.find_element_by_id("entry_form").submit()

        # User sees that it is now marked published.
        published = self.browser.find_elements_by_css_selector(".row1 td")
        self.assertIn("Published", published[2].text)

    def tearDown(self):
        Entry.objects.all().delete()
        self.browser.quit()


class EntryTests(SimpleTestCase):
    fixtures = ["users"]

    def test_create_entry_success(self):
        entry = Entry()

        entry.title = "New Blog Entry"
        entry.intro = "Just a short introduction, don't mind me"
        entry.body = "How's it going buddy?"
        entry.published = "d"

        entry.author = User.objects.get(username="powersurge")

        entry.save()
        entry.full_clean()

        self.assertEqual(Entry.objects.count(), 1)

        entry = Entry.objects.get()
        self.assertEqual("New Blog Entry", entry.title)
        self.assertEqual("new-blog-entry", entry.slug)

    def test_create_entry_author_failure(self):
        entry = Entry()

        entry.title = "New Blog Entry"
        entry.intro = "Just a short introduction, don't mind me"
        entry.body = "How's it going buddy?"
        entry.published = "d"

        with self.assertRaises(IntegrityError):
            entry.save()

    def test_create_entry_blanked_failure(self):
        entry = Entry()

        with self.assertRaises(ValidationError):
            entry.full_clean()
