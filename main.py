
from src.service.service_user import ServiceUser

service = ServiceUser()
resultado = service.add_user(None,"job1")
resultado2 = service.add_user("Nome1",None)
resultado3 = service.add_user("Nome","job")
resultado4 = service.add_user("Nome","job3")
resultado5 = service.add_user("Duda","job")
resultado6 = service.add_user("Maria","Suporte")
resultado7 = service.add_user("José","Comercial")

remove1 = service.remove_user(None,"job1")
remove2 = service.remove_user("Nome1",None)
remove3 = service.remove_user("Nome","job")
remove4 = service.remove_user("Nome","job3")
remove5 = service.remove_user("Duda","job")
remove6 = service.remove_user("Maria","Suporte")
remove7 = service.remove_user("José","Comercial")

print(resultado)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)
print(resultado6)
print(resultado7)

print(remove1)
print(remove2)
print(remove3)
print(remove4)
print(remove5)
print(remove6)
print(remove7)

#print(service.store.bd[0].name)