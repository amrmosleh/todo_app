from app import app
def test1():
    """
    this function tests that the flask app has a correct response code when the application goes live.
    """
    response = app.test_client().get('/')
    assert response.status_code == 200
def test2():
    """
    this function tests that the flask app has a correct response code when the application goes live.
    """
    response = app.test_client().get('/edit')
    assert response.status_code == 200
def test3():
    """A dummy docstring."""
    response = app.test_client().get("/edit")
    assert b"To-Do Application" in response.data
    assert b"Todo Title" in response.data
    assert b"Add" in response.data