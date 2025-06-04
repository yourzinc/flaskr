import pytest
from flaskr import app

def test_layout_title():
    """Test that the layout.html file has the correct title and h1."""
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'<title>Amazon Q Developer Flask Demo</title>' in response.data
        assert b'<h1>Amazon Q Developer Python Flask Demo</h1>' in response.data

if __name__ == '__main__':
    pytest.main(['-xvs', __file__])