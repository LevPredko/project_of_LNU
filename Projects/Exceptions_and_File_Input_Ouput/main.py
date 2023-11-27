from Projects.Exceptions_and_File_Input_Ouput.ContentFilter import ContentFilter

cf = ContentFilter("cf_example1.txt")
print(cf)
cf.uniform("uniform.txt", mode='w', case="upper")
cf.uniform("uniform.txt", mode='a', case="lower")
cf.reverse("reverse.txt", mode='w', unit="word")
cf.reverse("reverse.txt", mode='a', unit="line")
cf.transpose("transpose.txt", mode='w')
