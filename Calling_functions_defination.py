from FUNCTION_CONCEPTS import Types_of_functions as t
#call the function with the help of module name
res=t.login_credentials2(11445566,"alladi@123")
print("status:",res)
print("\nfunction with arguments and without return type:")
res2=t.login_credentials(11445566,"alladi@123")
print("status:",res2)
print("\na function without arguments with return type:")

res3=t.system_properties_info()
print("info:",res3)

print("\n a function without parameters and without return type:")
t.system_properties_info2()