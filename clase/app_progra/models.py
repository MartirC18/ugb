from django.db import models
class VEHICULOS(models.Model):
    marca=models.CharField(max_length=100)
    modelo=models.CharField(max_length=100)
    anio=models.CharField(max_length=100,null=True)
    tipo=models.CharField(max_length=100)
    disponibilidad=models.CharField(max_length=100)

class CLIENTES(models.Model):
    Nombre_Cliente=models.CharField(max_length=100)
    Direccion=models.CharField(max_length=100)
    Telefono=models.CharField(max_length=100,null=True)
    Edad=models.CharField(max_length=100,null=True)
    Sexo=models.CharField(max_length=100)

class EMPLEADOS(models.Model):
    Nombre=models.CharField(max_length=100)
    Edad=models.CharField(max_length=100,null=True)
    Telefono=models.CharField(max_length=100,null=True)
    Sexo=models.CharField(max_length=100)



class Registro(models.Model):
    Cliente_id=models.ForeignKey(CLIENTES,on_delete=models.CASCADE,null=True)
    vehiculo_id=models.ForeignKey(VEHICULOS,on_delete=models.CASCADE,null=True)
    Fecha_Salida=models.DateField
    empleado_id=models.ForeignKey(EMPLEADOS,on_delete=models.CASCADE,null=True)
