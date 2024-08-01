from src.my_python_project.main import main

def test_main(snapshot):
    actual = main()

    assert actual == snapshot
