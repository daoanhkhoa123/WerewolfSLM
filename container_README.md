```python

container = Container()
container.register("user_service", ()=>{})
container.register("variable", 6)

container.user_service(...) # run the user service function with params
container.variable *= 2
print(container.variable)
>>> 6



```