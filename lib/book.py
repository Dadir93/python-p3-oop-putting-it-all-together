#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

class TestBook:
    def title_and_page_count(self):
        book = Book("And Then There Were None", 272)
        assert book.page_count == 272
        assert book.title == "And Then There Were None"

    def int_page_count(self):
        book = Book("And Then There Were None", 272)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        book.page_count = "not an integer"
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue().strip() == "page_count must be an integer\n"

    def turn_page_output(self):
        book = Book("The World According to Garp", 69)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        book.turn_page()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue().strip() == "Flipping the page...wow, you read fast!"
