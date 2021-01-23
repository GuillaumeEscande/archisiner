"""
Test of location package
"""

from archisiner.model.location.location import Location

def test_getter_name():
    """Test to check the geter of name"""
    
    location = Location("test")
    assert location.name == "test"
    