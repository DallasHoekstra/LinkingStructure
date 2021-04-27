import pytest
import unittest
from unittest.mock import patch
import WebGraph as WG

def test_Web_Graph_initializes_empty():
    test_wg = WG.WebGraph()
    assert len(test_wg.pages) == 0

def test_Page_initializes_with_provided_title():

    title1 = "best loans"
    title2 = "best credit cards"

    page1 = WG.Page(title1)
    page2 = WG.Page(title2)

    assert page1.title == title1
    assert page2.title == title2

def test_Page_initializes_with_empty_connections():
    title1 = "best loans"
    page1 = WG.Page(title1)

    assert len(page1.links) == 0

def test_initial_add_link_inserts_title_and_sets_counter_to_1():
    title1 = "best loans"
    title2 = "best credit cards"
    
    page1 = WG.Page(title1)
    page1.add_link(title2)

    assert title2 in page1.links.keys()
    assert page1.links[title2] == 1

def test_subsequent_same_title_add_link_increments_counter():
    title1 = "best loans"
    title2 = "best credit cards"
    
    page1 = WG.Page(title1)
    page1.add_link(title2)
    page1.add_link(title2)

    assert page1.links[title2] == 2

def test_Web_Graph_add_page_adds_page_to_pages():
    title1 = "Best Credit Cards"
    test_page = WG.Page(title1)

    test_graph = WG.WebGraph()
    test_graph.add_page(test_page)

    assert test_graph.pages[test_page.title].title == test_page.title
