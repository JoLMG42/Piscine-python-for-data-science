ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"

new_t = list(ft_tuple)
new_t[1] = "France!"
ft_tuple = tuple(new_t)

ft_set.remove("tutu!")
ft_set.add("Paris!")

ft_dict.update({'Hello': "42Paris"})

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
