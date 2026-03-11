class bmi:
   def __init__(self,name,age,weight,h1,h2):
      self.name=name
      self.age=age
      self.weight=weight
      self.h1=h1
      self.h2=h2
   def get_bmi_result(self):
      print("Name:",self.name)
      H=((self.h1*30)+(self.h2*2.5))/100
      bmi=self.weight/(H**2)
      if(bmi<18.5):
       print("Underweight")
      elif(bmi>=18.5 and bmi<25):
       print("Normal weight")
      else:
       print("obese")
b1=bmi("Bala",20,61,5,9)
b1.get_bmi_result()
b2=bmi("Ram",23,90,5,8)
b2.get_bmi_result()
