x = 50   

def test_scope():
    x = 20   
    print("Local x:", x)

test_scope()
print("Global x:", x)